import sys
import os
import platform
import time

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *


import cv2

import code.HandGesture.HandGesture as hg
import code.ObjectDetection.yolov5.ObjectDetection as od
import code.LaneFollowing.LaneFollowing as lf

os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)

		self.hg_thread = True
		self.sd_thread = True

		self.initThread()

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		global widgets
		widgets = self.ui

		Settings.ENABLE_CUSTOM_TITLE_BAR = True

		self.setWindowTitle("Genesis control panel")

		UIFunctions.uiDefinitions(self)

		widgets.stackedWidget.setCurrentWidget(widgets.home)

		#UIFunctions.maximize_restore(self)

		widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

		self.connectButton()

		self.show()
	 
	def initThread(self):
		if self.hg_thread:
			self.HandGesture_Thread = HandGesture_Thread()
		if self.sd_thread:
			self.ObjectDetection_Thread = SelfDriving_Thread()

	def connectButton(self):
		widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

		widgets.btn_home.clicked.connect(self.buttonClick)
		widgets.btn_self_driving.clicked.connect(self.buttonClick)
		widgets.btn_hand_gesture.clicked.connect(self.buttonClick)
		widgets.btn_document.clicked.connect(self.buttonClick)
		widgets.closeAppBtn.clicked.connect(self.buttonClick)

		if self.hg_thread:
			self.HandGesture_Thread.ImageUpdate.connect(self.ImageUpdate_hg_screen)
			self.HandGesture_Thread.TextUpdate.connect(self.TextUpdate_hg_screen)
			self.HandGesture_Thread.CamUpdate.connect(self.CamUpdate_hg_screen)
		if self.sd_thread:
			self.ObjectDetection_Thread.od_ImageUpdate.connect(self.ImageUpdate_od_screen)
			self.ObjectDetection_Thread.lf_ImageUpdate.connect(self.ImageUpdate_lf_screen)
			self.ObjectDetection_Thread.sd_text.connect(self.ImageUpdate_sd_text)

	def buttonClick(self):
		btn = self.sender()
		btnName = btn.objectName()

		if btnName == "btn_home":
			widgets.stackedWidget.setCurrentWidget(widgets.home)
			UIFunctions.resetStyle(self, btnName)
			btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

		if btnName == "btn_self_driving":
			widgets.stackedWidget.setCurrentWidget(widgets.selfdriving)
			UIFunctions.resetStyle(self, btnName)
			btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
			if self.sd_thread:
				self.ObjectDetection_Thread.start()
				if AppFunction.hg_thread:
					AppFunction.hg_thread = False
				AppFunction.sd_thread = True

		if btnName == "btn_hand_gesture":
			widgets.stackedWidget.setCurrentWidget(widgets.handgesture) # SET PAGE
			UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
			btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

			if self.hg_thread:
				self.HandGesture_Thread.start()
				if AppFunction.sd_thread:
					AppFunction.sd_thread = False
				AppFunction.hg_thread = True

		if btnName == "btn_document":
			#widgets.stackedWidget.setCurrentWidget(widgets.tutorial) # SET PAGE
			#UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
			#btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
			pass

		if btnName == "closeAppBtn":
			if self.sd_thread or self.hg_thread:
				if AppFunction.hg_thread:
					self.HandGesture_Thread.stop()
				if AppFunction.sd_thread:
					self.ObjectDetection_Thread.stop()
					
				while True:
					if self.HandGesture_Thread.isFinished() and self.ObjectDetection_Thread.isFinished():
						self.close()
					print("waiting to shutdown")
					#time.sleep(0.1)
			else:
				self.close()

			

	def mousePressEvent(self, event):
		# SET DRAG POS WINDOW
		self.dragPos = event.globalPos()

	def ImageUpdate_hg_screen(self, Image):
		widgets.screen_cam.setPixmap(QPixmap.fromImage(Image))

	def ImageUpdate_od_screen(self, Image):
		widgets.sd_main_screen.setPixmap(QPixmap.fromImage(Image))

	def ImageUpdate_lf_screen(self, Image):
		widgets.sd_subscreen1.setPixmap(QPixmap.fromImage(Image))


	def TextUpdate_hg_screen(self, text):
		widgets.hg_message.setText(text)

	def CamUpdate_hg_screen(self, Image):
		widgets.car_cam.setPixmap(QPixmap.fromImage(Image))

	def ImageUpdate_sd_text(self, text):
		widgets.sd_message.setText(text)

	def SwitchMode(self):
		widgets.bgApp.setStyleSheet(u"background-color: #ECEFF4;")
		widgets.leftMenuBg.setStyleSheet(u"background-color: #c0c6d1;")
		widgets.contentTopBg.setStyleSheet(u"background-color: #c0c6d1;")
		widgets.topLogo.setStyleSheet(u"background-color: #c0c6d1;")
		widgets.label.setStyleSheet(u"background-color: #c0c6d1; color: #2E3440;")
		widgets.howtouse.setStyleSheet(u"background-color: #c0c6d1; color: #2E3440;")
		widgets.teammember.setStyleSheet(u"background-color: #c0c6d1; color: #2E3440;")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	app.setWindowIcon(QIcon("icon.ico"))
	window = MainWindow()
	sys.exit(app.exec())

