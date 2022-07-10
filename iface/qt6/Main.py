# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QColumnView, QComboBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(647, 397)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0())
        self.verticalLayout.setMargin(0())
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0())
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setMargin(0())
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setSpacing(0())
        self.verticalLayout_5.setMargin(0())
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tableView = QTableView(self.widget_2)
        self.tableView.setObjectName(u"tableView")
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setFrameShape(QFrame.NoFrame)
        self.tableView.setLineWidth(0)
        self.tableView.setAlternatingRowColors(False)
        self.tableView.setWordWrap(False)
        self.tableView.horizontalHeader().setVisible(False)
        self.tableView.horizontalHeader().setHighlightSections(False)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.verticalHeader().setHighlightSections(False)

        self.verticalLayout_5.addWidget(self.tableView)

        self.groupBox_2 = QGroupBox(self.widget_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QSize(0, 10))
        self.groupBox_2.setMaximumSize(QSize(16777215, 100))
        self.formLayout = QFormLayout(self.groupBox_2)
        self.formLayout.setSpacing(0())
        self.formLayout.setMargin(0())
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.widget_3 = QWidget(self.groupBox_2)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.widget_3.setMinimumSize(QSize(200, 20))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setSpacing(0())
        self.horizontalLayout_4.setMargin(0())
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.comboBox_3 = QComboBox(self.widget_3)
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.comboBox_3)


        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.widget_3)

        self.lbl_combox = QWidget(self.groupBox_2)
        self.lbl_combox.setObjectName(u"lbl_combox")
        sizePolicy1.setHeightForWidth(self.lbl_combox.sizePolicy().hasHeightForWidth())
        self.lbl_combox.setSizePolicy(sizePolicy1)
        self.lbl_combox.setMinimumSize(QSize(200, 20))
        self.horizontalLayout_3 = QHBoxLayout(self.lbl_combox)
        self.horizontalLayout_3.setSpacing(0())
        self.horizontalLayout_3.setMargin(0())
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.lbl_combox)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy2.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.comboBox)


        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lbl_combox)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)


        self.verticalLayout_5.addWidget(self.groupBox_2)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setMargin(0())
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setMargin(0())
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.columnView = QColumnView(self.frame_2)
        self.columnView.setObjectName(u"columnView")
        sizePolicy.setHeightForWidth(self.columnView.sizePolicy().hasHeightForWidth())
        self.columnView.setSizePolicy(sizePolicy)
        self.columnView.setMinimumSize(QSize(0, 20))

        self.verticalLayout_2.addWidget(self.columnView)

        self.tabWidget = QTabWidget(self.frame_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setSpacing(0())
        self.gridLayout.setMargin(0())
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox = QCheckBox(self.tab)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.tab)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0())
        self.horizontalLayout_2.setMargin(0())
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 647, 21))
        self.menuMain = QMenu(self.menubar)
        self.menuMain.setObjectName(u"menuMain")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy3)
        self.statusbar.setMinimumSize(QSize(0, 10))
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMain.menuAction())
qtq
        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Management Profiles", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Performance ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Energy", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"BD_PROCHOT", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"TurboBoost", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.menuMain.setTitle(QCoreApplication.translate("MainWindow", u"Main", None))
    # retranslateUi

