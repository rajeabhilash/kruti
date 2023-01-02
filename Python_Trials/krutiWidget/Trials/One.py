# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ContactBottom.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 50)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1920, 50))
        self.widget.setStyleSheet("background-color:  #1A1A1D; border: 2px solid #24292E")
        self.widget.setObjectName("widget")
        self.det_Lab01 = QtWidgets.QLabel(self.widget)
        self.det_Lab01.setGeometry(QtCore.QRect(30, 5, 141, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(16)
        self.det_Lab01.setFont(font)
        self.det_Lab01.setStyleSheet("color: #fcfcfc;\n"
"border: 0px;")
        self.det_Lab01.setObjectName("det_Lab01")
        self.det_Lab01_2 = QtWidgets.QLabel(self.widget)
        self.det_Lab01_2.setGeometry(QtCore.QRect(165, 5, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(16)
        self.det_Lab01_2.setFont(font)
        self.det_Lab01_2.setStyleSheet("color: #fcfcfc;\n"
"border: 0px;")
        self.det_Lab01_2.setObjectName("det_Lab01_2")
        self.Sep00 = QtWidgets.QWidget(self.widget)
        self.Sep00.setGeometry(QtCore.QRect(1465, 5, 3, 37))
        self.Sep00.setStyleSheet("background-color: #FCFCFC;\n"
"border: 0px;")
        self.Sep00.setObjectName("Sep00")
        self.det_Lab01_3 = QtWidgets.QLabel(self.widget)
        self.det_Lab01_3.setGeometry(QtCore.QRect(1280, 5, 141, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(16)
        self.det_Lab01_3.setFont(font)
        self.det_Lab01_3.setStyleSheet("color: #fcfcfc;\n"
"border: 0px;")
        self.det_Lab01_3.setObjectName("det_Lab01_3")
        self.tolFamily = QtWidgets.QLabel(self.widget)
        self.tolFamily.setGeometry(QtCore.QRect(1385, 5, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(16)
        self.tolFamily.setFont(font)
        self.tolFamily.setStyleSheet("color: #fcfcfc;\n"
"border: 0px;")
        self.tolFamily.setObjectName("tolFamily")
        self.totFriends = QtWidgets.QLabel(self.widget)
        self.totFriends.setGeometry(QtCore.QRect(1595, 5, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(16)
        self.totFriends.setFont(font)
        self.totFriends.setStyleSheet("color: #fcfcfc;\n"
"border: 0px;")
        self.totFriends.setObjectName("totFriends")
        self.det_Lab01_6 = QtWidgets.QLabel(self.widget)
        self.det_Lab01_6.setGeometry(QtCore.QRect(1480, 5, 141, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(16)
        self.det_Lab01_6.setFont(font)
        self.det_Lab01_6.setStyleSheet("color: #fcfcfc;\n"
"border: 0px;")
        self.det_Lab01_6.setObjectName("det_Lab01_6")
        self.Sep00_2 = QtWidgets.QWidget(self.widget)
        self.Sep00_2.setGeometry(QtCore.QRect(1685, 5, 3, 37))
        self.Sep00_2.setStyleSheet("background-color: #FCFCFC;\n"
"border: 0px;")
        self.Sep00_2.setObjectName("Sep00_2")
        self.totOthers = QtWidgets.QLabel(self.widget)
        self.totOthers.setGeometry(QtCore.QRect(1810, 5, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(16)
        self.totOthers.setFont(font)
        self.totOthers.setStyleSheet("color: #fcfcfc;\n"
"border: 0px;")
        self.totOthers.setObjectName("totOthers")
        self.det_Lab01_8 = QtWidgets.QLabel(self.widget)
        self.det_Lab01_8.setGeometry(QtCore.QRect(1700, 5, 151, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(16)
        self.det_Lab01_8.setFont(font)
        self.det_Lab01_8.setStyleSheet("color: #fcfcfc;\n"
"border: 0px;")
        self.det_Lab01_8.setObjectName("det_Lab01_8")
        self.det_Lab01.raise_()
        self.det_Lab01_2.raise_()
        self.det_Lab01_3.raise_()
        self.tolFamily.raise_()
        self.Sep00.raise_()
        self.det_Lab01_6.raise_()
        self.totFriends.raise_()
        self.Sep00_2.raise_()
        self.det_Lab01_8.raise_()
        self.totOthers.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.det_Lab01.setText(_translate("Form", "Contacts : "))
        self.det_Lab01_2.setText(_translate("Form", "250"))
        self.det_Lab01_3.setText(_translate("Form", "Family :"))
        self.tolFamily.setText(_translate("Form", "25"))
        self.totFriends.setText(_translate("Form", "150"))
        self.det_Lab01_6.setText(_translate("Form", "Friends : "))
        self.totOthers.setText(_translate("Form", "50"))
        self.det_Lab01_8.setText(_translate("Form", "Others : "))

