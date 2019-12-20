from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from weather import Weather, Unit
import dateTime as dt
import AboutKruti as abt
import DashUI as dash
import loginCheck as voiceLogin
import resource_list_rc
import sys
import faceRecognitionThread

class Ui_MainWindow(object):

    def __init__(self):
        self.currentLI = 0
        self.dashUI = dash.Dashboard()
        self.deviceWidth = 0; self.deviceHeight = 0
        self.dateTime = dt.dateTime()
        self.MainWindow = QMainWindow()
        self.loc = (18.6276,73.7455)
        #self.weather = Weather(unit = Unit.CELSIUS)
        #self.lookUp = self.weather.lookup_by_latlng(self.loc[0],self.loc[1])
        self.recThread = faceRecognitionThread.Recognise()
        self.vLogin = voiceLogin.Login()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(self.deviceWidth, self.deviceHeight)
        MainWindow.setCursor(QCursor(QtCore.Qt.ArrowCursor))
        self.MainWindow = MainWindow
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ICON.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.about = abt.Ui_aboutWidget(self.MainWindow)
        self.about.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.loginPanel = QtWidgets.QWidget(MainWindow)
        self.loginPanel.setObjectName("loginPanel")
        self.loginPanel.setStyleSheet("#loginPanel{border-image: url(:/images/Back.png);}")
        self.infoBar = QtWidgets.QWidget(self.loginPanel)
        #self.infoBar.setGeometry(QtCore.QRect(-1, 470, 720, 125))
        self.infoBar.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.infoBar.setStyleSheet("#infoBar\n"
                                   "{\n"
                                   "    background-color: #24292E;\n"
                                   "    border : 2px solid rgba(0,0,0,0);\n"
                                   "    border-top-right-radius: 15px;\n"
                                   "    border-bottom-right-radius: 15px; \n"
                                   "}")
        self.infoBar.setObjectName("infoBar")
        self.infoWether = QtWidgets.QLabel(self.infoBar)
        self.infoWether.setGeometry(QtCore.QRect(85, 30, 125, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.infoWether.setFont(font)
        self.infoWether.setStyleSheet("color: #FCFCFC")
        self.infoWether.setObjectName("infoWether")
        self.infoLocation = QtWidgets.QLabel(self.infoBar)
        self.infoLocation.setGeometry(QtCore.QRect(40, 75, 311, 25))
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(12)
        self.infoLocation.setFont(font)
        self.infoLocation.setStyleSheet("color: #FCFCFC;\n"
                                        "text-transform: uppercase;\n"
                                        "font-family : \"Roboto Thin\";")
        self.infoLocation.setObjectName("infoLocation")
        self.sep_1 = QtWidgets.QWidget(self.infoBar)
        self.sep_1.setGeometry(QtCore.QRect(20, 25, 5, 85))
        self.sep_1.setStyleSheet("background-color: #FCFCFC;\n"
                                 "color: #FCFCFC;\n"
                                 "border: 2px solid #FCFCFC;\n"
                                 "border-radius: 1px;")
        self.sep_1.setObjectName("sep_1")
        self.sep_2 = QtWidgets.QWidget(self.infoBar)
        self.sep_2.setGeometry(QtCore.QRect(300, 25, 5, 85))
        self.sep_2.setStyleSheet("background-color: #FCFCFC;\n"
                                 "color: #FCFCFC;\n"
                                 "border: 2px solid #FCFCFC;\n"
                                 "border-radius: 1px;")
        self.sep_2.setObjectName("sep_2")
        self.infoSun = QtWidgets.QLabel(self.infoBar)
        self.infoSun.setGeometry(QtCore.QRect(35, 32, 45, 45))
        self.infoSun.setStyleSheet("border-image: url(:/images/SunL.svg);")
        self.infoSun.setText("")
        self.infoSun.setObjectName("infoSun")
        self.info_Time = QtWidgets.QLabel(self.infoBar)
        self.info_Time.setGeometry(QtCore.QRect(325, 30, 275, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.info_Time.setFont(font)
        self.info_Time.setStyleSheet("color:#FCFCFC")
        self.info_Time.setObjectName("info_Time")
        self.info_Date = QtWidgets.QLabel(self.infoBar)
        self.info_Date.setGeometry(QtCore.QRect(325, 75, 311, 25))
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(12)
        self.info_Date.setFont(font)
        self.info_Date.setStyleSheet("color: #FCFCFC;\n"
                                     "text-transform: uppercase;\n"
                                     "font-family : \"Roboto Thin\";")
        self.info_Date.setObjectName("info_Date")
        self.loginBar = QtWidgets.QWidget(self.loginPanel)
        #self.loginBar.setGeometry(QtCore.QRect(882, 470, 1039, 125))
        self.loginBar.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.loginBar.setStyleSheet("#loginBar\n"
                                    "{\n"
                                    "    background-color: #24292E;\n"
                                    "    border : 2px solid rgba(0,0,0,0);\n"
                                    "    border-top-left-radius: 15px;\n"
                                    "    border-bottom-left-radius: 15px; \n"
                                    "}")
        self.loginBar.setObjectName("loginBar")
        self.voice = QtWidgets.QPushButton(self.loginBar)
        self.voice.setGeometry(QtCore.QRect(55, 25, 80, 80))
        self.voice.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.voice.setObjectName("voice")
        self.voice.setStyleSheet("#voice { background-image: url(:/images/InVoiceL.svg);\n"
                                 "background-color:rgba(0,0,0,0);\n"
                                 "background-position: center;\n"
                                 "background-repeat: repeat-none;\n"
                                 "border: 2px solid #FCFCFC;\n"
                                 "border-radius: 10px;\n}"
                                 "#voice:hover{ background-image: url(:/images/InVoice.svg);\n"
                                 "background-color:#FCFCFC}")
        self.voice.setText("")
        self.face = QtWidgets.QPushButton(self.loginBar)
        self.face.setGeometry(QtCore.QRect(380, 25, 80, 80))
        self.face.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.face.setObjectName("face")
        self.face.setStyleSheet("#face{background-image: url(:/images/InFaceLS.svg);\n"
                                "background-position: center;\n"
                                "background-color:rgba(0,0,0,0);\n"
                                "background-repeat: repeat-none;\n"
                                "border: 2px solid #FCFCFC;\n"
                                "border-radius: 10px;}\n"
                                "#face:hover{ background-image: url(:/images/InFace.svg);\n"
                                "background-color:#FCFCFC;}")
        self.face.setText("")
        self.keyPass = QtWidgets.QPushButton(self.loginBar)
        self.keyPass.setGeometry(QtCore.QRect(150, 25, 80, 80))
        self.keyPass.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.keyPass.setObjectName("keyPass")
        self.keyPass.setStyleSheet("#keyPass{ background-image: url(:/images/InKeyPassL.svg);\n"
                                   "background-position: center;\n"
                                   "background-color:rgba(0,0,0,0);\n"
                                   "background-repeat: repeat-none;\n"
                                   "border: 2px solid #FCFCFC;\n"
                                   "border-radius: 10px;}\n"
                                   "#keyPass:hover{ background-image: url(:/images/InKeyPass.svg);\n"
                                   "background-color: #FCFCFC;}")
        self.keyPass.setText("")
        self.numPass = QtWidgets.QPushButton(self.loginBar)
        self.numPass.setGeometry(QtCore.QRect(245, 25, 80, 80))
        self.numPass.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.numPass.setObjectName("numPass")
        self.numPass.setStyleSheet("#numPass{ background-image: url(:/images/InNumPassL.svg);\n"
                                   "background-position: center;\n"
                                   "background-color:rgba(0,0,0,0);\n"
                                   "background-repeat: repeat-none;\n"
                                   "border: 2px solid #FCFCFC;\n"
                                   "border-radius: 10px;}\n"
                                   "#numPass:hover{ background-image: url(:/images/InNumPass.svg);\n"
                                   "background-color:#FCFCFC;}")
        self.numPass.setText("")

        self.password = QtWidgets.QLineEdit(self.loginBar)
        self.password.setGeometry(475,65,0,40)
        self.password.setFont(QFont("Caviar Dreams",14,QFont.Bold))
        self.password.setPlaceholderText("Type Password, Hit Enter")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet("background-color:rgba(0,0,0,0);"
                                    "color:#FCFCFC;"
                                    "border: 2px solid #24292E;"
                                    "border-bottom: 2px solid #FCFCFC;"
                                    "padding-left: 5px")
        self.pin = QLineEdit(self.loginBar)
        self.pin.setGeometry(475,65,0,40)
        self.pin.setFont(QFont("Caviar Dreams",14,QFont.Bold))
        self.pin.setPlaceholderText("Type Pin, Hit Enter")
        self.pin.setEchoMode(QLineEdit.Password)
        self.pin.setStyleSheet("background-color:rgba(0,0,0,0);"
                                    "color:#FCFCFC;"
                                    "border: 2px solid #24292E;"
                                    "border-bottom: 2px solid #FCFCFC;"
                                    "padding-left: 5px")
        self.sep_5 = QtWidgets.QWidget(self.loginBar)
        self.sep_5.setGeometry(QtCore.QRect(350, 25, 5, 85))
        self.sep_5.setStyleSheet("background-color: #FCFCFC;\n"
                                 "color: #FCFCFC;\n"
                                 "border: 2px solid #FCFCFC;\n"
                                 "border-radius: 1px;")
        self.sep_5.setObjectName("sep_5")
        self.sep_6 = QtWidgets.QWidget(self.loginBar)
        self.sep_6.setGeometry(QtCore.QRect(25, 25, 5, 85))
        self.sep_6.setStyleSheet("background-color: #FCFCFC;\n"
                                 "color: #FCFCFC;\n"
                                 "border: 2px solid #FCFCFC;\n"
                                 "border-radius: 1px;")
        self.sep_6.setObjectName("sep_6")
        self.login_Info = QtWidgets.QLabel(self.loginBar)
        self.login_Info.setGeometry(QtCore.QRect(485, 35, 365, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.login_Info.setFont(font)
        self.login_Info.setStyleSheet("color:#FCFCFC;")
        self.login_Info.setObjectName("login_Info")
        self.login_Info_Details = QtWidgets.QLabel(self.loginBar)
        self.login_Info_Details.setGeometry(QtCore.QRect(480, 60, 0, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(12)
        self.login_Info_Details.setFont(font)
        self.login_Info_Details.setStyleSheet("color:#FCFCFC;\n"
                                              "font-family:\"Roboto Thin\";"
                                              "border: 2px solid #24292E;"
                                              "border-bottom: 2px solid #FCFCFC;")
        self.login_Info_Details.setObjectName("login_Info_Details")
        self.mainLogo = QtWidgets.QPushButton(self.loginPanel)
        #self.mainLogo.setGeometry(QtCore.QRect(727, 415, 145, 195))
        self.mainLogo.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.mainLogo.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.mainLogo.setObjectName("mainLogo")
        self.mainLogo.setStyleSheet("#mainLogo{border-image: url(:/images/REAL_ICON.png);}")
        self.mainLogo.setText("")
        self.sep_3 = QtWidgets.QWidget(self.loginPanel)
        #self.sep_3.setGeometry(QtCore.QRect(35, 55, 5, 75))
        self.sep_3.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.sep_3.setStyleSheet("background-color: #24292E;\n"
                                 "color: #24292E;\n"
                                 "border: 2px solid #24292E;\n"
                                 "border-radius: 1px;")
        self.sep_3.setObjectName("sep_3")
        self.quote_Head = QtWidgets.QLabel(self.loginPanel)
        #self.quote_Head.setGeometry(QtCore.QRect(50, 53, 650, 50))
        self.quote_Head.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.quote_Head.setFont(font)
        self.quote_Head.setStyleSheet("color:#24292E;\n"
                                      "text-transform: uppercase;")
        self.quote_Head.setObjectName("quote_Head")
        self.quote_Author = QtWidgets.QLabel(self.loginPanel)
        #self.quote_Author.setGeometry(QtCore.QRect(50, 100, 311, 25))
        self.quote_Author.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(15)
        self.quote_Author.setFont(font)
        self.quote_Author.setStyleSheet("color: #24292E;\n"
                                        "font-family : \"Roboto Thin\";")
        self.quote_Author.setObjectName("quote_Author")
        self.sep_4 = QtWidgets.QWidget(self.loginPanel)
        self.sep_4.setGeometry(QtCore.QRect(0, 20, 1920, 7))
        self.sep_4.setStyleSheet("background-color: #24292E;\n"
                                 "color: #24292E;")
        self.sep_4.setObjectName("sep_4")
        self.copyright = QtWidgets.QLabel(self.loginPanel)
        #self.copyright.setGeometry(QtCore.QRect(0, 1020, 1920, 45))
        self.copyright.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Caviar Dreams")
        font.setPointSize(14)
        self.copyright.setFont(font)
        self.copyright.setStyleSheet("background-color:#24292E;\n"
                                     "color: #FCFCFC")
        self.copyright.setAlignment(QtCore.Qt.AlignCenter)
        self.copyright.setObjectName("copyright")
        self.closeButton = QPushButton(self.loginPanel)
        self.closeButton.setObjectName("exit")
        self.closeButton.setGeometry(MainWindow.width()-55,5,50,0)
        self.closeButton.setStyleSheet("#exit{ background-color:#24292E;\n"
                                       "color:#FCFCFC;\n"
                                       "border: 2px solid #24292E;\n"
                                       "border-radius: 5px;}\n"
                                       "#exit:hover { background-color:rgb(250,25,25);\n"
                                       "color:#FCFCFC;}"
                                       "#exit:hover .login_Info{color:#24292E;}")
        self.closeButton.setText("X")
        self.closeButton.setFont(QFont("Caviar Dreams",16,QFont.Bold))
        self.colorb = QPushButton(self.loginPanel)
        self.colorb.setGeometry(QRect(0,0,20,20))
        self.closeButton.setCursor(Qt.PointingHandCursor)
        MainWindow.setCentralWidget(self.loginPanel)
        self.retranslateUi(MainWindow)
        self.dateTime.start()
        self.logins = [self.login_Info_Details,self.password,self.pin]
        self.logins[0].setGeometry(475,65,430,40)
        self.currentLI = 0
        self.dateTime.dateTimeChange.connect(self.changeDateTime)
        self.colorb.setText("C")
        self.colorb.setStyleSheet("color:#24292E;border:2px solid #24292E;")
        self.colorb.clicked.connect(self.chg)
        self.closeButton.clicked.connect(self.closeKruti)
        self.voice.clicked.connect(self.keyVoice_Clicked)
        self.keyPass.clicked.connect(self.keyPass_Clicked)
        self.numPass.clicked.connect(self.keyPin_Clicked)
        self.mainLogo.clicked.connect(self.showAbout)
        self.vLogin.keyGenerated.connect(self.showKey)
        self.vLogin.loginSuccess.connect(self.disAnimateAll)
        self.vLogin.loginFailed.connect(self.vLoginFailed)
        self.vLogin.waiting.connect(self.waitAnimate)
        self.vLogin.exceptionOccured.connect(self.vLoginEx)
        self.pin.returnPressed.connect(self.pinEnter)
        self.password.returnPressed.connect(self.passEnter)
        self.voice.setEnabled(False)
        self.keyPass.setEnabled(False)
        self.numPass.setEnabled(False)
        self.animateAll()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.recThread.faceRecognized.connect(self.recognized)
        self.recThread.start()
        self.dashUI.hidden.connect(MainWindow.show)
        self.dashUI.shown.connect(MainWindow.hide)
        self.dashUI.logout.connect(self.closedDashBoard)
        self.sec = 0
        MainWindow.centralWidget().releaseKeyboard()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kruti - An Artificial Intelligent System"))
        #self.infoWether.setText(_translate("MainWindow", "{0}°C".format(self.lookUp.condition.temp)))
        self.infoWether.setText(_translate("MainWindow", "27°C"))
        #self.infoLocation.setText(_translate("MainWindow", "{}".format(self.lookUp.condition.text)))
        self.infoLocation.setText(_translate("MainWindow", "Sunny Sky"))
        self.info_Time.setText(_translate("MainWindow", "09:30:25 AM"))
        self.info_Date.setText(_translate("MainWindow", "Saturday, 1 October 18"))
        self.login_Info.setText(_translate("MainWindow", "FACE RECOGNITION"))
        self.login_Info_Details.setText(_translate("MainWindow", "Clicking on Voice Menu gives you PASSCODE."))
        self.quote_Head.setText(_translate("MainWindow", "Be Odd, to be Number one"))
        self.quote_Author.setText(_translate("MainWindow", "Dr. SEUSS"))
        self.copyright.setText(_translate("MainWindow", "<html><head/><body><p>Copyright © <span style=\" font-weight:600;\">Vashishtha Enterprise</span>, 2018.</p></body></html>"))

    def openDashBoard(self):
        self.login_Info_Details.setText("Login Successfull...!")
        self.dashUI.show()
        self.face.setIcon(QtGui.QIcon())
        self.recThread.isRecognized = True

    def closedDashBoard(self):
        self.recThread.isRecognized = False
        self.login_Info_Details.setStyleSheet("color:#fcfcfc;\n"
                                              "font-family:\"Roboto Thin\";"
                                              "border: 2px solid #24292E;"
                                              "border-bottom: 2px solid #fcfcfc;")
        self.login_Info_Details.setText("Clicking on Voice Menu gives you PASSCODE.")
        self.recThread.start()
        self.animateAll()

    def showKey(self,key):
        self.login_Info_Details.setText("Tell Key of CODE : [ {} ]".format(''.join(map(str,key))))

    def recognized(self,name):
        icon = QtGui.QIcon()
        if name == "Raje Abhilash Mohite":
            icon.addPixmap(QtGui.QPixmap(":/images/ABHI_PI.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        if name == "Shreya Devkate":
            icon.addPixmap(QtGui.QPixmap(":/images/SHREYA_PI.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.face.setIcon(icon)
        self.face.setIconSize(QtCore.QSize(75, 75))
        self.login_Info.setText(name)
        self.voice.setEnabled(True)
        self.numPass.setEnabled(True)
        self.keyPass.setEnabled(True)

    def vLoginFailed(self):
        self.login_Info_Details.setStyleSheet("color:rgb(255,140,0);\n"
                                              "font-family:\"Roboto Thin\";"
                                              "border: 2px solid #24292E;"
                                              "border-bottom: 2px solid rgb(255,140,0);")
        self.login_Info_Details.setText("Passcode not Matched, Please try again.!")

    def vLoginEx(self,exp):
        self.login_Info_Details.setStyleSheet("color:rgb(255,69,0);\n"
                                              "font-family:\"Roboto Thin\";"
                                              "border: 2px solid #24292E;"
                                              "border-bottom: 2px solid rgb(255,69,0);")
        self.login_Info_Details.setText("Something went Wrong...")
        print(exp)

    def passEnter(self):
        print("Enter on Password")
        print(self.password.text())
        if self.login_Info.text()=="Raje Abhilash Mohite":
            if self.password.text()=="His@123":
                self.password.setText("")
                #self.openDashBoard()
                self.disAnimateAll()
            else:
                self.password.setText("")

        if self.login_Info.text()=="Shreya Devkate":
            if self.password.text()=="Her@123":
                self.password.setText("")
                #self.openDashBoard()
                self.disAnimateAll()
            else:
                self.password.setText("")

    def pinEnter(self):
        print("Enter on Pin")
        print(self.pin.text())
        if self.login_Info.text()=="Raje Abhilash Mohite":
            if self.pin.text()=="1434":
                self.pin.setText("")
                #self.openDashBoard()
                self.disAnimateAll()
            else:
                self.pin.setText("")
        if self.login_Info.text()=="Shreya Devkate":
            if self.pin.text()=="2629":
                self.pin.setText("")
                #self.openDashBoard()
                self.disAnimateAll()
            else:
                self.pin.setText("")

    def waitAnimate(self,val):
        otherVal = 0
        if val<9:
            val = '0.{}'.format(val)
        elif val==9:
            val = 1
            otherVal = 1
        self.login_Info_Details.setStyleSheet("color:#FCFCFC;\n"
                                              "font-family:\"Roboto Thin\";"
                                              "border: 2px solid #24292E;"
                                              "border-bottom: 2px solid qlineargradient(spread:pad, x1:{}, y1:0, x2:{}, y2:0, stop:0 #FCFCFC, stop:1 #24292E);".format(otherVal,val))
        if val == 10:
            self.login_Info_Details.setStyleSheet("color:#7CFC00;\n"
                                                  "font-family:\"Roboto Thin\";"
                                                  "border: 2px solid #24292E;"
                                                  "border-bottom: 2px solid #7CFC00")
            if not self.login_Info_Details.text().__contains__("[SPEAK]"):
                self.login_Info_Details.setText(self.login_Info_Details.text()+" [SPEAK]")
        if val == 15:
            self.login_Info_Details.setStyleSheet("color:#FFFF00;\n"
                                                  "font-family:\"Roboto Thin\";"
                                                  "border: 2px solid #24292E;"
                                                  "border-bottom: 2px solid #FFFF00;")
            self.login_Info_Details.setText("Verifying your passcode...")

    def chg(self):
        self.cl = QColorDialog().getColor()
        eff = QGraphicsColorizeEffect()
        eff.setColor(self.cl)
        self.mainLogo.setGraphicsEffect(None)
        self.loginPanel.setGraphicsEffect(eff)

    def showAbout(self):
        self.disAnimateAll()
        # self.about.raise_()
        # self.mainLogo.setGraphicsEffect(None)
        # self.about.setFocus(Qt.ActiveWindowFocusReason)
        # self.blr = QGraphicsBlurEffect()
        # self.loginPanel.setGraphicsEffect(self.blr)
        # self.aboutAnim = QPropertyAnimation(self.blr, b'blurRadius')
        # self.aboutAnim.setStartValue(0)
        # self.aboutAnim.setEndValue(15)
        # self.aboutAnim.setEasingCurve(QEasingCurve.InCurve)
        # self.aboutAnim.start()
        # self.aboutAnimTwo = QPropertyAnimation(self.about, b'geometry')
        # self.aboutAnimTwo.setStartValue(QRect(300,910,1425,0))
        # self.aboutAnimTwo.setEndValue(QRect(300,150,1425,750))
        # self.aboutAnimTwo.setDuration(1500)
        # self.aboutAnimTwo.setEasingCurve(QEasingCurve.OutExpo)
        # self.about.aboutClose.connect(self.restoreBlur)
        # self.aboutAnimTwo.start()
        # #self.aboutAnimTwo.finished.connect(self.about.sayAboutKruti)
        # self.about.show()

    def restoreBlur(self):
        self.blr = QGraphicsBlurEffect()
        self.MainWindow.setFocus(Qt.ActiveWindowFocusReason)
        self.loginPanel.setGraphicsEffect(self.blr)
        self.aboutAnim = QPropertyAnimation(self.blr, b'blurRadius')
        self.aboutAnim.setStartValue(15)
        self.aboutAnim.setEndValue(0)
        self.aboutAnim.setDuration(500)
        self.aboutAnim.setEasingCurve(QEasingCurve.InCurve)
        self.aboutAnim.start()

    def closeKruti(self):
        QApplication.exit()
        self.vLogin.__del__()
        self.recThread.__del__()

    def keyVoice_Clicked(self):
        if not self.currentLI==0:
            self.ChangeLoginOne = QPropertyAnimation(self.logins[self.currentLI],b'geometry')
            self.ChangeLoginTwo = QPropertyAnimation(self.logins[0],b'geometry')
            self.ChangeLoginOne.setDuration(500)
            self.ChangeLoginTwo.setDuration(750)
            self.ChangeLoginOne.setEasingCurve(QEasingCurve.OutCurve)
            self.ChangeLoginTwo.setEasingCurve(QEasingCurve.OutCurve)
            self.ChangeLoginOne.setStartValue(self.logins[self.currentLI].geometry())
            self.ChangeLoginOne.setEndValue(QRect(475,105,300,0))
            self.ChangeLoginTwo.setStartValue(QRect(475,55,430,0))
            self.ChangeLoginTwo.setEndValue(QRect(475,65,430,40))

            self.ChangeLoginOne.start()
            self.ChangeLoginTwo.start()
            self.currentLI = 0
            self.login_Info_Details.setStyleSheet("color:#fcfcfc;\n"
                                                  "font-family:\"Roboto Thin\";"
                                                  "border: 2px solid #24292E;"
                                                  "border-bottom: 2px solid #FCFCFC;")

        self.login_Info_Details.raise_()
        if self.login_Info.text()=="Raje Abhilash Mohite":
            self.vLogin.start()
        if self.login_Info.text()=="Shreya Devkate":
            self.vLogin.start()

    def keyPass_Clicked(self):
        if not self.currentLI==1:
            self.ChangeLoginOne = QPropertyAnimation(self.logins[self.currentLI],b'geometry')
            self.ChangeLoginTwo = QPropertyAnimation(self.logins[1],b'geometry')
            self.ChangeLoginOne.setDuration(500)
            self.ChangeLoginTwo.setDuration(750)
            self.ChangeLoginOne.setEasingCurve(QEasingCurve.OutCurve)
            self.ChangeLoginTwo.setEasingCurve(QEasingCurve.OutCurve)
            if self.currentLI==0:
                self.ChangeLoginOne.setStartValue(self.logins[self.currentLI].geometry())
                self.ChangeLoginOne.setEndValue(QRect(475,55,430,0))
                self.ChangeLoginTwo.setStartValue(QRect(475,105,300,0))
                self.ChangeLoginTwo.setEndValue(QRect(475,65,300,40))
            elif self.currentLI==2:
                self.ChangeLoginOne.setStartValue(self.logins[self.currentLI].geometry())
                self.ChangeLoginOne.setEndValue(QRect(475, 105, 300, 0))
                self.ChangeLoginTwo.setStartValue(QRect(475, 60, 300, 0))
                self.ChangeLoginTwo.setEndValue(QRect(475, 65, 300, 40))

            self.ChangeLoginOne.start()
            self.ChangeLoginTwo.start()
            self.currentLI = 1
            self.password.setFocus(Qt.OtherFocusReason)
            self.password.raise_()


    def keyPin_Clicked(self):
        if not self.currentLI==2:
            self.ChangeLoginOne = QPropertyAnimation(self.logins[self.currentLI],b'geometry')
            self.ChangeLoginTwo = QPropertyAnimation(self.logins[2],b'geometry')
            self.ChangeLoginOne.setDuration(500)
            self.ChangeLoginTwo.setDuration(750)
            self.ChangeLoginOne.setEasingCurve(QEasingCurve.OutCurve)
            self.ChangeLoginTwo.setEasingCurve(QEasingCurve.OutCurve)
            self.ChangeLoginOne.setStartValue(self.logins[self.currentLI].geometry())
            if self.currentLI==0:
                self.ChangeLoginOne.setEndValue(QRect(475,55,430,0))
            elif self.currentLI==1:
                self.ChangeLoginOne.setEndValue(QRect(475,55,300,0))
            self.ChangeLoginTwo.setStartValue(QRect(475,105,300,0))
            self.ChangeLoginTwo.setEndValue(QRect(475,65,300,40))

            self.ChangeLoginOne.start()
            self.ChangeLoginTwo.start()
            self.currentLI = 2
            self.pin.setFocus(Qt.OtherFocusReason)
            self.pin.raise_()

    def changeDateTime(self):
        self.info_Date.setText(QDateTime.currentDateTime().toString("dddd, dd MMMM yy"))
        self.info_Time.setText(QDateTime.currentDateTime().toString("hh:mm:ss A"))

    def animateAll(self):
        blur = QGraphicsBlurEffect()
        self.mainLogo.setGraphicsEffect(blur)
        self.logoAniOne = QPropertyAnimation(self.mainLogo, b'geometry')
        self.logoAniOne.setStartValue(QRect(800,512,0,0))
        self.logoAniOne.setEndValue(QRect(727,415,145,195))
        self.logoAniOne.setDuration(2500)
        self.logoAniOne.setEasingCurve(QEasingCurve.OutCubic)

        self.logoAniTwo = QPropertyAnimation(blur, b'blurRadius')
        self.logoAniTwo.setStartValue(100)
        self.logoAniTwo.setEndValue(0)
        self.logoAniTwo.setDuration(1500)
        self.logoAniTwo.setEasingCurve(QEasingCurve.OutCurve)

        self.loading = QPropertyAnimation(self.sep_4,b'geometry')
        self.loading.setStartValue(QRect(0,20,0,7))
        self.loading.setEndValue(QRect(0,20,self.deviceWidth,7))
        self.loading.setDuration(2000)
        self.loading.setEasingCurve(QEasingCurve.OutQuint)

        self.exitAni = QPropertyAnimation(self.closeButton,b'geometry')
        self.exitAni.setStartValue(QRect(self.deviceWidth-55, 5,50,0))
        self.exitAni.setEndValue(QRect(self.deviceWidth-55, 5, 50, 50))
        self.exitAni.setDuration(1000)
        self.exitAni.setEasingCurve(QEasingCurve.OutBounce)

        self.loadExit = QSequentialAnimationGroup()
        self.loadExit.addAnimation(self.loading)
        self.loadExit.addAnimation(self.exitAni)

        self.qth = QPropertyAnimation(self.quote_Head,b'geometry')
        self.qth.setDuration(5000)
        self.qth.setEasingCurve(QEasingCurve.OutExpo)
        self.qth.setStartValue(QRect(50,53,0,50))
        self.qth.setEndValue(QRect(50,53,500,50))

        self.qta= QPropertyAnimation(self.quote_Author,b'geometry')
        self.qta.setDuration(2500)
        self.qta.setEasingCurve(QEasingCurve.OutExpo)
        self.qta.setStartValue(QRect(50,100,0,25))
        self.qta.setEndValue(QRect(50,100,350,25))

        self.qsep = QPropertyAnimation(self.sep_3,b'geometry')
        self.qsep.setStartValue(QRect(35,55,5,0))
        self.qsep.setEndValue(QRect(35,55,5,80))
        self.qsep.setDuration(2500)
        self.qsep.setEasingCurve(QEasingCurve.OutExpo)

        self.quotAni = QParallelAnimationGroup()
        self.quotAni.addAnimation(self.qth)
        self.quotAni.addAnimation(self.qta)
        self.quotAni.addAnimation(self.qsep)

        self.infoBarAnimation = QPropertyAnimation(self.infoBar, b'geometry')
        self.infoBarAnimation.setStartValue(QRect(-1,470,0,125))
        self.infoBarAnimation.setEndValue(QRect(-1,470,720,125))
        self.infoBarAnimation.setDuration(2500)
        self.infoBarAnimation.setEasingCurve(QEasingCurve.OutExpo)

        self.loginBarAni = QPropertyAnimation(self.loginBar, b'geometry')
        self.loginBarAni.setDuration(2500)
        self.loginBarAni.setEasingCurve(QEasingCurve.OutExpo)
        self.loginBarAni.setStartValue(QRect(self.deviceWidth,470,0,125,))
        self.loginBarAni.setEndValue(QRect(882, 470, 1039, 125))

        self.copyrightAni = QPropertyAnimation(self.copyright,b'geometry')
        self.copyrightAni.setStartValue(QRect(0,(self.deviceHeight+50),(self.deviceWidth),0))
        self.copyrightAni.setEndValue(QRect(0, 1020, (self.deviceWidth), 45))
        self.copyrightAni.setDuration(1000)
        self.copyrightAni.setEasingCurve(QEasingCurve.OutCurve)

        self.panelAnimation = QParallelAnimationGroup()
        self.infoBarAnimation.start()
        self.copyrightAni.start()
        self.loginBarAni.start()
        self.quotAni.start()
        self.loadExit.start()
        self.logoAniOne.start()
        self.logoAniTwo.start()

    def disAnimateAll(self):
        blur = QGraphicsBlurEffect()
        self.mainLogo.setGraphicsEffect(blur)
        self.logoAniOne = QPropertyAnimation(self.mainLogo, b'geometry')
        self.logoAniOne.setStartValue(QRect(727, 415, 145, 195))
        self.logoAniOne.setEndValue(QRect(800, 512, 0, 0))
        self.logoAniOne.setDuration(2500)
        self.logoAniOne.setEasingCurve(QEasingCurve.OutCubic)

        self.logoAniTwo = QPropertyAnimation(blur, b'blurRadius')
        self.logoAniTwo.setStartValue(0)
        self.logoAniTwo.setEndValue(100)
        self.logoAniTwo.setDuration(1500)
        self.logoAniTwo.setEasingCurve(QEasingCurve.OutCurve)

        self.loading = QPropertyAnimation(self.sep_4, b'geometry')
        self.loading.setStartValue(QRect(0, 20, self.deviceWidth, 7))
        self.loading.setEndValue(QRect(0, 20, 0, 7))
        self.loading.setDuration(2000)
        self.loading.setEasingCurve(QEasingCurve.OutQuint)

        self.exitAni = QPropertyAnimation(self.closeButton, b'geometry')
        self.exitAni.setStartValue(QRect(self.deviceWidth - 55, 5, 50, 50))
        self.exitAni.setEndValue(QRect(self.deviceWidth - 55, 5, 50, 0))
        self.exitAni.setDuration(500)
        self.exitAni.setEasingCurve(QEasingCurve.OutBounce)

        self.loadExit = QSequentialAnimationGroup()
        self.loadExit.addAnimation(self.exitAni)
        self.loadExit.addAnimation(self.loading)

        self.qth = QPropertyAnimation(self.quote_Head, b'geometry')
        self.qth.setDuration(5000)
        self.qth.setEasingCurve(QEasingCurve.OutExpo)
        self.qth.setStartValue(QRect(50, 53, 500, 50))
        self.qth.setEndValue(QRect(50, 53, 0, 50))

        self.qta = QPropertyAnimation(self.quote_Author, b'geometry')
        self.qta.setDuration(2500)
        self.qta.setStartValue(QRect(50, 100, 350, 25))
        self.qta.setEndValue(QRect(50, 100, 0, 25))
        self.qta.setEasingCurve(QEasingCurve.OutExpo)

        self.qsep = QPropertyAnimation(self.sep_3, b'geometry')
        self.qsep.setStartValue(QRect(35, 55, 5, 80))
        self.qsep.setEndValue(QRect(35, 55, 5, 0))
        self.qsep.setDuration(2500)
        self.qsep.setEasingCurve(QEasingCurve.OutExpo)

        self.quotAni = QParallelAnimationGroup()
        self.quotAni.addAnimation(self.qth)
        self.quotAni.addAnimation(self.qta)
        self.quotAni.addAnimation(self.qsep)

        self.infoBarAnimation = QPropertyAnimation(self.infoBar, b'geometry')
        self.infoBarAnimation.setStartValue(QRect(-1, 470, 720, 125))
        self.infoBarAnimation.setEndValue(QRect(-1, 470, 0, 125))
        self.infoBarAnimation.setDuration(2500)
        self.infoBarAnimation.setEasingCurve(QEasingCurve.OutExpo)

        self.loginBarAni = QPropertyAnimation(self.loginBar, b'geometry')
        self.loginBarAni.setDuration(2500)
        self.loginBarAni.setEasingCurve(QEasingCurve.OutExpo)
        self.loginBarAni.setStartValue(QRect(882, 470, 1039, 125))
        self.loginBarAni.setEndValue(QRect(self.deviceWidth, 470, 0, 125, ))

        self.copyrightAni = QPropertyAnimation(self.copyright, b'geometry')
        self.copyrightAni.setStartValue(QRect(0, 1020, (self.deviceWidth), 45))
        self.copyrightAni.setEndValue(QRect(0, (self.deviceHeight + 50), (self.deviceWidth), 0))
        self.copyrightAni.setDuration(1000)
        self.copyrightAni.setEasingCurve(QEasingCurve.OutCurve)

        self.panelAnimation = QParallelAnimationGroup()
        self.infoBarAnimation.start()
        self.copyrightAni.start()
        self.loginBarAni.start()
        self.quotAni.start()
        self.loadExit.start()
        self.logoAniOne.start()
        self.logoAniTwo.start()
        self.loading.finished.connect(self.openDashBoard)
