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
            UIFunctions.maximize(self)
            self.showMaximized()
            self.ui.gridLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeRestoreAppBtn.setToolTip("Restore")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
            self.ui.frame_size_grip.hide()

        else:
            GLOBAL_STATE = False
            UIFunctions.restore(self)
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.gridLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
            self.ui.frame_size_grip.show()

    def maximize(self):

        self.ui.leftMenuBg.setMinimumSize(QSize(240,0))

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
        self.ui.verticalLayout_sd2.setContentsMargins(-1, -1, 250, -1)
        self.ui.verticalLayout_sd1.setContentsMargins(250, -1, -1, -1)

    def restore(self):

        self.ui.leftMenuBg.setMinimumSize(QSize(0,0))

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
            screen_width = self.width()
            screen_height = self.height()

            # SET MAX WIDTH
            if width == 60:
                toggle_widthExtended = maxExtend
                screen_widthExtended = screen_width + 180
            else:
                toggle_widthExtended = standard
                screen_widthExtended = screen_width - 180

            if GLOBAL_STATE:
                screen_widthExtended = screen_width
                
            # ANIMATION
            menu_animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth", duration = 500, startValue= width, endValue=toggle_widthExtended, easingCurve=QEasingCurve.InOutQuart)
            screen_animation = QPropertyAnimation(self, b"size", duration = 500, startValue= QSize(screen_width,screen_height), endValue= QSize(screen_widthExtended,screen_height), easingCurve=QEasingCurve.InOutQuart)
            self.group = QParallelAnimationGroup()
            self.group.addAnimation(menu_animation)
            self.group.addAnimation(screen_animation)
            self.group.start(QAbstractAnimation.DeleteWhenStopped)

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

        self.ui.topLogo.setPixmap(QPixmap('images/images/hcmut_small.png'))
        self.ui.bklogo.setPixmap(QPixmap('images/images/hcmut_small.png'))

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

        # MINIMIZE
        self.ui.minimizeAppBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # MAXIMIZE/RESTORE
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # CLOSE APPLICATION
        #self.ui.closeAppBtn.clicked.connect(lambda: self.close())

    # ///////////////////////////////////////////////////////////////
    # END - GUI DEFINITIONS
