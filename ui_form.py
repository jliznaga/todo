# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QGridLayout, QLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QCheckBox {\n"
"	background-color: #FFF;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border: 2px solid #ddd;\n"
"	margin-right: 3px;\n"
"	border-radius: 4px;\n"
"	height: 10px;\n"
"	width: 10px;\n"
"}\n"
"\n"
" QCheckBox::indicator:checked {\n"
"	border: 2px solid #2784ff;\n"
"	background-color: #2784ff;\n"
"	color: #FFF;\n"
"}")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 791, 541))
        self.addTaskBtn = QPushButton(self.widget)
        self.addTaskBtn.setObjectName(u"addTaskBtn")
        self.addTaskBtn.setGeometry(QRect(20, 20, 291, 36))
        self.addTaskBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addTaskBtn.setAutoDefault(False)
        self.addTaskBtn.setFlat(False)
        self.newTaskWrapper = QWidget(self.widget)
        self.newTaskWrapper.setObjectName(u"newTaskWrapper")
        self.newTaskWrapper.setGeometry(QRect(20, 60, 761, 51))
        self.newTaskWrapper.setAutoFillBackground(True)
        self.newTaskWrapper.setStyleSheet(u"")
        self.gridLayoutWidget = QWidget(self.newTaskWrapper)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 761, 48))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.createTaskBtn = QPushButton(self.gridLayoutWidget)
        self.createTaskBtn.setObjectName(u"createTaskBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.createTaskBtn.sizePolicy().hasHeightForWidth())
        self.createTaskBtn.setSizePolicy(sizePolicy)
        self.createTaskBtn.setMinimumSize(QSize(32, 36))
        self.createTaskBtn.setMaximumSize(QSize(32, 16777215))
        self.createTaskBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.createTaskBtn.setLayoutDirection(Qt.RightToLeft)
        self.createTaskBtn.setStyleSheet(u"")
        self.createTaskBtn.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.createTaskBtn, 0, 3, 1, 1)

        self.descEdit = QLineEdit(self.gridLayoutWidget)
        self.descEdit.setObjectName(u"descEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.descEdit.sizePolicy().hasHeightForWidth())
        self.descEdit.setSizePolicy(sizePolicy1)
        self.descEdit.setMinimumSize(QSize(0, 36))
        self.descEdit.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout.addWidget(self.descEdit, 0, 2, 1, 1)

        self.titleEdit = QLineEdit(self.gridLayoutWidget)
        self.titleEdit.setObjectName(u"titleEdit")
        self.titleEdit.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleEdit.sizePolicy().hasHeightForWidth())
        self.titleEdit.setSizePolicy(sizePolicy2)
        self.titleEdit.setMinimumSize(QSize(200, 36))
        self.titleEdit.setMaximumSize(QSize(200, 16777215))
        self.titleEdit.setFocusPolicy(Qt.ClickFocus)
        self.titleEdit.setAutoFillBackground(False)
        self.titleEdit.setFrame(False)
        self.titleEdit.setCursorPosition(0)

        self.gridLayout.addWidget(self.titleEdit, 0, 1, 1, 1)

        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setGeometry(QRect(10, 140, 781, 401))
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setStyleSheet(u"QScrollBar:horizontal\n"
"    {\n"
"        height: 15px;\n"
"        margin: 3px 15px 3px 15px;\n"
"        border: 1px transparent #2A2929;\n"
"        border-radius: 4px;\n"
"        background-color: yellow;    /* #2A2929; */\n"
"    }\n"
"\n"
"    QScrollBar::handle:horizontal\n"
"    {\n"
"        background-color: blue;      /* #605F5F; */\n"
"        min-width: 5px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:horizontal\n"
"    {\n"
"        margin: 0px 3px 0px 3px;\n"
"        border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"        width: 10px;\n"
"        height: 10px;\n"
"        subcontrol-position: right;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:horizontal\n"
"    {\n"
"        margin: 0px 3px 0px 3px;\n"
"        border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: left;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
""
                        "\n"
"    QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: right;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"\n"
"    QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: left;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"\n"
"    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar:vertical\n"
"    {\n"
"        background-color: #2A2929;\n"
"        width: 15px;\n"
"        margin: 15px 3px 15px 3px;\n"
"        border"
                        ": 1px transparent #2A2929;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:vertical\n"
"    {\n"
"        background-color: red;         /* #605F5F; */\n"
"        min-height: 5px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"        height: 10px;"
                        "\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"    {\n"
"        background: none;\n"
"    }")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setEnabled(True)
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 779, 399))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QFormLayout.WrapAllRows)

        self.verticalLayout.addLayout(self.formLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.completedTaskChBx = QCheckBox(self.widget)
        self.completedTaskChBx.setObjectName(u"completedTaskChBx")
        self.completedTaskChBx.setGeometry(QRect(620, 30, 171, 20))
        self.completedTaskChBx.setCursor(QCursor(Qt.PointingHandCursor))
        self.completedTaskChBx.setStyleSheet(u"QCheckBox {\n"
"	background-color: #FFF\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border: 2px solid #ddd;\n"
"	margin-right: 3px;\n"
"	border-radius: 4px;\n"
"	height: 10px;\n"
"	width: 10px;\n"
"}\n"
"\n"
" QCheckBox::indicator:checked {\n"
"	border: 2px solid #2784ff;\n"
"	background-color: #2784ff;\n"
"	color: #FFF;\n"
"}\n"
"")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 781, 111))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.raise_()
        self.addTaskBtn.raise_()
        self.newTaskWrapper.raise_()
        self.scrollArea.raise_()
        self.completedTaskChBx.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.addTaskBtn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VIVA TODO", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(QCoreApplication.translate("MainWindow", u"Viva Todo", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.widget.setToolTip(QCoreApplication.translate("MainWindow", u"Title", None))
#endif // QT_CONFIG(tooltip)
        self.addTaskBtn.setText(QCoreApplication.translate("MainWindow", u"Add a new task", None))
        self.createTaskBtn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.descEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Description", None))
#if QT_CONFIG(tooltip)
        self.titleEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.titleEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.completedTaskChBx.setText(QCoreApplication.translate("MainWindow", u"Show completed tasks", None))
    # retranslateUi

