# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtdict.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(366, 137)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setAutoFillBackground(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.treeWidget = QtWidgets.QTreeWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.treeWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.treeWidget.setLineWidth(0)
        self.treeWidget.setMidLineWidth(1)
        self.treeWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.treeWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.treeWidget.setAutoScroll(False)
        self.treeWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.SelectedClicked)
        self.treeWidget.setProperty("showDropIndicator", False)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setObjectName("treeWidget")
        self.verticalLayout_4.addWidget(self.treeWidget)
        self.verticalLayout.addWidget(self.groupBox)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.kcollapsiblegroupbox = KCollapsibleGroupBox(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kcollapsiblegroupbox.sizePolicy().hasHeightForWidth())
        self.kcollapsiblegroupbox.setSizePolicy(sizePolicy)
        self.kcollapsiblegroupbox.setAutoFillBackground(True)
        self.kcollapsiblegroupbox.setExpanded(False)
        self.kcollapsiblegroupbox.setObjectName("kcollapsiblegroupbox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.kcollapsiblegroupbox)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.kcollapsiblegroupbox_3 = KCollapsibleGroupBox(self.kcollapsiblegroupbox)
        self.kcollapsiblegroupbox_3.setExpanded(False)
        self.kcollapsiblegroupbox_3.setObjectName("kcollapsiblegroupbox_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.kcollapsiblegroupbox_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ktreewidgetsearchline = KTreeWidgetSearchLine(self.kcollapsiblegroupbox_3)
        self.ktreewidgetsearchline.setObjectName("ktreewidgetsearchline")
        self.horizontalLayout_3.addWidget(self.ktreewidgetsearchline)
        self.ktreewidgetsearchlinewidget = KTreeWidgetSearchLineWidget(self.kcollapsiblegroupbox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ktreewidgetsearchlinewidget.sizePolicy().hasHeightForWidth())
        self.ktreewidgetsearchlinewidget.setSizePolicy(sizePolicy)
        self.ktreewidgetsearchlinewidget.setObjectName("ktreewidgetsearchlinewidget")
        self.horizontalLayout_3.addWidget(self.ktreewidgetsearchlinewidget)
        self.verticalLayout_3.addWidget(self.kcollapsiblegroupbox_3)
        self.kcollapsiblegroupbox_4 = KCollapsibleGroupBox(self.kcollapsiblegroupbox)
        self.kcollapsiblegroupbox_4.setAutoFillBackground(False)
        self.kcollapsiblegroupbox_4.setExpanded(False)
        self.kcollapsiblegroupbox_4.setObjectName("kcollapsiblegroupbox_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.kcollapsiblegroupbox_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_3 = QtWidgets.QWidget(self.kcollapsiblegroupbox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_5.addWidget(self.widget_3)
        self.kcollapsiblegroupbox_2 = KCollapsibleGroupBox(self.kcollapsiblegroupbox_4)
        self.kcollapsiblegroupbox_2.setObjectName("kcollapsiblegroupbox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.kcollapsiblegroupbox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.kcollapsiblegroupbox_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.kpluralhandlingspinbox = KPluralHandlingSpinBox(self.kcollapsiblegroupbox_2)
        self.kpluralhandlingspinbox.setDisplayIntegerBase(10)
        self.kpluralhandlingspinbox.setObjectName("kpluralhandlingspinbox")
        self.horizontalLayout_2.addWidget(self.kpluralhandlingspinbox)
        self.kcombobox = KComboBox(self.kcollapsiblegroupbox_2)
        self.kcombobox.setObjectName("kcombobox")
        self.horizontalLayout_2.addWidget(self.kcombobox)
        self.verticalLayout_5.addWidget(self.kcollapsiblegroupbox_2)
        self.verticalLayout_3.addWidget(self.kcollapsiblegroupbox_4)
        self.groupBox_2 = QtWidgets.QGroupBox(self.kcollapsiblegroupbox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.klineedit = KLineEdit(self.groupBox_2)
        self.klineedit.setReadOnly(True)
        self.klineedit.setObjectName("klineedit")
        self.gridLayout_2.addWidget(self.klineedit, 2, 6, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.klineedit_2 = KLineEdit(self.groupBox_2)
        self.klineedit_2.setReadOnly(True)
        self.klineedit_2.setUrlDropsEnabled(False)
        self.klineedit_2.setObjectName("klineedit_2")
        self.gridLayout_2.addWidget(self.klineedit_2, 2, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 4, 7, 1, 1)
        self.klineedit_3 = KLineEdit(self.groupBox_2)
        self.klineedit_3.setReadOnly(True)
        self.klineedit_3.setObjectName("klineedit_3")
        self.gridLayout_2.addWidget(self.klineedit_3, 4, 4, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 5, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.verticalLayout_2.addWidget(self.kcollapsiblegroupbox)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_5 = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.verticalLayout.addWidget(self.widget_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QtpyDictator"))
        self.treeWidget.headerItem().setText(0, _translate("Form", "Key"))
        self.treeWidget.headerItem().setText(1, _translate("Form", "Value"))
        self.kcollapsiblegroupbox.setAccessibleName(_translate("Form", "Toolbox"))
        self.kcollapsiblegroupbox.setTitle(_translate("Form", "Toolbox"))
        self.kcollapsiblegroupbox_3.setTitle(_translate("Form", "Search"))
        self.kcollapsiblegroupbox_4.setTitle(_translate("Form", "Reloading"))
        self.checkBox.setText(_translate("Form", "Auto"))
        self.pushButton_3.setText(_translate("Form", "Reload"))
        self.kcollapsiblegroupbox_2.setTitle(_translate("Form", "Timing :"))
        self.label.setText(_translate("Form", "Frequency :"))
        self.kpluralhandlingspinbox.setSuffix(_translate("Form", " ms"))
        self.groupBox_2.setTitle(_translate("Form", "Data"))
        self.label_4.setText(_translate("Form", "Path:"))
        self.label_3.setText(_translate("Form", "Key:"))
        self.pushButton.setText(_translate("Form", "Copy"))
        self.label_2.setText(_translate("Form", "Val:"))
        self.pushButton_2.setText(_translate("Form", "About"))
        self.pushButton_4.setText(_translate("Form", "Exit"))
from kcollapsiblegroupbox import KCollapsibleGroupBox
from kcombobox import KComboBox
from klineedit import KLineEdit
from kpluralhandlingspinbox import KPluralHandlingSpinBox
from ktreewidgetsearchline import KTreeWidgetSearchLine
from ktreewidgetsearchlinewidget import KTreeWidgetSearchLineWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
