# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SpeedApplyRedeem_UseVolume.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dig_UseCode(object):
    def setupUi(self, Dig_UseCode):
        Dig_UseCode.setObjectName(_fromUtf8("Dig_UseCode"))
        Dig_UseCode.resize(251, 345)
        self.verticalLayout = QtGui.QVBoxLayout(Dig_UseCode)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pb_useCode = QtGui.QPushButton(Dig_UseCode)
        self.pb_useCode.setMaximumSize(QtCore.QSize(120, 40))
        self.pb_useCode.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pb_useCode.setFont(font)
        self.pb_useCode.setObjectName(_fromUtf8("pb_useCode"))
        self.verticalLayout.addWidget(self.pb_useCode)
        self.line = QtGui.QFrame(Dig_UseCode)
        self.line.setMinimumSize(QtCore.QSize(0, 15))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.l_orderVolume3 = QtGui.QLabel(Dig_UseCode)
        self.l_orderVolume3.setObjectName(_fromUtf8("l_orderVolume3"))
        self.gridLayout.addWidget(self.l_orderVolume3, 4, 1, 1, 1)
        self.l_orderVolume1 = QtGui.QLabel(Dig_UseCode)
        self.l_orderVolume1.setObjectName(_fromUtf8("l_orderVolume1"))
        self.gridLayout.addWidget(self.l_orderVolume1, 0, 1, 1, 1)
        self.l_orderVolume5 = QtGui.QLabel(Dig_UseCode)
        self.l_orderVolume5.setObjectName(_fromUtf8("l_orderVolume5"))
        self.gridLayout.addWidget(self.l_orderVolume5, 8, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.le_orderVolume4 = QtGui.QLineEdit(Dig_UseCode)
        self.le_orderVolume4.setObjectName(_fromUtf8("le_orderVolume4"))
        self.gridLayout.addWidget(self.le_orderVolume4, 6, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.le_orderVolume2 = QtGui.QLineEdit(Dig_UseCode)
        self.le_orderVolume2.setObjectName(_fromUtf8("le_orderVolume2"))
        self.gridLayout.addWidget(self.le_orderVolume2, 2, 2, 1, 1)
        self.le_orderVolume5 = QtGui.QLineEdit(Dig_UseCode)
        self.le_orderVolume5.setObjectName(_fromUtf8("le_orderVolume5"))
        self.gridLayout.addWidget(self.le_orderVolume5, 8, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 1, 1, 1)
        self.le_orderVolume1 = QtGui.QLineEdit(Dig_UseCode)
        self.le_orderVolume1.setObjectName(_fromUtf8("le_orderVolume1"))
        self.gridLayout.addWidget(self.le_orderVolume1, 0, 2, 1, 1)
        self.l_orderVolume2 = QtGui.QLabel(Dig_UseCode)
        self.l_orderVolume2.setObjectName(_fromUtf8("l_orderVolume2"))
        self.gridLayout.addWidget(self.l_orderVolume2, 2, 1, 1, 1)
        self.le_orderVolume3 = QtGui.QLineEdit(Dig_UseCode)
        self.le_orderVolume3.setObjectName(_fromUtf8("le_orderVolume3"))
        self.gridLayout.addWidget(self.le_orderVolume3, 4, 2, 1, 1)
        self.l_orderVolume4 = QtGui.QLabel(Dig_UseCode)
        self.l_orderVolume4.setObjectName(_fromUtf8("l_orderVolume4"))
        self.gridLayout.addWidget(self.l_orderVolume4, 6, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 7, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line_2 = QtGui.QFrame(Dig_UseCode)
        self.line_2.setMinimumSize(QtCore.QSize(0, 15))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.pb_enter = QtGui.QPushButton(Dig_UseCode)
        self.pb_enter.setObjectName(_fromUtf8("pb_enter"))
        self.horizontalLayout.addWidget(self.pb_enter)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.pb_cancel = QtGui.QPushButton(Dig_UseCode)
        self.pb_cancel.setObjectName(_fromUtf8("pb_cancel"))
        self.horizontalLayout.addWidget(self.pb_cancel)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dig_UseCode)
        QtCore.QMetaObject.connectSlotsByName(Dig_UseCode)

    def retranslateUi(self, Dig_UseCode):
        Dig_UseCode.setWindowTitle(_translate("Dig_UseCode", "Dialog", None))
        self.pb_useCode.setText(_translate("Dig_UseCode", "增加常用数量", None))
        self.l_orderVolume3.setText(_translate("Dig_UseCode", "委托数量3", None))
        self.l_orderVolume1.setText(_translate("Dig_UseCode", "委托数量1", None))
        self.l_orderVolume5.setText(_translate("Dig_UseCode", "委托数量5", None))
        self.l_orderVolume2.setText(_translate("Dig_UseCode", "委托数量2", None))
        self.l_orderVolume4.setText(_translate("Dig_UseCode", "委托数量4", None))
        self.pb_enter.setText(_translate("Dig_UseCode", "确定", None))
        self.pb_cancel.setText(_translate("Dig_UseCode", "取消", None))

