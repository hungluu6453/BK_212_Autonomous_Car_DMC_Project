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

class AppFunction():
    connection = None
    data = b""
    payload_size = struct.calcsize(">L")

    hg_thread = False
    sd_thread = False

    hg_size = [320,240]
    sd_main_size = [320,240]
    sd_sub_size = [320,240]

    def __init__(self):
        if AppFunction.connection is None:
            AppFunction.connection = AppFunction.connect(15, 25)
            

    def connect(PORT_send,PORT_receive):
        socket_send = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket_send.bind(("",PORT_send))

        socket_receive = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket_receive.bind(("",PORT_receive))

        print("waiting")

        socket_send.listen(10)
        conn_send,addr_send = socket_send.accept()

        print("send accepted")

        socket_receive.listen(10)
        conn_receive,addr_receive = socket_receive.accept()

        print("receive accepted")

        return conn_send,conn_receive

    def receive_image():
        while len(AppFunction.data) < AppFunction.payload_size:
            AppFunction.data += AppFunction.connection[1].recv(4096)
        packed_msg_size = AppFunction.data[:AppFunction.payload_size]
        AppFunction.data = AppFunction.data[AppFunction.payload_size:]
        msg_size = struct.unpack(">L", packed_msg_size)[0]
        while len(AppFunction.data) < msg_size:
            AppFunction.data += AppFunction.connection[1].recv(4096)
        frame_data = AppFunction.data[:msg_size]
        AppFunction.data = AppFunction.data[msg_size:]
        frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        #print("received")
        return frame

    def send_signal(signal):
        AppFunction.connection[0].send(str.encode(str(signal)+'.'))
        #print("sent")

    def convertToQImage(frame, width, height):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)


        Pic = image.scaled(width, height, Qt.KeepAspectRatio)

        return Pic

class HandGesture_Thread(AppFunction, QThread):
    Hand_Object = hg.HandGesture()

    ImageUpdate = Signal(QImage)
    TextUpdate = Signal(str)
    CamUpdate = Signal(QImage)

    def __init__(self):
        super(AppFunction, self).__init__()
        super().__init__()

    def run(self):
        self.ThreadActive = True

        while True:
            hg_image, hg_signal, hg_string  = self.Hand_Object.main()

            # cv2.imshow("", hg_image)
            # cv2.waitKey(1)

            if AppFunction.hg_thread:
                AppFunction.send_signal(hg_signal)

                cam_screen = AppFunction.receive_image()

                self.ImageUpdate.emit(AppFunction.convertToQImage(hg_image, AppFunction.hg_size[0], AppFunction.hg_size[1]))
                self.TextUpdate.emit(hg_string)
                self.CamUpdate.emit(AppFunction.convertToQImage(cam_screen, AppFunction.hg_size[0], AppFunction.hg_size[1]))

    def stop(self):
        self.Hand_Object.cap.release()
        self.quit()

class SelfDriving_Thread(AppFunction, QThread):
    ObjectDetection = od.ObjectDetection()

    LaneFollowing = lf.LaneFollowing()

    od_ImageUpdate = Signal(QImage)
    lf_ImageUpdate = Signal(QImage)
    sd_text = Signal(str)

    last_od_signal = "stop"

    def __init__(self):
        super(AppFunction, self).__init__()
        super().__init__()

    def run(self):
        self.ThreadActive = True
        signal = 0

        while True:
            if AppFunction.sd_thread:
                AppFunction.send_signal(signal)

                frame = AppFunction.receive_image()

                od_image, od_signal = self.ObjectDetection.run(frame)
                lf_image, lf_signal = self.LaneFollowing.run(frame)

                if od_signal != "none":
                    self.last_od_signal = od_signal

                print(lf_signal)
                text, signal = SelfDriving_Thread.makeDecision(self.last_od_signal, lf_signal)
                print(signal)

                self.od_ImageUpdate.emit(AppFunction.convertToQImage(od_image, AppFunction.sd_main_size[0], AppFunction.sd_main_size[1]))
                self.lf_ImageUpdate.emit(AppFunction.convertToQImage(lf_image, AppFunction.sd_sub_size[0], AppFunction.sd_sub_size[1]))
                self.sd_text.emit(text)

    def stop(self):
        self.quit()

    def makeDecision(od_signal, lf_signal):
        if od_signal == "stop":
            return "Stop", 8
        elif lf_signal == "forward":
            if od_signal == "fast":
                return "Fast speed", 7
            elif od_signal == "slow":
                return "Slow speed", 1
        elif lf_signal == "left":
            return "Turning left", 5
        elif lf_signal == "right":
            return "Turning right", 6
        elif lf_signal == "left-90":
            return "Moving left", 4
        elif lf_signal == "right-90":
            return "Moving right", 3
    