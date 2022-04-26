from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 630)
        MainWindow.setMinimumSize(QSize(940, 630))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 0px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 0px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 0px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.gridLayout = QGridLayout(self.styleSheet)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"background-color: #3B4252;")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setStyleSheet(u"background-color: #2E3440;")
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setStyleSheet(u"background-color: #232730;")
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Roboto Black"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        self.titleLeftDescription.setStyleSheet(u"color:#81A1C1;")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.topLogo = QLabel(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 45, 45))
        self.topLogo.setStyleSheet(u"padding-bottom: 5px;")
        self.topLogo.setPixmap(QPixmap(u":/images/images/images/hcmut_small.png"))
        self.topLogo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setMinimumSize(QSize(0, 0))
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_self_driving = QPushButton(self.topMenu)
        self.btn_self_driving.setObjectName(u"btn_self_driving")
        sizePolicy.setHeightForWidth(self.btn_self_driving.sizePolicy().hasHeightForWidth())
        self.btn_self_driving.setSizePolicy(sizePolicy)
        self.btn_self_driving.setMinimumSize(QSize(0, 45))
        self.btn_self_driving.setFont(font)
        self.btn_self_driving.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_self_driving.setLayoutDirection(Qt.LeftToRight)
        self.btn_self_driving.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-cursor-move.png);")

        self.verticalLayout_8.addWidget(self.btn_self_driving)

        self.btn_hand_gesture = QPushButton(self.topMenu)
        self.btn_hand_gesture.setObjectName(u"btn_hand_gesture")
        sizePolicy.setHeightForWidth(self.btn_hand_gesture.sizePolicy().hasHeightForWidth())
        self.btn_hand_gesture.setSizePolicy(sizePolicy)
        self.btn_hand_gesture.setMinimumSize(QSize(0, 45))
        self.btn_hand_gesture.setFont(font)
        self.btn_hand_gesture.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_hand_gesture.setLayoutDirection(Qt.LeftToRight)
        self.btn_hand_gesture.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-hand-point-right.png);")

        self.verticalLayout_8.addWidget(self.btn_hand_gesture)

        self.btn_document = QPushButton(self.topMenu)
        self.btn_document.setObjectName(u"btn_document")
        sizePolicy.setHeightForWidth(self.btn_document.sizePolicy().hasHeightForWidth())
        self.btn_document.setSizePolicy(sizePolicy)
        self.btn_document.setMinimumSize(QSize(0, 45))
        self.btn_document.setFont(font)
        self.btn_document.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_document.setLayoutDirection(Qt.LeftToRight)
        self.btn_document.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-description.png)")

        self.verticalLayout_8.addWidget(self.btn_document)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setStyleSheet(u"background-color: #232730;")
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon1)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon2)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"")
        self.verticalLayout_16 = QVBoxLayout(self.home)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(20, 20, 20, 0)
        self.bklogo = QLabel(self.home)
        self.bklogo.setObjectName(u"bklogo")
        self.bklogo.setMinimumSize(QSize(0, 60))
        self.bklogo.setMaximumSize(QSize(16777215, 50))
        self.bklogo.setAutoFillBackground(False)
        self.bklogo.setStyleSheet(u"background-color: #2E3440;\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"padding-top: 10px")
        self.bklogo.setPixmap(QPixmap(u":/images/images/images/hcmut_small.png"))
        self.bklogo.setAlignment(Qt.AlignCenter)
        self.bklogo.setMargin(0)

        self.verticalLayout_16.addWidget(self.bklogo)

        self.welcome = QLabel(self.home)
        self.welcome.setObjectName(u"welcome")
        self.welcome.setMaximumSize(QSize(16777215, 50))
        self.welcome.setStyleSheet(u"background-color: #2E3440;")
        self.welcome.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.welcome)

        self.appname = QLabel(self.home)
        self.appname.setObjectName(u"appname")
        self.appname.setMaximumSize(QSize(16777215, 60))
        self.appname.setFont(font)
        self.appname.setStyleSheet(u"background-color: #2E3440;")
        self.appname.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_16.addWidget(self.appname)

        self.appdescription = QLabel(self.home)
        self.appdescription.setObjectName(u"appdescription")
        self.appdescription.setMinimumSize(QSize(0, 0))
        self.appdescription.setStyleSheet(u"background-color: #2E3440;\n"
"padding-bottom: 15px;\n"
"")
        self.appdescription.setTextFormat(Qt.AutoText)
        self.appdescription.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.appdescription)

        self.home_layout = QHBoxLayout()
        self.home_layout.setSpacing(0)
        self.home_layout.setObjectName(u"home_layout")
        self.teammember = QLabel(self.home)
        self.teammember.setObjectName(u"teammember")
        self.teammember.setStyleSheet(u"background-color: #2E3440;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-left-radius:10px;\n"
"padding-top: 10px;\n"
"padding-bottom:20px;\n"
"\n"
"\n"
"")
        self.teammember.setLineWidth(1)

        self.home_layout.addWidget(self.teammember)

        self.howtouse = QLabel(self.home)
        self.howtouse.setObjectName(u"howtouse")
        self.howtouse.setMinimumSize(QSize(500, 0))
        self.howtouse.setStyleSheet(u"background-color: #2E3440;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:10px;\n"
"border-bottom-left-radius:0px;\n"
"padding-top: 10px;\n"
"padding-bottom:10px;\n"
"padding-left: 10px;\n"
"")

        self.home_layout.addWidget(self.howtouse)


        self.verticalLayout_16.addLayout(self.home_layout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 5, -1, -1)
        self.dark = QLabel(self.home)
        self.dark.setObjectName(u"dark")
        self.dark.setMaximumSize(QSize(16777215, 15))
        self.dark.setStyleSheet(u"padding-right: 5px;")

        self.horizontalLayout_7.addWidget(self.dark)

        self.switch_button = QCheckBox(self.home)
        self.switch_button.setObjectName(u"switch_button")
        self.switch_button.setMinimumSize(QSize(0, 0))
        self.switch_button.setMaximumSize(QSize(60, 20))

        self.horizontalLayout_7.addWidget(self.switch_button)

        self.light = QLabel(self.home)
        self.light.setObjectName(u"light")
        self.light.setMaximumSize(QSize(16777215, 15))
        self.light.setStyleSheet(u"padding-left: 5px;")

        self.horizontalLayout_7.addWidget(self.light)


        self.verticalLayout_16.addLayout(self.horizontalLayout_7)

        self.stackedWidget.addWidget(self.home)
        self.tutorial = QWidget()
        self.tutorial.setObjectName(u"tutorial")
        self.tutorial.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.tutorial)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget_2 = QStackedWidget(self.tutorial)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.sd_tutorial = QWidget()
        self.sd_tutorial.setObjectName(u"sd_tutorial")
        self.stackedWidget_2.addWidget(self.sd_tutorial)
        self.hg_tutorial = QWidget()
        self.hg_tutorial.setObjectName(u"hg_tutorial")
        self.stackedWidget_2.addWidget(self.hg_tutorial)

        self.verticalLayout.addWidget(self.stackedWidget_2)

        self.stackedWidget.addWidget(self.tutorial)
        self.handgesture = QWidget()
        self.handgesture.setObjectName(u"handgesture")
        self.verticalLayout_17 = QVBoxLayout(self.handgesture)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.handgesture_label = QLabel(self.handgesture)
        self.handgesture_label.setObjectName(u"handgesture_label")
        self.handgesture_label.setMaximumSize(QSize(16777215, 60))
        self.handgesture_label.setStyleSheet(u"padding-top:15px;")
        self.handgesture_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.handgesture_label)

        self.hg_layout = QGridLayout()
        self.hg_layout.setObjectName(u"hg_layout")
        self.hg_layout.setHorizontalSpacing(5)
        self.hg_layout.setVerticalSpacing(10)
        self.hg_layout.setContentsMargins(40, 40, 40, 20)
        self.car_cam = QLabel(self.handgesture)
        self.car_cam.setObjectName(u"car_cam")
        self.car_cam.setMinimumSize(QSize(320, 240))
        self.car_cam.setMaximumSize(QSize(320, 240))
        self.car_cam.setStyleSheet(u"background: #2E3440;\n"
"border: 3px solid #2E3440;\n"
"border-radius: 5px;")
        self.car_cam.setAlignment(Qt.AlignCenter)

        self.hg_layout.addWidget(self.car_cam, 0, 1, 1, 1)

        self.hg_message = QLabel(self.handgesture)
        self.hg_message.setObjectName(u"hg_message")
        self.hg_message.setMinimumSize(QSize(0, 100))
        self.hg_message.setMaximumSize(QSize(16777215, 80))
        self.hg_message.setStyleSheet(u"background:#D8DEE9;\n"
"border: 3px solid #2E3440;\n"
"border-radius: 5px; color: #2E3440; font-size: 20px")
        self.hg_message.setAlignment(Qt.AlignCenter)

        self.hg_layout.addWidget(self.hg_message, 1, 0, 1, 2)

        self.screen_cam = QLabel(self.handgesture)
        self.screen_cam.setObjectName(u"screen_cam")
        self.screen_cam.setMinimumSize(QSize(320, 240))
        self.screen_cam.setMaximumSize(QSize(320, 240))
        self.screen_cam.setStyleSheet(u"background: #2E3440;\n"
"border: 3px solid #2E3440;\n"
"border-radius: 5px;")
        self.screen_cam.setFrameShadow(QFrame.Plain)
        self.screen_cam.setAlignment(Qt.AlignCenter)

        self.hg_layout.addWidget(self.screen_cam, 0, 0, 1, 1)


        self.verticalLayout_17.addLayout(self.hg_layout)

        self.stackedWidget.addWidget(self.handgesture)
        self.selfdriving = QWidget()
        self.selfdriving.setObjectName(u"selfdriving")
        self.verticalLayout_18 = QVBoxLayout(self.selfdriving)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.selfdriving_label = QLabel(self.selfdriving)
        self.selfdriving_label.setObjectName(u"selfdriving_label")
        self.selfdriving_label.setMinimumSize(QSize(0, 60))
        self.selfdriving_label.setMaximumSize(QSize(16777215, 60))
        self.selfdriving_label.setFont(font)
        self.selfdriving_label.setStyleSheet(u"padding-top:25px; font-size:24pt; font-weight:700; color:#eceff4;")
        self.selfdriving_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.selfdriving_label)

        self.sd_layout = QFrame(self.selfdriving)
        self.sd_layout.setObjectName(u"sd_layout")
        self.sd_layout.setStyleSheet(u"")
        self.sd_layout.setFrameShape(QFrame.StyledPanel)
        self.sd_layout.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.sd_layout)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_sd1 = QVBoxLayout()
        self.verticalLayout_sd1.setObjectName(u"verticalLayout_sd1")
        self.verticalLayout_sd1.setContentsMargins(30, -1, 40, 30)
        self.sd_main_screen = QLabel(self.sd_layout)
        self.sd_main_screen.setObjectName(u"sd_main_screen")
        self.sd_main_screen.setMinimumSize(QSize(360, 270))
        self.sd_main_screen.setMaximumSize(QSize(320, 240))
        self.sd_main_screen.setStyleSheet(u"background: #2E3440;\n"
"border: 3px solid #2E3440;\n"
"border-radius: 5px;")
        self.sd_main_screen.setAlignment(Qt.AlignCenter)

        self.verticalLayout_sd1.addWidget(self.sd_main_screen)


        self.horizontalLayout_6.addLayout(self.verticalLayout_sd1)

        self.verticalLayout_sd2 = QVBoxLayout()
        self.verticalLayout_sd2.setSpacing(0)
        self.verticalLayout_sd2.setObjectName(u"verticalLayout_sd2")
        self.verticalLayout_sd2.setContentsMargins(0, -1, 80, -1)
        self.sd_subscreen1 = QLabel(self.sd_layout)
        self.sd_subscreen1.setObjectName(u"sd_subscreen1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sd_subscreen1.sizePolicy().hasHeightForWidth())
        self.sd_subscreen1.setSizePolicy(sizePolicy3)
        self.sd_subscreen1.setMinimumSize(QSize(280, 210))
        self.sd_subscreen1.setMaximumSize(QSize(280, 210))
        self.sd_subscreen1.setStyleSheet(u"background: #2E3440;\n"
"border: 3px solid #2E3440;\n"
"border-radius: 5px;")
        self.sd_subscreen1.setMidLineWidth(0)
        self.sd_subscreen1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_sd2.addWidget(self.sd_subscreen1)

        self.sd_message = QLabel(self.sd_layout)
        self.sd_message.setObjectName(u"sd_message")
        self.sd_message.setMinimumSize(QSize(280, 100))
        self.sd_message.setMaximumSize(QSize(280, 100))
        self.sd_message.setStyleSheet(u"background: #D8DEE9;\n"
"border: 3px solid #2E3440;\n"
"border-radius: 5px; color: #2E3440; font-size: 20px")
        self.sd_message.setAlignment(Qt.AlignCenter)

        self.verticalLayout_sd2.addWidget(self.sd_message)


        self.horizontalLayout_6.addLayout(self.verticalLayout_sd2)


        self.verticalLayout_18.addWidget(self.sd_layout)

        self.stackedWidget.addWidget(self.selfdriving)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(False)
        font4.setItalic(False)
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.gridLayout.addWidget(self.bgApp, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Genesis", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Autonomous car system", None))
        self.topLogo.setText("")
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_self_driving.setText(QCoreApplication.translate("MainWindow", u"Self Driving Mode", None))
        self.btn_hand_gesture.setText(QCoreApplication.translate("MainWindow", u"Hand Gesture Mode", None))
        self.btn_document.setText(QCoreApplication.translate("MainWindow", u"Document", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.bklogo.setText("")
        self.welcome.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#d8dee9;\">Welcome to</span></p></body></html>", None))
        self.appname.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-family:'Copperplate'; font-size:36pt; font-weight:700; color:#81a1c1;\">Genesis</span></p></body></html>", None))
        self.appdescription.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#d8dee9;\">----------------------------------------</span></p><p align=\"center\"><span style=\" color:#eceff4;\">A mecanum car system integrated with </span></p><p align=\"center\"><span style=\" color:#eceff4;\">lane following, object detection and hand gesture control features</span></p></body></html>", None))
        self.teammember.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700; color:#d8dee9;\">Team CacheHit</span></p><p align=\"center\"><span style=\" font-size:8pt; color:#eceff4;\">Huynh Minh Tri</span></p><p align=\"center\"><span style=\" font-size:8pt; color:#eceff4;\">Dang Cao Cuong</span></p><p align=\"center\"><span style=\" font-size:8pt; color:#eceff4;\">Quach Dang Giang</span></p><p align=\"center\"><span style=\" font-size:8pt; color:#eceff4;\">Tran Nhat Tan</span></p><p align=\"center\"><span style=\" font-size:8pt; color:#eceff4;\">Luu Chan Hung</span></p></body></html>", None))
        self.howtouse.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700; color:#d8dee9;\">Simple Guide</span></p><p><img src=\":/icons/images/icons/cil-cursor-move.png\"/><span style=\" font-weight:700; font-style:italic; color:#eceff4;\">Self-driving mode</span><span style=\" font-weight:700; color:#eceff4;\">: </span><span style=\" color:#eceff4;\">Sit back and let's the car be the driver itself</span></p><p><img src=\":/icons/images/icons/cil-hand-point-right.png\"/><span style=\" font-weight:700; font-style:italic; color:#eceff4;\">Hand-gesture mode</span><span style=\" font-weight:700; color:#eceff4;\">: </span><span style=\" color:#eceff4;\">Control your car by a set of hand gestures</span></p><p><img src=\":/icons/images/icons/cil-description.png\"/><span style=\" font-weight:700; font-style:italic; color:#eceff4;\">Tutorial</span><span style=\" font-weight:700; color:#eceff4;\">: </span><span style=\" color:#eceff4;\">Learn how each mode works ?</span></p></body></html>", None))
        self.dark.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">DARK</p></body></html>", None))
        self.switch_button.setText("")
        self.light.setText(QCoreApplication.translate("MainWindow", u"LIGHT", None))
        self.handgesture_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700; color:#eceff4;\">HAND GESTURE MODE</span></p></body></html>", None))
        self.car_cam.setText(QCoreApplication.translate("MainWindow", u"Car Screen", None))
        self.hg_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.screen_cam.setText(QCoreApplication.translate("MainWindow", u"Camera Screen", None))
        self.selfdriving_label.setText(QCoreApplication.translate("MainWindow", u"SELF DRVING MODE", None))
        self.sd_main_screen.setText(QCoreApplication.translate("MainWindow", u"Main Screen", None))
        self.sd_subscreen1.setText(QCoreApplication.translate("MainWindow", u"Sub Screen", None))
        self.sd_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Team CacheHit - Ho Chi Minh City University of Technology", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

