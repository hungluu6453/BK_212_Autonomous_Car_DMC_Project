import cv2 as cv
import mediapipe as mp
from . helper import *
import serial
import socket

#import copy
#from collections import Counter
#from collections import deque
#import os 
#import time
#from datetime import datetime 
#from serial import Serial
#import socket, threading, sys, traceback, os, time

"""
SERIAL = False
s = None
if SERIAL:
    s = serial.Serial(port = 'COM3', baudrate=19200, bytesize = 8, timeout = 1)

LAN = True
SERVER_PORT = 10
rtspSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
LOCAL_HOST, PORT = ("172.20.10.3", SERVER_PORT)

if LAN:
    try:
        rtspSocket.bind((LOCAL_HOST, PORT))
        rtspSocket.listen(5)
        (clientConnected, clientAddress) = rtspSocket.accept()
        print(print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1])))
    except:
        print('Can not open port')"""



class HandGesture():
    def __init__(self):     #, connect_status = False, SERIAL = False, LAN = True):
        
        ## Connection 
        #self.connectStatus = connect_status
        #self.SERIAL = SERIAL
        #self.s = None
        #self.LAN = LAN
        #self.SERVER_PORT = 10
        #self.rtspSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.LOCAL_HOST, self.PORT = ("172.20.10.4", self.SERVER_PORT)
        #self.LOCAL_HOST, self.PORT = (socket.gethostbyname(socket.gethostname()), self.SERVER_PORT)
        #self.clientConnected = None
        #self.clientAddress = None
        
        #if self.connectStatus:
        #    self.connect()

        ## Output to send to Pi
        self.hand_sign_id = 3 
        self.previous_action_id = 0
        self.current_action_id = 0
        self.auto_mode = False
        self.light_mode = False

        ## Webcam
        self.use_brect = True
        self.cap_width = 320
        self.cap_height = 240
        self.min_detection_confidence  = 0.8
        self.min_tracking_confidence = 0.8
        self.cap_device = 0
        self.cap = cv.VideoCapture(self.cap_device)
        self.cap.set(cv.CAP_PROP_FRAME_WIDTH, self.cap_width)
        self.cap.set(cv.CAP_PROP_FRAME_HEIGHT, self.cap_height)

        ## Hand detection
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
        static_image_mode= False,
            max_num_hands=1,
            min_detection_confidence=self.min_detection_confidence,
            min_tracking_confidence=self.min_tracking_confidence,
        )
        self.keypoint_classifier = KeyPointClassifier()
        self.action_list = ["stop", "forward", "backward", "go right", "go left", "spin left", "spin right", "forward faster", "do nothing", "diagonal left", "diagonal right", "change mode", "change light"]
        self.keypoint_classifier_labels = ["upward fist", "normal fist", "reverse fist", "close palm", "reverse palm", "thumb left", "thumb right", "OK", "index up"]
        self.printsen = ["Car is staying still 🛑", 
        "Car is moving forward at normal speed ⬆️", "Car is moving backward ⬇️", "Car is moving right ➡️", "Car is moving left ⬅️","Car is spinning left ↪️", "Car is spinning right ↩️", "Car is moving forward at fast speed ⬆️⬆️", "Car is doing nothing", "Car is moving diagonally left ↖️", "Car is moving diagonally right ↗️", "Car is changing mode", "Car is changing light"]
        #self.printsen = ["Car is staying still", "Car is moving forward at normal speed", "Car is moving backward", "Car is moving right", "Car is moving left", "Car is spinning right", "Car is spinning left", "Car is moving forward at fast speed", "Car is doing nothing", "Car is moving diagonally left", "Car is moving diagonally right", "Car is changing mode", "Car is changing light"]
        #self.keypoint_classifier_labels = ["upward fist", "normal fist", "reverse fist", "close palm", "reverse palm", "thumb left", "thumb right", "OK", "index up", "open palm"]

        #self.draw_on_cam = False

    def main(self):
        __, image = self.cap.read()
        image = cv.flip(image, 1) 
        debug_image = copy.deepcopy(image)

        ##############################################################
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

        image.flags.writeable = False
        results = self.hands.process(image)
        image.flags.writeable = True

        ####################################################################
        if results.multi_hand_landmarks is not None: # if there is a hand
            for hand_landmarks, handedness in zip(results.multi_hand_landmarks,
                                                results.multi_handedness):
                # Calculation of rectangle boundaries
                brect = calc_bounding_rect(debug_image, hand_landmarks)
                
                # Landmark calculation
                landmark_list = calc_landmark_list(debug_image, hand_landmarks)

                # Conversion to relative coordinates / normalized coordinates
                pre_processed_landmark_list = pre_process_landmark(
                    landmark_list)

                # Hand sign classification
                self.hand_sign_id = self.keypoint_classifier(pre_processed_landmark_list)
                """
                cv.putText(debug_image, "Detected shape: " + self.keypoint_classifier_labels[self.hand_sign_id], 
                (10,30), 
                cv.FONT_HERSHEY_DUPLEX, 
                0.5, (0, 0, 0), 1, cv.LINE_AA)"""
                self.previous_action_id = self.current_action_id
                self.current_action_id = self.getActionAndMode(self.hand_sign_id, hand_landmarks.landmark[0].x, hand_landmarks.landmark[8].x)

                ## Draw result
                #debug_image = draw_bounding_rect(self.use_brect, debug_image, brect)
                debug_image = draw_landmarks(debug_image, landmark_list)
                
                """
                debug_image = draw_label(
                    debug_image,
                    brect,
                    handedness,
                    self.action_list[self.current_action_id],
                    #keypoint_classifier_labels[hand_sign_id],
                    self.auto_mode
                )"""
                
        else: # if there is no hand
            self.current_action_id = 0 # do nothing
            """cv.putText(debug_image, "Detected shape: None", 
                (10,30), 
                cv.FONT_HERSHEY_DUPLEX, 
                0.5, (0, 0, 0), 1, cv.LINE_AA)"""

        #current_mode = "Auto" if self.auto_mode else "Manual"
        #current_light = "On" if self.light_mode else "Off"
        #cv.putText(debug_image, "Current Mode: " + current_mode, (10,60), cv.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0), 1, cv.LINE_AA)
        #cv.putText(debug_image, "Car Light: " + current_light, (10,90), cv.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0), 1, cv.LINE_AA)

        # SEND TO PI ThE self.CURRENT_ACTION_ID
        #if self.connectStatus:
        #    self.sendToPi()



        ##########################################################################
        return debug_image, self.current_action_id, self.printsen[self.current_action_id]

    def getActionAndMode(self, hand_sign_id, hand_place, hand_tip):
        if hand_sign_id == 0 or hand_sign_id == 1: # UPWARD FIST OR NORMAL FIST
            if hand_place < 0.33: # LEFT SCREEN FIST
                return 9 # diagonal left
            elif hand_place > 0.66: # RIGHT SCREEN FIST
                return 10 # diagonal right
            else:
                if hand_sign_id == 0: # MIDDLE SCREEN UPWARD FIST
                    return 1 # normal forward
                else: # MIDDLE SCREEN NORMAL FIST
                    return 7 # fast forward
        elif hand_sign_id == 2: # REVERSE FIST
            return 2 # backward
        elif hand_sign_id == 3: # PALM
            return 0 # stop
        elif hand_sign_id == 4: # REVERSE PALM
            return 8 # do nothing
        elif hand_sign_id == 5: # THUMB LEFT
            return 4 # go left
        elif hand_sign_id == 6: # THUMB RIGHT
            return 3 # go right
        elif hand_sign_id == 7: # OK
            #if (self.previous_action_id != 11): # if change mode first time
            #    self.auto_mode = not self.auto_mode
            #return 11 # change mode
            return 8
        elif hand_sign_id == 8: # INDEX UP
            if hand_tip < 0.5:
                return 6 # spin left
            else:
                return 5 # spin right
            #if (self.previous_action_id != 12): # if change light first time
            #    self.light_mode = not self.light_mode
            #return 12 # change light
            #return 8

        #elif hand_sign_id == 9: # OPEN PALM
        #    if hand_place < 0.5:
        #        return 9 # diagonal left
        #    else:
        #        return 10 # diagonal right


    def adjustSize(self,w,h):
        self.cap.set(cv.CAP_PROP_FRAME_WIDTH, w)
        self.cap.set(cv.CAP_PROP_FRAME_HEIGHT, h)

    """
    def connect(self):
        if self.SERIAL:
            self.s = serial.Serial(port = 'COM3', baudrate=19200, bytesize = 8, timeout = 1)
        if self.LAN:
            try:
                self.rtspSocket.bind((self.LOCAL_HOST, self.PORT))
                self.rtspSocket.listen(5)
                (self.clientConnected, self.clientAddress) = self.rtspSocket.accept()
                print("Accepted a connection request from %s:%s"%(self.clientAddress[0], self.clientAddress[1]))
            except:
                print('Can not open port')

    def sendToPi(self):
        if self.SERIAL:
            self.s.write(str.encode(str(self.current_action_id)+'.'))
            print(self.current_action_id)
        if self.LAN:
            self.clientConnected.send(str.encode(str(self.current_action_id)+'.'))"""
    
if __name__ == "__main__":
    #Hand_Object = HandGesture(connect_status=False, LAN=False)
    Hand_Object = HandGesture()
    while True:
        key = cv.waitKey(1)
        if key == 27:
            break
        image, __ , __ = Hand_Object.main()
        #cv.imwrite('F:\\Hung Luu\\BK_19_22\\3_Junior\\212\\DMC\\App Design\\Self-drviving-Car_App\\images\\hand_gesture_images\\cache.jpeg',
                    #image)
        cv.imshow('Hand Gesture Recognition', image)

    Hand_Object.cap.release()
    cv.destroyAllWindows()
