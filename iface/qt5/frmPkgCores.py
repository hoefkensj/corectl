# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmPkgCores.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(527, 325)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(527, 325))
        self.wgt_tblPpgCores = QtWidgets.QWidget(Form)
        self.wgt_tblPpgCores.setGeometry(QtCore.QRect(0, 0, 471, 283))
        self.wgt_tblPpgCores.setObjectName("wgt_tblPpgCores")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.wgt_tblPpgCores)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frmPkgCores_Data = QtWidgets.QFrame(self.wgt_tblPpgCores)
        self.frmPkgCores_Data.setObjectName("frmPkgCores_Data")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frmPkgCores_Data)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treeWidget = QtWidgets.QTreeWidget(self.frmPkgCores_Data)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.verticalLayout_2.addWidget(self.treeWidget)
        self.verticalLayout.addWidget(self.frmPkgCores_Data)
        self.frmPkgCores_Opts = QtWidgets.QFrame(self.wgt_tblPpgCores)
        self.frmPkgCores_Opts.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frmPkgCores_Opts.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frmPkgCores_Opts.setObjectName("frmPkgCores_Opts")
        self.gridLayout = QtWidgets.QGridLayout(self.frmPkgCores_Opts)
        self.gridLayout.setObjectName("gridLayout")
        self.grpOption = QtWidgets.QGroupBox(self.frmPkgCores_Opts)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpOption.sizePolicy().hasHeightForWidth())
        self.grpOption.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ableton Sans Small")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.grpOption.setFont(font)
        self.grpOption.setAutoFillBackground(True)
        self.grpOption.setFlat(True)
        self.grpOption.setCheckable(False)
        self.grpOption.setObjectName("grpOption")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.grpOption)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.optSpnBox_1 = QtWidgets.QWidget(self.grpOption)
        self.optSpnBox_1.setObjectName("optSpnBox_1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.optSpnBox_1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblRefresh = QtWidgets.QLabel(self.optSpnBox_1)
        self.lblRefresh.setObjectName("lblRefresh")
        self.horizontalLayout.addWidget(self.lblRefresh)
        self.spnUpdatePeriod = QtWidgets.QDoubleSpinBox(self.optSpnBox_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spnUpdatePeriod.sizePolicy().hasHeightForWidth())
        self.spnUpdatePeriod.setSizePolicy(sizePolicy)
        self.spnUpdatePeriod.setMinimumSize(QtCore.QSize(0, 20))
        self.spnUpdatePeriod.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.spnUpdatePeriod.setMouseTracking(True)
        self.spnUpdatePeriod.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spnUpdatePeriod.setAccelerated(True)
        self.spnUpdatePeriod.setProperty("showGroupSeparator", False)
        self.spnUpdatePeriod.setDecimals(2)
        self.spnUpdatePeriod.setMinimum(0.0)
        self.spnUpdatePeriod.setMaximum(60.0)
        self.spnUpdatePeriod.setSingleStep(1.0)
        self.spnUpdatePeriod.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.spnUpdatePeriod.setProperty("value", 1.0)
        self.spnUpdatePeriod.setObjectName("spnUpdatePeriod")
        self.horizontalLayout.addWidget(self.spnUpdatePeriod)
        self.horizontalLayout_4.addWidget(self.optSpnBox_1)
        self.optCmbBox_3 = QtWidgets.QWidget(self.grpOption)
        self.optCmbBox_3.setObjectName("optCmbBox_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.optCmbBox_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblRefresh_3 = QtWidgets.QLabel(self.optCmbBox_3)
        self.lblRefresh_3.setObjectName("lblRefresh_3")
        self.horizontalLayout_3.addWidget(self.lblRefresh_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.optCmbBox_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        self.horizontalLayout_4.addWidget(self.optCmbBox_3)
        self.optCmbBox_2 = QtWidgets.QWidget(self.grpOption)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.optCmbBox_2.sizePolicy().hasHeightForWidth())
        self.optCmbBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ableton Sans Small")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.optCmbBox_2.setFont(font)
        self.optCmbBox_2.setObjectName("optCmbBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.optCmbBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblRefresh_2 = QtWidgets.QLabel(self.optCmbBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblRefresh_2.sizePolicy().hasHeightForWidth())
        self.lblRefresh_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ableton Sans Small")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblRefresh_2.setFont(font)
        self.lblRefresh_2.setObjectName("lblRefresh_2")
        self.horizontalLayout_2.addWidget(self.lblRefresh_2)
        self.comboBox = QtWidgets.QComboBox(self.optCmbBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ableton Sans Small")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setFrame(True)
        self.comboBox.setModelColumn(0)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.horizontalLayout_4.addWidget(self.optCmbBox_2)
        self.gridLayout.addWidget(self.grpOption, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frmPkgCores_Opts)
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(60, 280, 141, 35))
        self.toolButton.setObjectName("toolButton")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(260, 290, 99, 35))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.grpOption.setTitle(_translate("Form", "Refresh"))
        self.lblRefresh.setText(_translate("Form", "Time"))
        self.spnUpdatePeriod.setSuffix(_translate("Form", " "))
        self.lblRefresh_3.setText(_translate("Form", "Scale:"))
        self.comboBox_2.setItemText(0, _translate("Form", "p (10^-12 pico)"))
        self.comboBox_2.setItemText(1, _translate("Form", "n (10^-9 nano)"))
        self.comboBox_2.setItemText(2, _translate("Form", "u (10^6 micro)"))
        self.comboBox_2.setItemText(3, _translate("Form", "m (10^-3 milli)"))
        self.comboBox_2.setItemText(4, _translate("Form", "E  (10^0 )"))
        self.comboBox_2.setItemText(5, _translate("Form", "K (10^3  Kilo)"))
        self.comboBox_2.setItemText(6, _translate("Form", "M (10^6 Mega)"))
        self.comboBox_2.setItemText(7, _translate("Form", "G (10^9 Giga)"))
        self.comboBox_2.setItemText(8, _translate("Form", "T (10^12 Tera)"))
        self.lblRefresh_2.setText(_translate("Form", "Unit"))
        self.comboBox.setItemText(0, _translate("Form", "Hertz(Hz) : Frequency (f)"))
        self.comboBox.setItemText(1, _translate("Form", "Seconds(S): Period (T)"))
        self.toolButton.setText(_translate("Form", "..."))
        self.pushButton.setText(_translate("Form", "PushButton"))
