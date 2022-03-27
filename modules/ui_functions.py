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

# MAIN FILE
# ///////////////////////////////////////////////////////////////
from main import *

# GLOBALS
# ///////////////////////////////////////////////////////////////
GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True

class UIFunctions(MainWindow):
    # MAXIMIZE/RESTORE
    # ///////////////////////////////////////////////////////////////
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == False:
            GLOBAL_STATE = True
            UIFunctions.maximize_restore_screen(self)
            self.showMaximized()
            self.ui.gridLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeRestoreAppBtn.setToolTip("Restore")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
            self.ui.frame_size_grip.hide()
            
            #self.left_grip.hide()
            #self.right_grip.hide()
            #self.top_grip.hide()
            #self.bottom_grip.hide()
        else:
            GLOBAL_STATE = False
            UIFunctions.maximize_restore_screen(self)
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.gridLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
            self.ui.frame_size_grip.show()
            #self.left_grip.show()
            #self.right_grip.show()
            #self.top_grip.show()
            #self.bottom_grip.show()

    def maximize_restore_screen(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == True:
            self.ui.car_cam.setMinimumSize(QSize(640, 480))
            self.ui.car_cam.setMaximumSize(QSize(640, 480))
            self.ui.screen_cam.setMinimumSize(QSize(640, 480))
            self.ui.screen_cam.setMaximumSize(QSize(640, 480))
            self.ui.hg_layout.setVerticalSpacing(70)

            self.ui.sd_main_screen.setMinimumSize(QSize(640, 480))
            self.ui.sd_main_screen.setMaximumSize(QSize(640, 480))
            self.ui.sd_subscreen1.setMinimumSize(QSize(360, 270))
            self.ui.sd_subscreen1.setMaximumSize(QSize(360, 270))
            self.ui.sd_subscreen2.setMinimumSize(QSize(360, 270))
            self.ui.sd_subscreen2.setMaximumSize(QSize(360, 270))
            self.ui.sd_message.setMinimumSize(QSize(640, 120))
            self.ui.sd_message.setMaximumSize(QSize(640, 120))
            self.ui.verticalLayout_sd2.setSpacing(70)
            self.ui.verticalLayout_sd2.setContentsMargins(-1, -1, 400, -1)
            self.ui.verticalLayout_sd1.setContentsMargins(300, -1, -1, -1)
        else:
            self.ui.car_cam.setMinimumSize(QSize(320, 240))
            self.ui.car_cam.setMaximumSize(QSize(320, 240))
            self.ui.screen_cam.setMinimumSize(QSize(320, 240))
            self.ui.screen_cam.setMaximumSize(QSize(320, 240))
            self.ui.hg_layout.setVerticalSpacing(30)

            self.ui.sd_main_screen.setMinimumSize(QSize(320, 240))
            self.ui.sd_main_screen.setMaximumSize(QSize(320, 240))
            self.ui.sd_subscreen1.setMinimumSize(QSize(240, 180))
            self.ui.sd_subscreen1.setMaximumSize(QSize(240, 180))
            self.ui.sd_subscreen2.setMinimumSize(QSize(240, 180))
            self.ui.sd_subscreen2.setMaximumSize(QSize(240, 180))
            self.ui.sd_message.setMinimumSize(QSize(320, 120))
            self.ui.sd_message.setMaximumSize(QSize(320, 120))
            self.ui.verticalLayout_sd2.setSpacing(10)
            self.ui.verticalLayout_sd2.setContentsMargins(-1, -1, 110, -1)
            self.ui.verticalLayout_sd1.setContentsMargins(80, -1, -1, -1)

    # RETURN STATUS
    # ///////////////////////////////////////////////////////////////
    def returStatus(self):
        return GLOBAL_STATE

    # SET STATUS
    # ///////////////////////////////////////////////////////////////
    def setStatus(self, status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    # TOGGLE MENU
    # ///////////////////////////////////////////////////////////////
    def toggleMenu(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.leftMenuBg.width()
            maxExtend = Settings.MENU_WIDTH
            standard = 60

            # SET MAX WIDTH
            if width == 60:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    def start_box_animation(self, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0 

        # Check values
        if left_box_width == 0 and direction == "left":
            left_width = 240
        else:
            left_width = 0
        # Check values
        if right_box_width == 0 and direction == "right":
            right_width = 240
        else:
            right_width = 0       

        # ANIMATION LEFT BOX        
        self.left_box = QPropertyAnimation(self.ui.extraLeftBox, b"minimumWidth")
        self.left_box.setDuration(Settings.TIME_ANIMATION)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX        
        self.right_box = QPropertyAnimation(self.ui.extraRightBox, b"minimumWidth")
        self.right_box.setDuration(Settings.TIME_ANIMATION)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()

    # SELECT/DESELECT MENU
    # ///////////////////////////////////////////////////////////////
    # SELECT
    def selectMenu(getStyle):
        select = getStyle + Settings.MENU_SELECTED_STYLESHEET
        return select

    # DESELECT
    def deselectMenu(getStyle):
        deselect = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET, "")
        return deselect

    # START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    # RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    # IMPORT THEMES FILES QSS/CSS
    # ///////////////////////////////////////////////////////////////
    def theme(self, file, useCustomTheme):
        if useCustomTheme:
            str = open(file, 'r').read()
            self.ui.styleSheet.setStyleSheet(str)

    # START - GUI DEFINITIONS
    # ///////////////////////////////////////////////////////////////
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))
        self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore

        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            #STANDARD TITLE BAR
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            # MOVE WINDOW / MAXIMIZE / RESTORE
            def moveWindow(event):
                # IF MAXIMIZED CHANGE TO NORMAL
                if UIFunctions.returStatus(self):
                    UIFunctions.maximize_restore(self)
                # MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()

            self.ui.titleRightInfo.mouseMoveEvent = moveWindow

            # CUSTOM GRIPS
            #self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
            #self.right_grip = CustomGrip(self, Qt.RightEdge, True)
            #self.top_grip = CustomGrip(self, Qt.TopEdge, True)
            #self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

        else:
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.minimizeAppBtn.hide()
            self.ui.maximizeRestoreAppBtn.hide()
            self.ui.closeAppBtn.hide()
            self.ui.frame_size_grip.hide()

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

        # RESIZE WINDOW
        #self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        #self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # MINIMIZE
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # CLOSE APPLICATION
        #self.ui.closeAppBtn.clicked.connect(lambda: self.close())

    #def resize_grips(self):
        #if Settings.ENABLE_CUSTOM_TITLE_BAR:
            #self.left_grip.setGeometry(0, 10, 10, self.height())
            #self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
            #self.top_grip.setGeometry(0, 0, self.width(), 10)
            #self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    # ///////////////////////////////////////////////////////////////
    # END - GUI DEFINITIONS
