import os
import re
import cv2
import numpy as np
import math

PATH_IMAGE = './real_frames/'

class LaneFollowing:
	def __init__(self, W = 680, H = 480, C = 3, polygon = np.array([[0, 480], [0,400], [680,400], [680,480]]), thresh = 150, waypoint_y = 400, bottom = 40):
		self.W, self.H, self.C = W, H, C
		self.bottom = bottom
		self.polygon = polygon
		self.thresh = thresh
		self.waypoint_y = waypoint_y
		# self.initSize()

	# def drawLine(self):
	# 	pass

	# def getFrames(self):
	# 	# get file names of frames
	# 	col_frames = os.listdir(PATH_IMAGE)

	# 	# load frames
	# 	col_images=[]
	# 	for i in col_frames:
	# 			img = cv2.imread(PATH_IMAGE+i)
	# 			col_images.append(img)

	# 	self.NUM, self.H, self.W, self.C = np.array(col_images).shape
	# 	print(np.array(col_images).shape)
	# 	self.col_images = col_images

	# def run(self):
	# 	for img in self.col_images:
	# 		angle = self.getAngle(img)
	
	def run(self, img):
		dim = (self.W, self.H)
		img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
		#cv2.imshow('original', img)

		# create a zero array
		stencil = np.zeros_like(img[:,:,0])

		# fill polygon with ones
		cv2.fillConvexPoly(stencil, self.polygon, 1)

		# apply polygon as a mask on the frame
		img = cv2.bitwise_and(img[:,:,1], img[:,:,1], mask=stencil)
		#cv2.imshow('polygon', img)

		def binary_threshold(img, thresh):
			return  np.array(np.where(img <= thresh, 0, 255), dtype="uint8")

		img_inv = cv2.bitwise_not(img)
		img_inv = cv2.bitwise_and(img_inv, img_inv, mask=stencil)

		thresh2 = binary_threshold(img_inv, self.thresh)
		#print(thresh2)
		#cv2.imshow('thresh', thresh2)

		def calculateWhiteMean(arr):
			max_arr = 1
			len_arr = 1
			start = arr[0]
			cur = arr[0]
			ret = [0,0]
			for i in range(len(arr)):
				if i == 0:
					continue
				if i == len(arr)-1:
					if max_arr < len_arr:
						max_arr = len_arr
						ret[0] = start
						ret[1] = cur-1

				if arr[i] == arr[i-1] + 1:
					len_arr += 1
					cur = arr[i]
				else:
					if max_arr < len_arr:
						max_arr = len_arr
						len_arr = 1
						ret[0] = start
						ret[1] = cur-1
					start = arr[i]

			return ret[0] + int((ret[1]-ret[0])/2)

		def getBlackList(black):
			start = black[0]
			end = black[0]
			ret = list()
			length = 1
			for i in range(len(black)):
				if i == 0:
					continue

				if i == len(black)-1:
					ret.append([length,start,end])

				if black[i] == black[i-1] + 1:
					length += 1
					end = black[i]

				else:
					ret.append([length,start,end])
					length = 1
					start = black[i]

			return list(filter(lambda x: x[0] >= 25 and x[0] <= 60, ret))

		def mean_horizontal_slide(vert_point):
			arr = thresh2[vert_point]
			white = np.where(arr == 255)[0]
			black = np.where(arr == 0)[0]

			if len(white) == 0 or len(black) ==0:
				white_mean = self.W//2
				
				return white_mean, 2
			else:
				white_mean = calculateWhiteMean(white)
				black_list =  getBlackList(black)
				if len(black_list) == 1 and white[0] == 0:
					return white_mean, 0
				elif len(black_list) == 1 and white[-1] == self.W-1:
					return white_mean, 1
				else:
					return white_mean, 2
			
		# 0: 1-left
		# 1: 1- right
		# 2: 2
		top_mean, top_black= mean_horizontal_slide(self.waypoint_y)
		center_mean, center_black= mean_horizontal_slide(self.H - self.bottom)
		bot_mean, bot_black= mean_horizontal_slide(self.H-1)

		if top_black == 0 or top_black == 1:
			return thresh2, self.getActionblack(top_black)
		else:
			angle = 180 / math.pi * math.atan2(self.H-self.waypoint_y, top_mean - bot_mean) - 90

			print(angle)
			dmy = thresh2.copy()

			cv2.line(dmy,  (top_mean, self.waypoint_y),  (bot_mean, self.H - 1),  (0,0,0),  3 )

			return dmy, self.getActionWhite(angle, top_mean)

	def getActionWhite(self, angle, top_mean):
		# if top_mean<= 250:
		# 	#return 'right-out'
		# 	return "left"
		# elif top_mean >= 430:
		# 	#return 'left-out'
		# 	return "right"
		# else:

		if abs(angle) < 10:
			return 'forward'
		if angle > 0 :
			#return 'left-2'
			return "left"
		#return 'right-2'
		return "right"

	def getActionblack(self, top):
		if top == 0:
			#return 'left-1'
			return "left-90"
		else:
			#return 'right-1'
			return "right-90"

def main():
	lf = LaneFollowing()
	lf.run()

if __name__ == "__main__":
	cam = cv2.VideoCapture(1)
	cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
	cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
	lf = LaneFollowing()
	while True:
		ret, frame = cam.read()
		frame, text = lf.run(frame)
		print(text)
		cv2.imshow("", frame)
		cv2.waitKey(1)
