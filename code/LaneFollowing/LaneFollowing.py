import os
import re
import cv2
import numpy as np
import math

PATH_IMAGE = './real_frames/'

class LaneFollowing:
	def __init__(self, polygon = np.array([[0, 480], [0,380], [680,380], [680,480]]), thresh = 40, waypoint_y = 380, bottom = 50):
		self.bottom = bottom
		self.polygon = polygon
		self.thresh = thresh
		self.waypoint_y = waypoint_y
		self.getFrames()

	def drawLine(self):
		pass

	def getFrames(self):
		# get file names of frames
		col_frames = os.listdir(PATH_IMAGE)

		# load frames
		col_images=[]
		for i in col_frames:
				img = cv2.imread(PATH_IMAGE+i)
				col_images.append(img)

		self.NUM, self.H, self.W, self.C = np.array(col_images).shape
		self.col_images = col_images

	def run(self):
		for img in self.col_images:
			angle = self.getAngle(img)
	
	def getAngle(self, img):
		cv2.imshow('original', img)

		# create a zero array
		stencil = np.zeros_like(img[:,:,0])

		# fill polygon with ones
		cv2.fillConvexPoly(stencil, self.polygon, 1)

		# apply polygon as a mask on the frame
		img = cv2.bitwise_and(img[:,:,1], img[:,:,1], mask=stencil)
		cv2.imshow('polygon', img)

		def binary_threshold(img, thresh):
			return  np.array(np.where(img <= thresh, 0, 255), dtype="uint8")

		img_inv = cv2.bitwise_not(img)
		img_inv = cv2.bitwise_and(img_inv, img_inv, mask=stencil)

		thresh2 = binary_threshold(img_inv, self.thresh)
		print(thresh2)
		cv2.imshow('thresh', thresh2)

		def mean_horizontal_slide(vert_point):
			horizontal_slide = thresh2[vert_point]
			indices = np.where(horizontal_slide == 255)
			return int(np.mean(indices))
		waypoint_x = mean_horizontal_slide(self.waypoint_y)
		center_x = mean_horizontal_slide(self.H - self.bottom)

		angle = 180 / math.pi * math.atan2(self.H-self.waypoint_y, waypoint_x - center_x) - 90

		print(angle)
		dmy = thresh2.copy()
		cv2.line(dmy,  (waypoint_x, self.waypoint_y),  (center_x, self.H - 1),  (0, 255, 0),  3 )

		cv2.imshow('angle', dmy)
		cv2.waitKey(0) 
		cv2.destroyAllWindows() 
		return self.action(angle), dmy

	def action(self, angle):
		if abs(angle) < 20:
			return 'forward'
		if angle < 0 :
			return 'left'
		return 'right'

def main():
	lf = LaneFollowing()
	lf.run()

if __name__ == "__main__":
		main()
