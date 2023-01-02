# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SampleCheck.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1175, 725)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(30, 150, 821, 141))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 81, 821, 51))
        font = QtGui.QFont()
        
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 310, 821, 87))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.lineEdit.setFocus(QtCore.Qt.OtherFocusReason)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "QLine Edit"))


if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wid = Ui_Form()
    window = QtWidgets.QWidget()
    wid.setupUi(window)
    window.show()
    sys.exit(app.exec_())
