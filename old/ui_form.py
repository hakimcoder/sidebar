# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar_rtl.ui'
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
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.full_menu_widget = QWidget(self.centralwidget)
        self.full_menu_widget.setObjectName(u"full_menu_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.full_menu_widget.sizePolicy().hasHeightForWidth())
        self.full_menu_widget.setSizePolicy(sizePolicy)
        self.full_menu_widget.setMaximumSize(QSize(16777214, 16777215))
        
        self.sidebar_verticalLayout = QVBoxLayout(self.full_menu_widget)
        self.sidebar_verticalLayout.setObjectName(u"sidebar_verticalLayout")

        self.logo_horizontalLayout = QHBoxLayout()
        self.logo_horizontalLayout.setSpacing(0)
        self.logo_horizontalLayout.setObjectName(u"logo_horizontalLayout")
        
        self.logo_text_label = QLabel(self.full_menu_widget)
        self.logo_text_label.setObjectName(u"logo_text_label")
        font = QFont()
        font.setPointSize(15)
        self.logo_text_label.setFont(font)

        self.logo_horizontalLayout.addWidget(self.logo_text_label)

        self.logo_icon_label = QLabel(self.full_menu_widget)
        self.logo_icon_label.setObjectName(u"logo_icon_label")
        self.logo_icon_label.setMinimumSize(QSize(40, 40))
        self.logo_icon_label.setMaximumSize(QSize(40, 40))
        self.logo_icon_label.setPixmap(QPixmap(u":/icon/icon/Logo.png"))
        self.logo_icon_label.setScaledContents(True)

        self.logo_horizontalLayout.addWidget(self.logo_icon_label)

        self.sidebar_verticalLayout.addLayout(self.logo_horizontalLayout)

        self.buttons_verticalLayout = QVBoxLayout()
        self.buttons_verticalLayout.setSpacing(0)
        self.buttons_verticalLayout.setObjectName(u"buttons_verticalLayout")

        self.home_btn = QPushButton(self.full_menu_widget)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setLayoutDirection(Qt.LeftToRight)
        self.home_btn.setLocale(QLocale(QLocale.Arabic, QLocale.Morocco))
        icon = QIcon()
        icon.addFile(u":/icon/icon/home-4-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icon/icon/home-4-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.home_btn.setIcon(icon)
        self.home_btn.setIconSize(QSize(14, 14))
        self.home_btn.setCheckable(True)
        self.home_btn.setAutoExclusive(True)

        self.buttons_verticalLayout.addWidget(self.home_btn)

        self.dashborad_btn = QPushButton(self.full_menu_widget)
        self.dashborad_btn.setObjectName(u"dashborad_btn")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/dashboard-5-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icon/icon/dashboard-5-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.dashborad_btn.setIcon(icon1)
        self.dashborad_btn.setIconSize(QSize(14, 14))
        self.dashborad_btn.setCheckable(True)
        self.dashborad_btn.setAutoExclusive(True)

        self.buttons_verticalLayout.addWidget(self.dashborad_btn)

        self.sidebar_verticalLayout.addLayout(self.buttons_verticalLayout)

        self.sidebar_verticalSpacer = QSpacerItem(20, 373, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.sidebar_verticalLayout.addItem(self.sidebar_verticalSpacer)

        self.exit_btn = QPushButton(self.full_menu_widget)
        self.exit_btn.setObjectName(u"exit_btn")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/close-window-64.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_btn.setIcon(icon2)
        self.exit_btn.setIconSize(QSize(14, 14))

        self.sidebar_verticalLayout.addWidget(self.exit_btn)

        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)

        self.pages_container = QWidget(self.centralwidget)
        self.pages_container.setObjectName(u"pages_container")
        self.pages_container.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pages_container.sizePolicy().hasHeightForWidth())
        self.pages_container.setSizePolicy(sizePolicy)
        self.pages_container.setMaximumSize(QSize(16777214, 16777215))

        self.pages_verticalLayout = QVBoxLayout(self.pages_container)
        self.pages_verticalLayout.setSpacing(0)
        self.pages_verticalLayout.setObjectName(u"pages_verticalLayout")
        self.pages_verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.pages_verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.pages_header_horizontalLayout = QHBoxLayout(self.pages_container)
        self.pages_header_horizontalLayout.setSpacing(0)
        self.pages_header_horizontalLayout.setObjectName(u"pages_header_horizontalLayout")
        self.pages_header_horizontalLayout.setContentsMargins(0, 0, 9, 0)

        # self.pages_search_box = QWidget(self.pages_header_horizontalLayout)
        # self.pages_search_box.setObjectName(u"pages_search_box")
        # self.pages_search_box.setMinimumSize(QSize(0, 40))

        self.user_btn = QPushButton()
        self.user_btn.setObjectName(u"user_btn")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/user-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.user_btn.setIcon(icon3)

        self.pages_header_horizontalLayout.addWidget(self.user_btn)

        self.pages_horizontalSpacer_left = QSpacerItem(236, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.pages_header_horizontalLayout.addItem(self.pages_horizontalSpacer_left)

        self.search_horizontalLayout = QHBoxLayout()
        # self.search_horizontalLayout.setSpacing(10)
        # self.search_horizontalLayout.setObjectName(u"search_horizontalLayout")
        self.search_horizontalLayout.setObjectName(u"pages_search_box")
        # self.search_horizontalLayout.setMinimumSize(QSize(0, 40))

        self.search_btn = QPushButton()
        self.search_btn.setObjectName(u"search_btn")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/search-13-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon4)

        self.search_horizontalLayout.addWidget(self.search_btn)

        self.search_input = QLineEdit()
        self.search_input.setObjectName(u"search_input")

        self.search_horizontalLayout.addWidget(self.search_input)

        self.pages_header_horizontalLayout.addLayout(self.search_horizontalLayout)

        self.pages_horizontalSpacer_right = QSpacerItem(236, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.pages_header_horizontalLayout.addItem(self.pages_horizontalSpacer_right)

        self.btn_toggle_menu = QPushButton()
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/menu-4-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle_menu.setIcon(icon5)
        self.btn_toggle_menu.setIconSize(QSize(14, 14))
        self.btn_toggle_menu.setCheckable(True)

        self.pages_header_horizontalLayout.addWidget(self.btn_toggle_menu)

        self.pages_verticalLayout.addWidget(self.pages_search_box)

        self.stackedWidget = QStackedWidget(self.pages_container)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.gridLayout_2 = QGridLayout(self.page_home)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_home = QLabel(self.page_home)
        self.label_home.setObjectName(u"label_home")
        font1 = QFont()
        font1.setPointSize(20)
        self.label_home.setFont(font1)
        self.label_home.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_home, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_home)
        self.page_dashboard = QWidget()
        self.page_dashboard.setObjectName(u"page_dashboard")
        self.gridLayout_3 = QGridLayout(self.page_dashboard)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_dashboard = QLabel(self.page_dashboard)
        self.label_dashboard.setObjectName(u"label_dashboard")
        self.label_dashboard.setFont(font1)
        self.label_dashboard.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_dashboard, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_dashboard)
        self.page_user = QWidget()
        self.page_user.setObjectName(u"page_user")
        self.gridLayout_8 = QGridLayout(self.page_user)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_user = QLabel(self.page_user)
        self.label_user.setObjectName(u"label_user")
        self.label_user.setFont(font1)
        self.label_user.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_user, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_user)
        self.page_search = QWidget()
        self.page_search.setObjectName(u"page_search")
        self.gridLayout_7 = QGridLayout(self.page_search)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_search = QLabel(self.page_search)
        self.label_search.setObjectName(u"label_search")
        self.label_search.setFont(font1)
        self.label_search.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_search, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_search)

        self.pages_verticalLayout.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.pages_container, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_toggle_menu.toggled.connect(self.full_menu_widget.setHidden)
        self.exit_btn.clicked.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_text_label.setText(QCoreApplication.translate("MainWindow", u"Sidebar", None))
        self.logo_icon_label.setText("")
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.dashborad_btn.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.user_btn.setText("")
        self.search_btn.setText("")
        self.search_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.btn_toggle_menu.setText("")
        self.label_home.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.label_dashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard Page", None))
        self.label_user.setText(QCoreApplication.translate("MainWindow", u"User Page", None))
        self.label_search.setText(QCoreApplication.translate("MainWindow", u"Search Page", None))
    # retranslateUi

