import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
from math import atan2
import math

path = './Capture.PNG'
window_name = 'HSV'

image = cv2.imread(path)

def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE Max", "HSV", 160, 255, empty)


while True:
    imgHsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")
    
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask) 
    # mask = 1 (in range)=> giu nguyen gia tri
    # 

    # Histogram
    upper_area = int(mask.shape[0]/3*2)
    lower_area = int(mask.shape[0]/9*7)
    reduce_mask = mask[upper_area:lower_area,:]/255
    bar = np.sum(reduce_mask, axis=0)
    bar = np.cumsum(bar)
    pct_50 = bar[-1]/2
    w_pointx = np.sum([x < pct_50 for x in bar])
    w_pointy = (lower_area+upper_area)/2
    H = mask.shape[0]
    W = mask.shape[1]
    # print(ind_50)
    print(atan2(H - w_pointy, w_pointx - W/2)/math.pi*180)

    plt.bar(list(range(0,bar.shape[0])),bar)
    # plt.xlabel(range(160, 20))
    plt.show(block=False)
    plt.pause(3)
    plt.close()

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([image, mask, result])
    cv2.imshow('Reduced mask', reduce_mask)
    cv2.imshow('Horizontal Stacking', hStack)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

cv2.destroyAllWindows()