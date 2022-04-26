import cv2 as cv
import numpy as np
vid = cv.VideoCapture(0)
# print(dir(vid))
lowerWhite = np.array([80,0,0])
upperWhite = np.array([255,160,255])

while True:
	ret, frame = vid.read()
	cv.imshow('sdf', frame)
	cv.inRange(frame,lowerWhite,upperWhite)
	if cv.waitKey(1) & 0xFF == ord('q'):
		break

# print(help(cv.createTrackbar))
# print(help(cv.getTrackbarPos))