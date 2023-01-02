from PyQt5 import QtCore, QtGui, QtWidgets
from win32com import client

class Ui_aboutWidget(QtWidgets.QWidget):

    aboutClose = QtCore.pyqtSignal()

    def __init__(self,parent):
        super().__init__(parent)
        self.sayIt = client.Dispatch('SAPI.SpVoice')
        aboutWidget = QtWidgets.QWidget(self)
        aboutWidget.setObjectName("aboutWidget")
        aboutWidget.resize(1290, 750)
        font = QtGui.QFont()
        font.setFamily("Caviar Dreams")
        aboutWidget.setFont(font)
        aboutWidget.setStyleSheet("#aboutWidget\n"
                                  "{\n"
                                  "background-color:#FCFCFC;\n"
                                  "border: 2px solid #24292E;\n"
                                  "border-radius: 25px;\n"
                                  "}")
        self.mainLogo = QtWidgets.QLabel(aboutWidget)
        self.mainLogo.setGeometry(QtCore.QRect(30, 50, 475, 650))
        self.mainLogo.setStyleSheet("#mainLogo{\n"
                                    "border-image: url(:/images/HD_ICON.png);\n"
                                    "}")
        self.mainLogo.setText("")
        self.mainLogo.setObjectName("mainLogo")
        self.aboutHead = QtWidgets.QLabel(aboutWidget)
        self.aboutHead.setGeometry(QtCore.QRect(520, 50, 690, 50))
        font = QtGui.QFont()
        font.setFamily("Caviar Dreams")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.aboutHead.setFont(font)
        self.aboutHead.setStyleSheet("#aboutHead\n"
                                     "{\n"
                                     "    background-color: #24292E;\n"
                                     "    color:#FCFCFC;\n"
                                     "    padding-left: 15px;\n"
                                     "    border: 2px solid #24292E;\n"
                                     "    border-top-left-radius: 10px;\n"
                                     "}")
        self.aboutHead.setObjectName("aboutHead")
        self.exitAbout = QtWidgets.QPushButton(aboutWidget)
        self.exitAbout.setGeometry(QtCore.QRect(1210, 50, 50, 52))
        font = QtGui.QFont()
        font.setFamily("Caviar Dreams")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.exitAbout.setFont(font)
        self.exitAbout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitAbout.setStyleSheet("#exitAbout\n"
                                     "{\n"
                                     "    background-color: #24292E;\n"
                                     "    color:#FCFCFC;\n"
                                     "    border: 2px solid #24292E;\n"
                                     "    border-top-right-radius: 10px;\n"
                                     "    border-left: 2px solid #FCFCFC;\n"
                                     "}\n"
                                     "#exitAbout:hover\n"
                                     "{\n"
                                     "    background-color:rgb(255,0,0);\n"
                                     "    color: #FCFCFC;\n"
                                     "    border: 0px\n"
                                     "}")
        self.exitAbout.setObjectName("exitAbout")
        self.aboutDetailsWid = QtWidgets.QWidget(aboutWidget)
        self.aboutDetailsWid.setGeometry(QtCore.QRect(520, 100, 739, 600))
        self.aboutDetailsWid.setStyleSheet("#aboutDetailsWid\n"
                                           "{\n"
                                           "    border: 2px solid #24292E;\n"
                                           "    border-bottom-left-radius: 10px;\n"
                                           "    border-bottom-right-radius: 10px;\n"
                                           "}")
        self.aboutDetailsWid.setObjectName("aboutDetailsWid")
        self.aboutText = QtWidgets.QLabel(self.aboutDetailsWid)
        self.aboutText.setGeometry(QtCore.QRect(10, 10, 715, 241))
        font = QtGui.QFont()
        font.setFamily("Caviar Dreams")
        font.setPointSize(12)
        self.aboutText.setFont(font)
        self.aboutText.setStyleSheet("#aboutText\n"
                                     "{\n"
                                     "    color: #24292E;\n"
                                     "}")
        self.aboutText.setFrameShadow(QtWidgets.QFrame.Plain)
        self.aboutText.setLineWidth(1)
        self.aboutText.setMidLineWidth(0)
        self.aboutText.setTextFormat(QtCore.Qt.AutoText)
        self.aboutText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.aboutText.setWordWrap(True)
        self.aboutText.setObjectName("aboutText")
        self.sep_1 = QtWidgets.QLabel(self.aboutDetailsWid)
        self.sep_1.setGeometry(QtCore.QRect(0, 310, 739, 2))
        self.sep_1.setStyleSheet("background-color: #24292E;\n"
                                 "border: 2px;\n"
                                 "border-radius: 2px;")
        self.sep_1.setText("")
        self.sep_1.setObjectName("sep_1")
        self.abhiAvatar = QtWidgets.QLabel(self.aboutDetailsWid)
        self.abhiAvatar.setGeometry(QtCore.QRect(600, 340, 100, 100))
        self.abhiAvatar.setStyleSheet("border-image: url(:/images/ABHI.png);")
        self.abhiAvatar.setText("")
        self.abhiAvatar.setObjectName("abhiAvatar")
        self.shreyaAvatar = QtWidgets.QLabel(self.aboutDetailsWid)
        self.shreyaAvatar.setGeometry(QtCore.QRect(40, 480, 100, 100))
        self.shreyaAvatar.setStyleSheet("border-image: url(:/images/SHREYA.png);")
        self.shreyaAvatar.setText("")
        self.shreyaAvatar.setObjectName("shreyaAvatar")
        self.label_3 = QtWidgets.QLabel(self.aboutDetailsWid)
        self.label_3.setGeometry(QtCore.QRect(0, 390, 739, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: #24292E;\n"
                                   "color: #FCFCFC;\n"
                                   "padding-right: 150px;\n"
                                   "text-transform:uppercase;\n"
                                   "font-family: \"Roboto Thin\"")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.aboutDetailsWid)
        self.label_4.setGeometry(QtCore.QRect(0, 530, 739, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: #24292E;\n"
                                   "color: #FCFCFC;\n"
                                   "padding-left: 150px;\n"
                                   "text-transform:uppercase;\n"
                                   "font-family: \"Roboto Thin\"")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.aboutDetailsWid)
        self.label.setGeometry(QtCore.QRect(-10, 345, 591, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #24292E;\n"
                                 "text-transform:uppercase;")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.aboutDetailsWid)
        self.label_2.setGeometry(QtCore.QRect(150, 490, 341, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #24292E;\n"
                                   "text-transform:uppercase;")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.aboutDetailsWid)
        self.label_5.setGeometry(QtCore.QRect(120, 275, 511, 35))
        font = QtGui.QFont()
        font.setFamily("Caviar Dreams")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:#FCFCFC;\n"
                                   "background-color: #24292E;\n"
                                   "border:2px solid #24292E;\n"
                                   "border-top-right-radius: 5px;\n"
                                   "border-top-left-radius: 5px;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.aboutText.raise_()
        self.sep_1.raise_()
        self.label_3.raise_()
        self.abhiAvatar.raise_()
        self.label_4.raise_()
        self.shreyaAvatar.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.retranslateUi(aboutWidget)
        self.exitAbout.clicked.connect(self.exitEvent)
        self.setWindowIcon(QtGui.QIcon('ICON.png'))
        self.setWindowTitle("About Kruti")
        self.aboutAnimTwo = QtCore.QPropertyAnimation(self, b'geometry')
        self.aboutAnimTwo.setStartValue(QtCore.QRect(300, 150, 1425, 750))
        self.aboutAnimTwo.setEndValue(QtCore.QRect(300, 910, 1425, 0))
        self.aboutAnimTwo.setDuration(1500)
        self.aboutAnimTwo.setEasingCurve(QtCore.QEasingCurve.OutExpo)
        self.aboutAnimTwo.finished.connect(self.hide)
        QtCore.QMetaObject.connectSlotsByName(aboutWidget)

    def exitEvent(self):
        #self.sayIt.Speak("Thanks for your interest in Kruti.")
        self.aboutAnimTwo.start()
        self.aboutClose.emit()

    def sayAboutKruti(self):
        self.sayIt.Speak("Hi, It's Kruti - An Artificial Intelligent System for Everyone,"
                         "Invented by Raje Abhilash Mohite.")

    def keyPressEvent(self, event):
        if event.key()==QtCore.Qt.Key_Escape:
            self.aboutAnimTwo.start()
            self.aboutClose.emit()
            self.sayIt.Speak("Thanks for your interest in Kruti.")

    def retranslateUi(self, aboutWidget):
        _translate = QtCore.QCoreApplication.translate
        aboutWidget.setWindowTitle(_translate("aboutWidget", "Form"))
        self.aboutHead.setText(_translate("aboutWidget", "ABOUT KRUTI"))
        self.exitAbout.setText(_translate("aboutWidget", "X"))
        self.aboutText.setText(_translate("aboutWidget", "<html><head/><body><p><span style=\" font-weight:600;\">Kruti</span> is an <span style=\" font-weight:600;\">Artificial Intelligent System</span> specially designed for the Everyone who comes in touch with 21<span style=\" vertical-align:super;\">st</span> centuries Technology, That is Computer.</p><p><span style=\" text-decoration: underline;\">Computers are not same as it was before</span>. It has been changed so much that it can now <span style=\" font-weight:600;\">learn and think</span> on <span style=\" font-weight:600;\">what have learned</span>, too Amazing...!</p><p>Thus <span style=\" font-weight:600;\">Kruti</span> provides all the Toolset of Modern Computer Technology and let the user modify them as they want. <span style=\" font-weight:600;\">Kruti</span> can be very handy tool for Professional users,Home users or even for Students.</p><p>For More Details,  Just use it and you will know Everything.!</p></body></html>"))
        self.label_3.setText(_translate("aboutWidget", "Author, Inventor, UI & UX Designer"))
        self.label_4.setText(_translate("aboutWidget", "Developer and Designer"))
        self.label.setText(_translate("aboutWidget", "Raje Abhilash Mohite"))
        self.label_2.setText(_translate("aboutWidget", "Shreya Devkate"))
        self.label_5.setText(_translate("aboutWidget", "A VASHISHTHA ENTERPISE PRODUCT"))

import resource_list_rc
