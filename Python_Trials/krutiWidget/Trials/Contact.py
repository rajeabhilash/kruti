# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Contact.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 250)
        self.Panel = QtWidgets.QWidget(Form)
        self.Panel.setGeometry(QtCore.QRect(0, 0, 500, 250))
        self.Panel.setStyleSheet("#Panel\n"
"{\n"
"background-color: #24292E;\n"
"border: 2px solid #24292E;\n"
"border-radius:10px;\n"
"}")
        self.Panel.setObjectName("Panel")
        self.Avatar = QtWidgets.QLabel(self.Panel)
        self.Avatar.setGeometry(QtCore.QRect(2, 2, 496, 246))
        self.Avatar.setStyleSheet("#Avatar\n"
"{\n"
"background-image: url(:/icons/ABHI_FIVE.jpg);\n"
"background-repeat: none;\n"
"background-position: center;\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-radius: 15px;\n"
"}")
        self.Avatar.setText("")
        self.Avatar.setObjectName("Avatar")
        self.infoPanel = QtWidgets.QWidget(self.Panel)
        self.infoPanel.setGeometry(QtCore.QRect(0, 135, 500, 115))
        self.infoPanel.setStyleSheet("#infoPanel{\n"
"border: 0px solid rgba(0,0,0,0);\n"
"border-top: 2px solid rgba(0,0,0,200);\n"
"border-radius: 0px;\n"
"background-color: rgba(0,0,0,135);\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"}")
        self.infoPanel.setObjectName("infoPanel")
        self.Name = QtWidgets.QLabel(self.infoPanel)
        self.Name.setGeometry(QtCore.QRect(20, 5, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Name.setFont(font)
        self.Name.setStyleSheet("color: #FCFCFC;\n"
"text-transform: uppercase;")
        self.Name.setObjectName("Name")
        self.Mobile = QtWidgets.QLabel(self.infoPanel)
        self.Mobile.setGeometry(QtCore.QRect(20, 40, 121, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Mobile.setFont(font)
        self.Mobile.setStyleSheet("color: #FCFCFC;\n"
"font: 12pt \"Roboto Thin\";")
        self.Mobile.setObjectName("Mobile")
        self.Email = QtWidgets.QLabel(self.infoPanel)
        self.Email.setGeometry(QtCore.QRect(150, 40, 331, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Email.setFont(font)
        self.Email.setStyleSheet("color: #FCFCFC;\n"
"font: 12pt \"Roboto Thin\";")
        self.Email.setObjectName("Email")
        self.Sep_ = QtWidgets.QWidget(self.infoPanel)
        self.Sep_.setGeometry(QtCore.QRect(140, 50, 2, 15))
        self.Sep_.setStyleSheet("background-color: #FCFCFC;\n"
"border: 0px;")
        self.Sep_.setObjectName("Sep_")
        self.View = QtWidgets.QPushButton(self.infoPanel)
        self.View.setGeometry(QtCore.QRect(20, 70, 90, 35))
        font = QtGui.QFont()
        font.setFamily("Caviar Dreams")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.View.setFont(font)
        self.View.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.View.setStyleSheet("#View\n"
"{\n"
"    background-color: rgba(0,0,0,0);\n"
"    color: #FCFCFC;\n"
"    border: 0px;\n"
"    border-left: 4px solid #FCFCFC;\n"
"    border-top: 1px solid #FCFCFC;\n"
"    border-right: 1px solid #FCFCFC;\n"
"    border-bottom: 1px solid #FCFCFC;\n"
"}\n"
"#View:hover{\n"
"    border-left: 4px solid #ffff00;\n"
"}")
        self.View.setObjectName("View")
        self.Edit = QtWidgets.QPushButton(self.infoPanel)
        self.Edit.setGeometry(QtCore.QRect(115, 70, 90, 35))
        font = QtGui.QFont()
        font.setFamily("Caviar Dreams")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Edit.setFont(font)
        self.Edit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Edit.setStyleSheet("#Edit\n"
"{\n"
"    background-color: rgba(0,0,0,0);\n"
"    color: #FCFCFC;\n"
"    border: 0px;\n"
"    border-left: 4px solid #FCFCFC;\n"
"    border-top: 1px solid #FCFCFC;\n"
"    border-right: 1px solid #FCFCFC;\n"
"    border-bottom: 1px solid #FCFCFC;\n"
"}\n"
"#Edit:hover{\n"
"    border-left: 4px solid #00ffff;\n"
"}")
        self.Edit.setObjectName("Edit")
        self.Delete = QtWidgets.QPushButton(self.infoPanel)
        self.Delete.setGeometry(QtCore.QRect(210, 70, 90, 35))
        font = QtGui.QFont()
        font.setFamily("Caviar Dreams")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Delete.setFont(font)
        self.Delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Delete.setStyleSheet("#Delete\n"
"{\n"
"    background-color: rgba(0,0,0,0);\n"
"    color: #FCFCFC;\n"
"    border: 0px;\n"
"    border-left: 4px solid #FCFCFC;\n"
"    border-top: 1px solid #FCFCFC;\n"
"    border-right: 1px solid #FCFCFC;\n"
"    border-bottom: 1px solid #FCFCFC;\n"
"}\n"
"#Delete:hover{\n"
"    border-left: 4px solid #ff00ff;\n"
"}")
        self.Delete.setObjectName("Delete")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Name.setText(_translate("Form", "Raje Abhilash Mohite"))
        self.Mobile.setText(_translate("Form", "8378881434"))
        self.Email.setText(_translate("Form", "rajeabhilashmohite@gmail.com"))
        self.View.setText(_translate("Form", "View"))
        self.Edit.setText(_translate("Form", "Edit"))
        self.Delete.setText(_translate("Form", "Delete"))

import all_resource_rc
