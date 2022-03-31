# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform
import time

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *

import cv2

import code.HandGestureCode_v2.HandGesture as hg
import code.ObjectDetection.ObjectDetection as od

os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.HandGesture_Thread = HandGesture_Thread()
        self.HandGesture_Thread.ImageUpdate.connect(self.ImageUpdate_hg_screen)

        self.ObjectDetection_Thread = ObjectDetection_Thread()
        self.ObjectDetection_Thread.ImageUpdate.connect(self.ImageUpdate_od_screen)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "ABC - Autonomous Car Control App"
        description = "PyDracula APP - Theme with colors based on Dracula for Python."
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # SET HOME PAGE AND 
        # ///////////////////////////////////////////////////////////////

        widgets.stackedWidget.setCurrentWidget(widgets.home)

        # Default full screen
        # ///////////////////////////////////////////////////////////////

        #UIFunctions.maximize_restore(self)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)
        widgets.closeAppBtn.clicked.connect(self.buttonClick)

        # SELECT MENU
        # ///////////////////////////////////////////////////////////////

        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()
        


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.selfdriving)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.ObjectDetection_Thread.start()

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.handgesture) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
            self.HandGesture_Thread.start()

        if btnName == "btn_save":
            print("Save BTN clicked!")

        if btnName == "closeAppBtn":

            if self.HandGesture_Thread.ThreadActive:
                self.HandGesture_Thread.stop()
            if self.ObjectDetection_Thread.ThreadActive:
                self.ObjectDetection_Thread.stop()
                
            while not self.HandGesture_Thread.ReadytoClose and not self.ObjectDetection_Thread.ReadytoClose:
                time.sleep(0.1)               


            self.close()


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    #def resizeEvent(self, event):
        # Update Size Grips
       # UIFunctions.resize_grips(self)

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

    def ImageUpdate_hg_screen(self, Image):
        widgets.screen_cam.setPixmap(QPixmap.fromImage(Image))

    def ImageUpdate_od_screen(self, Image):
        widgets.sd_main_screen.setPixmap(QPixmap.fromImage(Image))

class HandGesture_Thread(QThread):

    Hand_Object = hg.HandGesture(connect_status = True, LAN = True)

    ImageUpdate = Signal(QImage)

    ThreadActive = False

    ReadytoClose = False

    def run(self):
        self.ThreadActive = True
        
        while True:
            frame = self.Hand_Object.main()

            #cv2.imshow('Hand Gesture Recognition', frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)

            Pic = image.scaled(320, 240, Qt.KeepAspectRatio)

            self.ImageUpdate.emit(Pic)

            if self.ThreadActive == False:
                self.Hand_Object.cap.release()
                break

        self.quit()

        self.ReadytoClose = True
    
    def stop(self):
        self.ThreadActive = False

class ObjectDetection_Thread(QThread):

    ObjectDetection = od.ObjectDetection()

    ImageUpdate = Signal(QImage)

    ThreadActive = False

    ReadytoClose = False

    def run(self):
        self.ThreadActive = True
        
        while True:
            frame = self.ObjectDetection.main()

            #cv2.imshow('Hand Gesture Recognition', frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)

            Pic = image.scaled(320, 240, Qt.KeepAspectRatio)

            self.ImageUpdate.emit(Pic)

            if self.ThreadActive == False:
                self.ObjectDetection.cap.release()
                break

        self.quit()

        self.ReadytoClose = True
    
    def stop(self):
        self.ThreadActive = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
