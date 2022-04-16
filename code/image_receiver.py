# Import the required modules
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

class Receiver:
    def __init__(self, HOST, PORT_send, PORT_receive,):
        self.HOST = HOST
        self.PORT_send = PORT_send
        self.PORT_receive = PORT_receive
        
        self.socket_send = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket_send.bind((self.HOST,self.PORT_send))

        self.socket_receive = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket_receive.bind((self.HOST,self.PORT_receive  ))

        self.socket_send.listen(10)
        self.conn_send,self.addr_send = self.socket_send.accept()

        print("send accepted")

        self.socket_receive.listen(10)
        self.conn_receive,self.addr_receive = self.socket_receive.accept()

        print("receive accepted")

        self.data = b""
        self.payload_size = struct.calcsize(">L")

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

    def send_signal(self, signal):
        self.conn_send.send(str.encode(str(signal)+'.'))
        print("sent")
        
if __name__ == "__main__":
    object = Receiver("",10)
    while True:
        cv2.imshow("",object.receive_image())
        cv2.waitKey(1)

"""HOST=''
PORT=10

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')

conn,addr=s.accept()

data = b""
payload_size = struct.calcsize(">L")
print("payload_size: {}".format(payload_size))
while True:
    while len(data) < payload_size:
        data += conn.recv(4096)
    # receive image row data form client socket
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack(">L", packed_msg_size)[0]
    while len(data) < msg_size:
        data += conn.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    # unpack image using pickle 
    frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

    cv2.imshow('server',frame)
    cv2.waitKey(1)  """