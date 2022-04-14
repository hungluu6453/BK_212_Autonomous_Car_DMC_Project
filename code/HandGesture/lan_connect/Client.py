import socket, threading, sys, traceback, os, time

SERVER_ADDRESS = "127.0.0.1"
PORT = 10

rtspSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rtspSocket.settimeout(0.5)
try:
    rtspSocket.connect((SERVER_ADDRESS, PORT))
except:
    print('Connection Failed', 'Connection to \'%s\' failed.' %SERVER_ADDRESS)


while True:
    try:
        message = rtspSocket.recv(1024)
        print(message.decode())
    except:
        print('Cannot receive data')
print(help(rtspSocket.recv))