import copy
from collections import Counter
from collections import deque
import cv2 as cv
import mediapipe as mp

if __package__ is None or __package__ == '':
    # uses current directory visibility
    from helper import *
else:
    # uses current package visibility
    from .helper import *

class HandGesture():
    def __init__(self):
        self.previous_action_id = 0
        self.current_action_id = 0
        self.auto_mode = False
        self.light_mode = False

        self.use_brect = True
        self.cap_width = 320
        self.cap_height = 240
        self.min_detection_confidence  = 0.7
        self.min_tracking_confidence = 0.7

        self.cap_device = 0
        self.cap = cv.VideoCapture(self.cap_device)
        self.cap.set(cv.CAP_PROP_FRAME_WIDTH, self.cap_width)
        self.cap.set(cv.CAP_PROP_FRAME_HEIGHT, self.cap_height)
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
        static_image_mode= False,
            max_num_hands=1,
            min_detection_confidence=self.min_detection_confidence,
            min_tracking_confidence=self.min_tracking_confidence,
        )

        self.keypoint_classifier = KeyPointClassifier()
        self.action_list = ["stop", "forward", "backward", "go left", "go right", "spin right", "spin left", "forward faster", "do nothing", "change mode", "change light"]
        self.keypoint_classifier_labels = ["upward fist", "normal fist", "reverse fist", "palm", "reverse palm", "thumb left", "thumb right", "OK", "index up"]

    def main(self):
        _, image = self.cap.read()
        image = cv.flip(image, 1) 
        debug_image = copy.deepcopy(image)

        ##############################################################
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

        image.flags.writeable = False
        results = self.hands.process(image)
        image.flags.writeable = True

        ####################################################################
        if results.multi_hand_landmarks is not None:
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
                hand_sign_id = self.keypoint_classifier(pre_processed_landmark_list)
                cv.putText(debug_image, "Detected shape: " + self.keypoint_classifier_labels[hand_sign_id], 
                (10,30), 
                cv.FONT_HERSHEY_DUPLEX, 
                0.5, (0, 0, 0), 1, cv.LINE_AA)
                self.previous_action_id = self.current_action_id
                self.current_action_id = self.getActionAndMode(hand_sign_id, hand_landmarks.landmark[0].x)

                ## Draw result
                debug_image = draw_bounding_rect(self.use_brect, debug_image, brect)
                debug_image = draw_landmarks(debug_image, landmark_list)
                debug_image = draw_label(
                    debug_image,
                    brect,
                    handedness,
                    self.action_list[self.current_action_id],
                    #keypoint_classifier_labels[hand_sign_id],
                    self.auto_mode
                )
        else:
            self.current_action_id = 8 # do nothing
            cv.putText(debug_image, "Detected shape: None", 
                (10,30), 
                cv.FONT_HERSHEY_DUPLEX, 
                0.5, (0, 0, 0), 1, cv.LINE_AA)

        current_mode = "Auto" if self.auto_mode else "Manual"
        current_light = "On" if self.light_mode else "Off"
        cv.putText(debug_image, "Current Mode: " + current_mode, (10,60), cv.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0), 1, cv.LINE_AA)
        cv.putText(debug_image, "Car Light: " + current_light, (10,90), cv.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0), 1, cv.LINE_AA)

        # SEND TO PI ThE self.CURRENT_ACTION_ID
        #if not self.auto_mode:



        ##########################################################################
        return debug_image

    def getActionAndMode(self, hand_sign_id, hand_place):
        if hand_sign_id == 0 or hand_sign_id == 1: # UPWARD FIST OR NORMAL FIST
            if hand_place < 0.33: # LEFT SCREEN FIST
                return 6 # spin left
            elif hand_place > 0.66: # RIGHT SCREEN FIST
                return 5 # spin right
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
            return 3 # go left
        elif hand_sign_id == 6: # THUMB RIGHT
            return 4 # go right
        elif hand_sign_id == 7: # OK
            if (self.previous_action_id != 9): # if change mode first time
                self.auto_mode = not self.auto_mode
            return 9 # change mode
        elif hand_sign_id == 8: # INDEX UP
            if (self.previous_action_id != 10): # if change light first time
                self.light_mode = not self.light_mode
            return 10 # change light

if __name__ == "__main__":
    Hand_Object = HandGesture()
    while True:
        key = cv.waitKey(1)
        if key == 27:
            break
        image = Hand_Object.main()
        #cv.imwrite('F:\\Hung Luu\\BK_19_22\\3_Junior\\212\\DMC\\App Design\\Self-drviving-Car_App\\images\\hand_gesture_images\\cache.jpeg',
                    #image)
        cv.imshow('Hand Gesture Recognition', image)

    Hand_Object.cap.release()
    cv.destroyAllWindows()
