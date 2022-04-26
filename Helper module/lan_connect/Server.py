from random import randint
import sys, traceback, threading, socket, os


SERVER_PORT = 10
rtspSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
LOCAL_HOST, PORT = ("127.0.0.1", SERVER_PORT)

try:
	rtspSocket.bind((LOCAL_HOST, PORT))
	rtspSocket.listen(5)
	(clientConnected, clientAddress) = rtspSocket.accept()
	print(print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1])))
except:
	print('Can not open port')


while True:
	try:
		clientConnected.send('1.0'.encode())
	except:
		print('Cannot send data')