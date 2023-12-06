# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        ############################################################
        ############################################################
        #################### app main window #######################
        # app main window
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 600)
        self.app_main_widget = QWidget(MainWindow)
        self.app_main_widget.setObjectName(u"app_main_widget")
        # app main window grid layout
        self.app_main_gridLay = QGridLayout(self.app_main_widget)
        self.app_main_gridLay.setSpacing(0)
        self.app_main_gridLay.setObjectName(u"app_main_gridLay")
        self.app_main_gridLay.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.app_main_widget)
        MainWindow.setWindowTitle("برنامج المساعد الرقمي")

        ###################################################################################
        ##################### app main window -) content main widget ######################
        # content main widget
        self.content_main_widget = QWidget(self.app_main_widget)
        self.content_main_widget.setObjectName(u"content_main_widget")
        self.content_main_widget.setMaximumSize(QSize(16777215, 16777215))
        self.app_main_gridLay.addWidget(self.content_main_widget, 0, 1, 1, 1)
        # content main widget vertical layout
        self.content_main_vertiLay = QVBoxLayout(self.content_main_widget)
        self.content_main_vertiLay.setSpacing(0)
        self.content_main_vertiLay.setObjectName(u"content_main_vertiLay")
        self.content_main_vertiLay.setContentsMargins(0, 0, 0, 0)

        ##################### app main window -) content main widget -) content header widget ######################
        # content header widget
        self.content_header_widget = QWidget()
        self.content_header_widget.setObjectName(u"content_header_widget")
        self.content_header_widget.setMinimumSize(QSize(0, 40))
        self.content_main_vertiLay.addWidget(self.content_header_widget)
        # content header widget horizontal layout
        self.content_header_widget_horizlay = QHBoxLayout(self.content_header_widget)
        self.content_header_widget_horizlay.setSpacing(0)
        self.content_header_widget_horizlay.setObjectName(u"content_header_widget_horizlay")
        self.content_header_widget_horizlay.setContentsMargins(0, 0, 9, 0)
        
        # content header toggle menu button
        self.toggle_menu_btn = QPushButton()
        self.toggle_menu_btn.setObjectName(u"toggle_menu_btn")
        icon = QIcon()
        icon.addFile(u":/icon/icon/menu-4-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.toggle_menu_btn.setIcon(icon)
        self.toggle_menu_btn.setIconSize(QSize(14, 14))
        self.toggle_menu_btn.setCheckable(True)
        self.content_header_widget_horizlay.addWidget(self.toggle_menu_btn)

        # content header left horizontal spacer
        self.header_left_horiSpacer = QSpacerItem(236, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.content_header_widget_horizlay.addItem(self.header_left_horiSpacer)

        # content header search box horizontal layout
        self.searchbox_horizLay = QHBoxLayout()
        self.searchbox_horizLay.setSpacing(10)
        self.searchbox_horizLay.setObjectName(u"searchbox_horizLay")
        self.content_header_widget_horizlay.addLayout(self.searchbox_horizLay)
        # content header search input lineedit
        self.search_input = QLineEdit()
        self.search_input.setObjectName(u"search_input")
        self.search_input.setPlaceholderText(u"Search...")
        self.searchbox_horizLay.addWidget(self.search_input)
        # content header search button
        self.search_btn = QPushButton(self.content_header_widget)
        self.search_btn.setObjectName(u"search_btn")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/search-13-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon1)
        self.searchbox_horizLay.addWidget(self.search_btn)

        # content header right horizontal spacer
        self.header_right_horiSpacer = QSpacerItem(236, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.content_header_widget_horizlay.addItem(self.header_right_horiSpacer)

        # content header user button
        self.user_btn = QPushButton()
        self.user_btn.setObjectName(u"user_btn")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/user-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.user_btn.setIcon(icon2)
        self.content_header_widget_horizlay.addWidget(self.user_btn)

        ##################### app main window -) content main widget -) content stack widget ######################
        # content stack widget
        self.content_stackedWidget = QStackedWidget()
        self.content_stackedWidget.setObjectName(u"content_stackedWidget")
        self.content_main_vertiLay.addWidget(self.content_stackedWidget)
        # content stack widget
        font = QFont()
        font.setPointSize(20)
        # content stack widget home page
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_vertilay = QVBoxLayout(self.page_home)
        self.label_home = QLabel()
        self.label_home.setObjectName(u"label_home")
        self.label_home.setFont(font)
        self.label_home.setAlignment(Qt.AlignCenter)
        self.label_home.setText(u"The home page")
        self.page_vertilay.addWidget(self.label_home)
        self.content_stackedWidget.addWidget(self.page_home)
        # content stack widget dashboard page
        self.page_dashboard = QWidget()
        self.page_dashboard.setObjectName(u"page_dashboard")
        self.page_vertilay = QVBoxLayout(self.page_dashboard)
        self.label_dashboard = QLabel()
        self.label_dashboard.setObjectName(u"label_dashboard")
        self.label_dashboard.setFont(font)
        self.label_dashboard.setAlignment(Qt.AlignCenter)
        self.label_dashboard.setText(u"The dashboard page")
        self.page_vertilay.addWidget(self.label_dashboard)
        self.content_stackedWidget.addWidget(self.page_dashboard)
        # content stack widget search page
        self.page_search = QWidget()
        self.page_search.setObjectName(u"page_search")
        self.page_vertilay = QVBoxLayout(self.page_search)
        self.label_search = QLabel()
        self.label_search.setObjectName(u"label_search")
        self.label_search.setFont(font)
        self.label_search.setAlignment(Qt.AlignCenter)
        self.label_search.setText(u"The search page")
        self.page_vertilay.addWidget(self.label_search)
        self.content_stackedWidget.addWidget(self.page_search)
        # content stack widget user page
        self.page_user = QWidget()
        self.page_user.setObjectName(u"page_user")
        self.page_vertilay = QVBoxLayout(self.page_user)
        self.label_user = QLabel()
        self.label_user.setObjectName(u"label_user")
        self.label_user.setFont(font)
        self.label_user.setAlignment(Qt.AlignCenter)
        self.label_user.setText(u"The user page")
        self.page_vertilay.addWidget(self.label_user)
        self.content_stackedWidget.addWidget(self.page_user)


        ###################################################################################
        ##################### app main window -) sidebar main widget ######################
        # sidebar main widget
        self.sidebar_main_widget = QWidget(self.app_main_widget)
        self.sidebar_main_widget.setObjectName(u"sidebar_main_widget")
        self.sidebar_main_widget.setMaximumSize(QSize(16777215, 16777215))
        # sidebar main widget vertical layout
        self.sidebar_main_widget_vertilay = QVBoxLayout(self.sidebar_main_widget)
        self.sidebar_main_widget_vertilay.setObjectName(u"sidebar_main_widget_vertilay")
        self.app_main_gridLay.addWidget(self.sidebar_main_widget, 0, 2, 1, 1)
        # sidebar main title horizontal layout
        self.sidebar_title_horizLay = QHBoxLayout()
        self.sidebar_title_horizLay.setSpacing(0)
        self.sidebar_title_horizLay.setObjectName(u"sidebar_title_horizLay")
        self.sidebar_main_widget_vertilay.addLayout(self.sidebar_title_horizLay)
        # sidebar title icon
        self.logo_label_icon = QLabel(self.sidebar_main_widget)
        self.logo_label_icon.setObjectName(u"logo_label_icon")
        self.logo_label_icon.setMinimumSize(QSize(40, 40))
        self.logo_label_icon.setMaximumSize(QSize(40, 40))
        self.logo_label_icon.setPixmap(QPixmap(u":/icon/icon/Logo.png"))
        self.logo_label_icon.setScaledContents(True)
        self.sidebar_title_horizLay.addWidget(self.logo_label_icon)
        # sidebar title text
        self.logo_label_text = QLabel(self.sidebar_main_widget)
        self.logo_label_text.setObjectName(u"logo_label_text")
        font1 = QFont()
        font1.setPointSize(15)
        self.logo_label_text.setFont(font1)
        self.logo_label_text.setText(u"قائمة العمل")
        self.sidebar_title_horizLay.addWidget(self.logo_label_text)
        # sidebar items box vertical layout 
        self.sidebar_items_vertiLay = QVBoxLayout()
        self.sidebar_items_vertiLay.setSpacing(0)
        self.sidebar_items_vertiLay.setObjectName(u"sidebar_items_vertiLay")
        self.sidebar_main_widget_vertilay.addLayout(self.sidebar_items_vertiLay)
        # sidebar item: home button
        self.home_btn = QPushButton()
        self.home_btn.setObjectName(u"home_btn")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/home-4-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icon/icon/home-4-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.home_btn.setIcon(icon3)
        self.home_btn.setIconSize(QSize(14, 14))
        self.home_btn.setCheckable(True)
        self.home_btn.setAutoExclusive(True)
        self.sidebar_items_vertiLay.addWidget(self.home_btn)
        # sidebar item: dashboard button
        self.dashborad_btn = QPushButton()
        self.dashborad_btn.setObjectName(u"dashborad_btn")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/dashboard-5-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icon/icon/dashboard-5-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.dashborad_btn.setIcon(icon4)
        self.dashborad_btn.setIconSize(QSize(14, 14))
        self.dashborad_btn.setCheckable(True)
        self.dashborad_btn.setAutoExclusive(True)
        self.sidebar_items_vertiLay.addWidget(self.dashborad_btn)
        # sidebar vertical spacer
        self.sidebar_vertiSpacer = QSpacerItem(20, 373, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.sidebar_main_widget_vertilay.addItem(self.sidebar_vertiSpacer)
        # sidebar exit button
        self.exit_btn = QPushButton()
        self.exit_btn.setObjectName(u"exit_btn")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/close-window-64.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_btn.setIcon(icon5)
        self.exit_btn.setIconSize(QSize(14, 14))
        self.sidebar_main_widget_vertilay.addWidget(self.exit_btn)



        self.toggle_menu_btn.toggled.connect(self.sidebar_main_widget.setHidden)
        self.exit_btn.clicked.connect(MainWindow.close)

        self.content_stackedWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)

