# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ContactDock.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Contact(object):
    def setupUi(self, Contact):
        Contact.setObjectName("Contact")
        Contact.resize(450, 150)
        Contact.setStyleSheet("#Contact\n"
"{\n"
"    border: 2px solid #24292E;\n"
"    border-radius : 10px;\n"
"}")
        self.ControlsPane = QtWidgets.QWidget(Contact)
        self.ControlsPane.setGeometry(QtCore.QRect(150, 0, 301, 50))
        self.ControlsPane.setObjectName("ControlsPane")
        self.contactDelete = QtWidgets.QPushButton(self.ControlsPane)
        self.contactDelete.setGeometry(QtCore.QRect(200, 0, 100, 50))
        self.contactDelete.setObjectName("contactDelete")
        self.contactEdit = QtWidgets.QPushButton(self.ControlsPane)
        self.contactEdit.setGeometry(QtCore.QRect(100, 0, 100, 50))
        self.contactEdit.setObjectName("contactEdit")
        self.contactMessage = QtWidgets.QPushButton(self.ControlsPane)
        self.contactMessage.setGeometry(QtCore.QRect(0, 0, 100, 50))
        self.contactMessage.setObjectName("contactMessage")
        self.Avatar = QtWidgets.QPushButton(Contact)
        self.Avatar.setGeometry(QtCore.QRect(0, 0, 150, 150))
        self.Avatar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("boy.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Avatar.setIcon(icon)
        self.Avatar.setIconSize(QtCore.QSize(100, 100))
        self.Avatar.setObjectName("Avatar")
        self.contactName = QtWidgets.QLabel(Contact)
        self.contactName.setGeometry(QtCore.QRect(160, 70, 241, 30))
        font = QtGui.QFont()
        font.setFamily("Caviar Dreams")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.contactName.setFont(font)
        self.contactName.setObjectName("contactName")
        self.contactNumber = QtWidgets.QLabel(Contact)
        self.contactNumber.setGeometry(QtCore.QRect(160, 105, 151, 30))
        font = QtGui.QFont()
        font.setFamily("Caviar Dreams")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.contactNumber.setFont(font)
        self.contactNumber.setObjectName("contactNumber")

        self.retranslateUi(Contact)
        QtCore.QMetaObject.connectSlotsByName(Contact)

    def retranslateUi(self, Contact):
        _translate = QtCore.QCoreApplication.translate
        Contact.setWindowTitle(_translate("Contact", "Form"))
        self.contactDelete.setText(_translate("Contact", "Delete"))
        self.contactEdit.setText(_translate("Contact", "Edit"))
        self.contactMessage.setText(_translate("Contact", "Message"))
        self.contactName.setText(_translate("Contact", "Raje Abhilash"))
        self.contactNumber.setText(_translate("Contact", "8378881434"))

