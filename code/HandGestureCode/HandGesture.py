#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import csv
import copy
#import argparse
#import itertools
from collections import Counter
from collections import deque

import cv2 as cv
import numpy as np
import mediapipe as mp

if __package__ is None or __package__ == '':
    # uses current directory visibility
    from helper import *
else:
    # uses current package visibility
    from .helper import *

#from utils import CvFpsCalc
#from model import KeyPointClassifier
#from model import PointHistoryClassifier



class HandGesture():

    def __init__(self):

        # 320*180 320*240 640*360 640*480 

        self.cam_width = 320

        self.cam_height = 240

        self.min_detection_confidence  = 0.5
        self.min_tracking_confidence = 0.5

        self.auto_mode = "Manual"
        self.previous_action_id = -1
        self.current_action_id = -1
        self.mpDraw = mp.solutions.drawing_utils


        self.cap_device = 0
        self.cap_width = self.cam_width
        self.cap_height = self.cam_height

        self.use_static_image_mode = False
        self.use_brect = True

        self.cap = cv.VideoCapture(self.cap_device)

        self.cap.set(cv.CAP_PROP_FRAME_WIDTH, self.cap_width)
        self.cap.set(cv.CAP_PROP_FRAME_HEIGHT, self.cap_height)

        #width = self.cap.get(cv.CAP_PROP_FRAME_WIDTH)
        #height = self.cap.get(cv.CAP_PROP_FRAME_HEIGHT)
        
        #resolution=str(width)+"x"+str(height)

        #print(resolution)

        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            static_image_mode=self.use_static_image_mode,
            max_num_hands=1,
            min_detection_confidence=self.min_detection_confidence,
            min_tracking_confidence=self.min_tracking_confidence,
        )

        self.point_history_classifier = PointHistoryClassifier()
        self.keypoint_classifier = KeyPointClassifier()

        self.action_list = ["stop", "forward", "backward", "turn left", "turn right", "go left", "go right", "backward left", "backward right", "change mode"]
        self.keypoint_classifier_labels = ["fist", "reverse fist", "palm", "thumb_left", "thumb_right", "OK", "draw"]
        self.point_history_classifier_labels = ["swipe_left", "swipe_right", "swipe_up", "swipe_down", "no_motion"]
        self.finger_action_list = ["auto go left", "auto go right", "turn on light", "turn off light", "no action"]

        self.history_length = 16
        self.point_history = deque(maxlen=self.history_length)

        self.finger_gesture_history = deque(maxlen=self.history_length)

        self.mode = 0

    def getActionAndMode(self,hand_sign_id, hand_place):
        if hand_sign_id == 0:
            if hand_place < 0.33:
                return 3
            elif hand_place > 0.66:
                return 4
            else:
                return 1
        elif hand_sign_id == 1:
            if hand_place < 0.33:
                return 7
            elif hand_place > 0.66:
                return 8
            else:
                return 2
        elif hand_sign_id == 2:
            return 0
        elif hand_sign_id == 3:
            return 5
        elif hand_sign_id == 4:
            return 6
        else:
            if self.auto_mode == "Manual" and self.previous_action_id != 9:
                self.auto_mode = "Auto"
            elif self.auto_mode == "Auto" and self.previous_action_id != 9:
                self.auto_mode = "Manual"
            return 9

    def draw_info(self,image, mode, number = 0):
        #cv.putText(image, "FPS:" + str(fps), (10, 30), cv.FONT_HERSHEY_SIMPLEX,
                   #1.0, (0, 0, 0), 4, cv.LINE_AA)
        #cv.putText(image, "FPS:" + str(fps), (10, 30), cv.FONT_HERSHEY_SIMPLEX,
                   #1.0, (255, 255, 255), 2, cv.LINE_AA)

        mode_string = ['Logging Key Point', 'Logging Point History']
        if 1 <= self.mode <= 2:
            cv.putText(image, "MODE:" + mode_string[mode - 1], (10, 90),
                       cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1,
                       cv.LINE_AA)
            if 0 <= number <= 9:
                cv.putText(image, "NUM:" + str(number), (10, 110),
                           cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1,
                           cv.LINE_AA)
        return image

    def main(self):

        # キー処理(ESC：終了) #################################################
        

        #number, mode = select_mode(key, mode)

        # カメラキャプチャ #####################################################
        ret, image = self.cap.read()
        #if not ret:
            #break
        image = cv.flip(image, 1)  # ミラー表示
        debug_image = copy.deepcopy(image)

        # 検出実施 #############################################################
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

        image.flags.writeable = False
        results = self.hands.process(image)
        image.flags.writeable = True

        #  ####################################################################
        if results.multi_hand_landmarks is not None:
            for hand_landmarks, handedness in zip(results.multi_hand_landmarks,
                                                  results.multi_handedness):
                # 外接矩形の計算
                brect = calc_bounding_rect(debug_image, hand_landmarks)
                # ランドマークの計算
                landmark_list = calc_landmark_list(debug_image, hand_landmarks)

                # 相対座標・正規化座標への変換
                pre_processed_landmark_list = pre_process_landmark(
                    landmark_list)
                pre_processed_point_history_list = pre_process_point_history(
                    debug_image, self.point_history)
                # 学習データ保存
                #logging_csv(number, mode, pre_processed_landmark_list,
                            #pre_processed_point_history_list)

                # ハンドサイン分類
                hand_sign_id = self.keypoint_classifier(pre_processed_landmark_list)
                if hand_sign_id == 6:  # 指差しサイン
                    self.point_history.append(landmark_list[8])  # 人差指座標
                else:
                    self.point_history.append([0, 0])

                # フィンガージェスチャー分類
                finger_gesture_id = -1
                point_history_len = len(pre_processed_point_history_list)
                if point_history_len == (self.history_length * 2):
                    finger_gesture_id = self.point_history_classifier(
                        pre_processed_point_history_list)

                # 直近検出の中で最多のジェスチャーIDを算出
                self.finger_gesture_history.append(finger_gesture_id)
                most_common_fg_id = Counter(
                    self.finger_gesture_history).most_common()

                # 描画
                if (hand_sign_id != 6):
                    self.previous_action_id = self.current_action_id
                    self.current_action_id = self.getActionAndMode(hand_sign_id, hand_landmarks.landmark[0].x)
                    current_finger_action = "None"
                else: 
                    current_finger_action = self.finger_action_list[most_common_fg_id[0][0]]

                ##
                debug_image = draw_bounding_rect(self.use_brect, debug_image, brect)
                debug_image = draw_landmarks(debug_image, landmark_list)
                debug_image = draw_info_text(
                    debug_image,
                    brect,
                    handedness,
                    #keypoint_classifier_labels[hand_sign_id],
                    self.action_list[self.current_action_id],
                    #point_history_classifier_labels[most_common_fg_id[0][0]],
                    current_finger_action,
                    self.auto_mode
                )
        else:
            self.point_history.append([0, 0])

        debug_image = draw_point_history(debug_image, self.point_history)
        #debug_image = draw_info(debug_image, mode, number)
        debug_image = self.draw_info(debug_image, self.mode)

        # 画面反映 #############################################################
        # cv.imshow('Hand Gesture Recognition', debug_image)
        return debug_image

if __name__ == "__main__":
        Hand_Object = HandGesture()
        while True:
            key = cv.waitKey(10)
            if key == 27:  # ESC
                break
            image = Hand_Object.main()
            cv.imwrite('F:\\Hung Luu\\BK_19_22\\3_Junior\\212\\DMC\\App Design\\Self-drviving-Car_App\\images\\hand_gesture_images\\cache.jpeg',
                       image)
            cv.imshow('Hand Gesture Recognition', image)

        Hand_Object.cap.release()
        cv.destroyAllWindows()