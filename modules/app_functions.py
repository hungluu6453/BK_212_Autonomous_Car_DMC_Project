# MAIN FILE
# ///////////////////////////////////////////////////////////////
from main import *
from IPython.display import clear_output
import socket
import sys
import cv2
import matplotlib.pyplot as plt
import pickle
import numpy as np
import struct ## new
import zlib
from PIL import Image, ImageOps

def convertToQImage(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)

    #Pic = image.scaled(320, 240, Qt.KeepAspectRatio)
    Pic = image.scaled(640, 480, Qt.KeepAspectRatio)

    return Pic

class HandGesture_Thread(QThread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection

    Hand_Object = hg.HandGesture()

    ImageUpdate = Signal(QImage)
    TextUpdate = Signal(str)
    CamUpdate = Signal(QImage)

    ThreadActive = False
    ReadytoClose = False

    def run(self):
        self.ThreadActive = True

        """self.socket_send = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                                self.socket_send.bind(("",10))
                        
                                self.socket_receive = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                                self.socket_receive.bind(("",20))
                        
                                self.socket_send.listen(10)
                                self.conn_send,self.addr_send = self.socket_send.accept()
                        
                                print("send accepted")
                        
                                
                                self.socket_receive.listen(10)
                                self.conn_receive,self.addr_receive = self.socket_receive.accept()
                        
                                print("receive accepted")
                        
                                self.data = b""
                                self.payload_size = struct.calcsize(">L")"""
        
        while True:
            hg_image, hg_signal, hg_string  = self.Hand_Object.main()

            self.connection.send_signal(hg_signal)

            cam_screen = self.connection.receive_image()

            self.ImageUpdate.emit(convertToQImage(hg_image))
            self.TextUpdate.emit(hg_string)
            self.CamUpdate.emit(convertToQImage(cam_screen))

        
            #cv2.imshow("",cam_screen)
            #cv2.waitKey(1)

            if self.ThreadActive == False:
                self.Hand_Object.cap.release()
                break

        self.quit()

        self.ReadytoClose = True
    
    def stop(self):
        self.ThreadActive = False

    def receive_image(self):
        while len(self.data) < self.payload_size:
            self.data += self.conn_receive.recv(4096)
        packed_msg_size = self.data[:self.payload_size]
        self.data = self.data[self.payload_size:]
        msg_size = struct.unpack(">L", packed_msg_size)[0]
        while len(self.data) < msg_size:
            self.data += self.conn_receive.recv(4096)
        frame_data = self.data[:msg_size]
        self.data = self.data[msg_size:]
        frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        print("received")
        return frame

class SelfDriving_Thread(QThread):
    #def __init__(self, connection):
        #self.connection = connection

    #ObjectDetection = od.ObjectDetection()

    #LaneFollowing = lf.LaneFollowing()

    od_ImageUpdate = Signal(QImage)
    #lf_ImageUpdate = Signal(QImage)

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

    ThreadActive = False
    ReadytoClose = False

    def run(self):
        self.ThreadActive = True
        
        while True:
            #frame = self.connection.receive_image()

            _,frame = SelfDriving_Thread.cap.read()

            od_image, od_signal = self.ObjectDetection.run(frame)
            #lf_image, lf_signal = LaneFollowing.run(frame)

            #cv2.imshow('Hand Gesture Recognition', frame)

            self.od_ImageUpdate.emit(convertToQImage(od_image))
            #self.lf_ImageUpdate.emit(convertToQImage(lf_image))

            if self.ThreadActive == False:
                SelfDriving_Thread.cap.release()
                break

        self.quit()

        self.ReadytoClose = True
    
    def stop(self):
        self.ThreadActive = False

    