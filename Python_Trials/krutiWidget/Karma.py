from PyQt5 import QtCore, QtGui, QtWidgets
from . import res_karma_rc

class KarmaUI(QtWidgets.QWidget):


    def __init__(self,parent):
        super().__init__(parent)
        Karma = QtWidgets.QWidget(self)
        Karma.setObjectName("Karma")
        Karma.resize(1920, 780)
        Karma.setStyleSheet("#Karma{background-color :rgba(255,255,255,120);border: 2px solid #24292E;}")
        self.KarmaPanel = QtWidgets.QWidget(Karma)
        self.KarmaPanel.setGeometry(QtCore.QRect(0, 0, 1920, 780))
        self.KarmaPanel.setStyleSheet("#KarmaPanel{\n"
"background-color: rgb(0,255,255,0); border: 2px solid #24292E;\n"
"}")
        self.KarmaPanel.setObjectName("KarmaPanel")
        self.karmaHead = QtWidgets.QWidget(self.KarmaPanel)
        self.karmaHead.setGeometry(QtCore.QRect(0, 1, 1920, 111))
        self.karmaHead.setStyleSheet("#karmaHead\n"
"{\n"
"    border: 2px solid #24292E;\n"
"}")
        self.karmaHead.setObjectName("karmaHead")
        self.label_2 = QtWidgets.QLabel(self.karmaHead)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 201, 28))
        font = QtGui.QFont()
        font.setFamily("Caviar Dreams")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_20 = QtWidgets.QPushButton(self.karmaHead)
        self.pushButton_20.setGeometry(QtCore.QRect(1520, 30, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 41, 46);")
        self.pushButton_20.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/iconfinder-icon Light.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_20.setIcon(icon)
        self.pushButton_20.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.karmaHead)
        self.pushButton_21.setGeometry(QtCore.QRect(1567, 30, 131, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_21.setStyleSheet("color: rgb(36, 41, 46);\n"
"border: 2px solid #24292E;")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_2 = QtWidgets.QPushButton(self.karmaHead)
        self.pushButton_2.setGeometry(QtCore.QRect(1750, 30, 131, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("color: rgb(36, 41, 46);\n"
"border: 2px solid #24292E;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.karmaHead)
        self.label.setGeometry(QtCore.QRect(50, 15, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.karmaHead)
        self.pushButton.setGeometry(QtCore.QRect(1703, 30, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 41, 46);")
        self.pushButton.setObjectName("pushButton")
        self.widget_9 = QtWidgets.QWidget(self.karmaHead)
        self.widget_9.setGeometry(QtCore.QRect(1500, 20, 5, 70))
        self.widget_9.setStyleSheet("border: 0px solid #24292E;\n"
"border-radius:1.5px;\n"
"background-color: rgb(36, 41, 46);")
        self.widget_9.setObjectName("widget_9")
        self.widget = QtWidgets.QWidget(self.karmaHead)
        self.widget.setGeometry(QtCore.QRect(30, 20, 5, 80))
        self.widget.setStyleSheet("border: 0px solid #24292E;\n"
"border-radius:1.5px;\n"
"background-color: rgb(36, 41, 46);")
        self.widget.setObjectName("widget")
        self.KarmaTimeLine = QtWidgets.QWidget(self.KarmaPanel)
        self.KarmaTimeLine.setGeometry(QtCore.QRect(0, 120, 1920, 661))
        self.KarmaTimeLine.setStyleSheet("#KarmaTimeLine{border: 2px solid #24292E;}")
        self.KarmaTimeLine.setObjectName("KarmaTimeLine")
        self.widget_2 = QtWidgets.QWidget(self.KarmaTimeLine)
        self.widget_2.setGeometry(QtCore.QRect(740, 54, 3, 585))
        self.widget_2.setStyleSheet("border: 0px solid #24292E;\n"
"border-radius:0.5px;\n"
"background-color: rgb(36, 41, 46);")
        self.widget_2.setObjectName("widget_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.KarmaTimeLine)
        self.pushButton_3.setGeometry(QtCore.QRect(740, 110, 275, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 41, 46);\n"
"border: 2px solid  #24292E;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/view-list-button.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.KarmaTimeLine)
        self.pushButton_4.setGeometry(QtCore.QRect(740, 210, 275, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 41, 46);\n"
"border: 2px solid  #24292E;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.widget_3 = QtWidgets.QWidget(self.KarmaTimeLine)
        self.widget_3.setGeometry(QtCore.QRect(1070, 54, 3, 585))
        self.widget_3.setStyleSheet("border: 0px solid #24292E;\n"
"border-radius:0.5px;\n"
"background-color: rgb(36, 41, 46);")
        self.widget_3.setObjectName("widget_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.KarmaTimeLine)
        self.pushButton_5.setGeometry(QtCore.QRect(1070, 110, 275, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 41, 46);\n"
"border: 2px solid  #24292E;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.KarmaTimeLine)
        self.pushButton_6.setGeometry(QtCore.QRect(1070, 530, 275, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 41, 46);\n"
"border: 2px solid  #24292E;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.widget_4 = QtWidgets.QWidget(self.KarmaTimeLine)
        self.widget_4.setGeometry(QtCore.QRect(1400, 54, 3, 585))
        self.widget_4.setStyleSheet("border: 0px solid #24292E;\n"
"border-radius:0.5px;\n"
"background-color: rgb(36, 41, 46);")
        self.widget_4.setObjectName("widget_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.KarmaTimeLine)
        self.pushButton_7.setGeometry(QtCore.QRect(1400, 162, 275, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 41, 46);\n"
"border: 2px solid  #24292E;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.KarmaTimeLine)
        self.pushButton_8.setGeometry(QtCore.QRect(1400, 110, 275, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 41, 46);\n"
"border: 2px solid  #24292E;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.pushButton_8.setIcon(icon1)
        self.pushButton_8.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.KarmaTimeLine)
        self.pushButton_9.setGeometry(QtCore.QRect(60, 110, 275, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 41, 46);\n"
"border: 2px solid  #24292E;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.pushButton_9.setIcon(icon1)
        self.pushButton_9.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_9.setObjectName("pushButton_9")
        self.widget_5 = QtWidgets.QWidget(self.KarmaTimeLine)
        self.widget_5.setGeometry(QtCore.QRect(60, 54, 3, 585))
        self.widget_5.setStyleSheet("border: 0px solid #24292E;\n"
"border-radius:0.5px;\n"
"background-color: rgb(36, 41, 46);")
        self.widget_5.setObjectName("widget_5")
        self.pushButton_10 = QtWidgets.QPushButton(self.KarmaTimeLine)
        self.pushButton_10.setGeometry(QtCore.QRect(60, 450, 275, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 41, 46);\n"
"border: 2px solid  #24292E;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.pushButton_10.setIcon(icon1)
        self.pushButton_10.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_10.setObjectName("pushButton_10")
        self.widget_6 = QtWidgets.QWidget(self.KarmaTimeLine)
        self.widget_6.setGeometry(QtCore.QRect(400, 54, 3, 585))
        self.widget_6.setStyleSheet("border: 0px solid #24292E;\n"
"border-radius:0.5px;\n"
"background-color: rgb(36, 41, 46);")
        self.widget_6.setObjectName("widget_6")
        self.pushButton_11 = QtWidgets.QPushButton(self.KarmaTimeLine)
        self.pushButton_11.setGeometry(QtCore.QRect(400, 210, 275, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 41, 46);\n"
"border: 2px solid  #24292E;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.pushButton_11.setIcon(icon1)
        self.pushButton_11.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.KarmaTimeLine)
        self.pushButton_12.setGeometry(QtCore.QRect(400, 110, 275, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 41, 46);\n"
"border: 2px solid  #24292E;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.pushButton_12.setIcon(icon1)
        self.pushButton_12.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.KarmaTimeLine)
        self.pushButton_13.setGeometry(QtCore.QRect(400, 320, 275, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 41, 46);\n"
"border: 2px solid  #24292E;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.pushButton_13.setIcon(icon1)
        self.pushButton_13.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.KarmaTimeLine)
        self.pushButton_14.setGeometry(QtCore.QRect(740, 580, 275, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 41, 46);\n"
"border: 2px solid  #24292E;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.pushButton_14.setIcon(icon1)
        self.pushButton_14.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_3 = QtWidgets.QLabel(self.KarmaTimeLine)
        self.label_3.setGeometry(QtCore.QRect(60, 15, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Caviar Dreams")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(34, 39, 44);\n"
"border: 2px solid;\n"
"border-color: rgb(35, 40, 44);\n"
"padding-right: 15px;")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.KarmaTimeLine)
        self.label_4.setGeometry(QtCore.QRect(400, 15, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Caviar Dreams")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(34, 39, 44);\n"
"border: 2px solid;\n"
"border-color: rgb(35, 40, 44);\n"
"padding-right: 15px;")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.KarmaTimeLine)
        self.label_5.setGeometry(QtCore.QRect(740, 15, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Caviar Dreams")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(34, 39, 44);\n"
"border: 2px solid;\n"
"border-color: rgb(35, 40, 44);\n"
"padding-right: 15px;")
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.KarmaTimeLine)
        self.label_6.setGeometry(QtCore.QRect(1070, 15, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Caviar Dreams")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(34, 39, 44);\n"
"border: 2px solid;\n"
"border-color: rgb(35, 40, 44);\n"
"padding-right: 15px;")
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.KarmaTimeLine)
        self.label_7.setGeometry(QtCore.QRect(1400, 15, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Caviar Dreams")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(34, 39, 44);\n"
"border: 2px solid;\n"
"border-color: rgb(35, 40, 44);\n"
"padding-right: 15px;")
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.pushButton_15 = QtWidgets.QPushButton(self.KarmaTimeLine)
        self.pushButton_15.setGeometry(QtCore.QRect(1740, 110, 275, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_15.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 41, 46);\n"
"border: 2px solid  #24292E;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.pushButton_15.setIcon(icon1)
        self.pushButton_15.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_15.setObjectName("pushButton_15")
        self.widget_7 = QtWidgets.QWidget(self.KarmaTimeLine)
        self.widget_7.setGeometry(QtCore.QRect(1740, 54, 3, 585))
        self.widget_7.setStyleSheet("border: 0px solid #24292E;\n"
"border-radius:0.5px;\n"
"background-color: rgb(36, 41, 46);")
        self.widget_7.setObjectName("widget_7")
        self.label_8 = QtWidgets.QLabel(self.KarmaTimeLine)
        self.label_8.setGeometry(QtCore.QRect(1740, 15, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Caviar Dreams")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(34, 39, 44);\n"
"border: 2px solid;\n"
"border-color: rgb(35, 40, 44);\n"
"padding-left: 75px;")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.pushButton_16 = QtWidgets.QPushButton(self.KarmaTimeLine)
        self.pushButton_16.setGeometry(QtCore.QRect(1740, 170, 275, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_16.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 41, 46);\n"
"border: 2px solid  #24292E;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.pushButton_16.setIcon(icon1)
        self.pushButton_16.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_16.setObjectName("pushButton_16")
        self.TimeLine = QtWidgets.QWidget(self.KarmaTimeLine)
        self.TimeLine.setGeometry(QtCore.QRect(0, 54, 80, 585))
        self.TimeLine.setStyleSheet("#TimeLine{\n"
"border: 0px solid #24292E;\n"
"border-top-right-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"background-color: rgb(36, 41, 46,200);\n"
"}")
        self.TimeLine.setObjectName("TimeLine")
        self.label_9 = QtWidgets.QLabel(self.TimeLine)
        self.label_9.setGeometry(QtCore.QRect(0, 56, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0,0);\n"
"border:2px solid  rgba(0,0,0,0);\n"
"border-top: 2px solid #fcfcfc;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.TimeLine)
        self.label_10.setGeometry(QtCore.QRect(0, 150, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0,0);\n"
"border:2px solid  rgba(0,0,0,0);\n"
"border-top: 2px solid #fcfcfc;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.TimeLine)
        self.label_11.setGeometry(QtCore.QRect(0, 260, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0,0);\n"
"border:2px solid  rgba(0,0,0,0);\n"
"border-top: 2px solid #fcfcfc;")
        self.label_11.setObjectName("label_11")
        self.label_20 = QtWidgets.QLabel(self.TimeLine)
        self.label_20.setGeometry(QtCore.QRect(0, 396, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0,0);\n"
"border:2px solid  rgba(0,0,0,0);\n"
"border-top: 2px solid #fcfcfc;")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.TimeLine)
        self.label_21.setGeometry(QtCore.QRect(0, 527, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0,0);\n"
"border:2px solid  rgba(0,0,0,0);\n"
"border-top: 2px solid #fcfcfc;")
        self.label_21.setObjectName("label_21")
        self.label_12 = QtWidgets.QLabel(self.KarmaTimeLine)
        self.label_12.setGeometry(QtCore.QRect(-270, 15, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Caviar Dreams")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(34, 39, 44);\n"
"border: 2px solid;\n"
"border-color: rgb(35, 40, 44);\n"
"padding-right: 15px;")
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.pushButton_17 = QtWidgets.QPushButton(self.KarmaTimeLine)
        self.pushButton_17.setGeometry(QtCore.QRect(-270, 580, 275, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_17.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 41, 46);\n"
"border: 2px solid  #24292E;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.pushButton_17.setIcon(icon1)
        self.pushButton_17.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_17.setObjectName("pushButton_17")
        self.widget_8 = QtWidgets.QWidget(self.KarmaTimeLine)
        self.widget_8.setGeometry(QtCore.QRect(-270, 54, 3, 585))
        self.widget_8.setStyleSheet("border: 0px solid #24292E;\n"
"border-radius:0.5px;\n"
"background-color: rgb(36, 41, 46);")
        self.widget_8.setObjectName("widget_8")
        self.pushButton_18 = QtWidgets.QPushButton(self.KarmaTimeLine)
        self.pushButton_18.setGeometry(QtCore.QRect(-270, 110, 275, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_18.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 41, 46);\n"
"border: 2px solid  #24292E;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.pushButton_18.setIcon(icon1)
        self.pushButton_18.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.KarmaTimeLine)
        self.pushButton_19.setGeometry(QtCore.QRect(-270, 210, 275, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_19.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 41, 46);\n"
"border: 2px solid  #24292E;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.pushButton_19.setIcon(icon1)
        self.pushButton_19.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_19.setObjectName("pushButton_19")
        self.label_13 = QtWidgets.QLabel(self.KarmaTimeLine)
        self.label_13.setGeometry(QtCore.QRect(60, 15, 71, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 41, 46);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.KarmaTimeLine)
        self.label_14.setGeometry(QtCore.QRect(400, 15, 71, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 41, 46);")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.KarmaTimeLine)
        self.label_15.setGeometry(QtCore.QRect(740, 15, 71, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 41, 46);")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.KarmaTimeLine)
        self.label_16.setGeometry(QtCore.QRect(1070, 15, 71, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 41, 46);")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.KarmaTimeLine)
        self.label_17.setGeometry(QtCore.QRect(1400, 15, 71, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 41, 46);")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.KarmaTimeLine)
        self.label_18.setGeometry(QtCore.QRect(1740, 15, 71, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 41, 46);")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.KarmaTimeLine)
        self.label_19.setGeometry(QtCore.QRect(0, 160, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0,0);\n"
"border:2px solid  rgba(0,0,0,0);\n"
"border-top: 2px solid #fcfcfc;")
        self.label_19.setObjectName("label_19")

        self.retranslateUi(Karma)
        QtCore.QMetaObject.connectSlotsByName(Karma)

    def retranslateUi(self, Karma):
        _translate = QtCore.QCoreApplication.translate
        Karma.setWindowTitle(_translate("Karma", "Form"))
        self.label_2.setText(_translate("Karma", "It\'s the only right."))
        self.pushButton_21.setText(_translate("Karma", "VIEW"))
        self.pushButton_2.setText(_translate("Karma", "NEW"))
        self.label.setText(_translate("Karma", "KARMA"))
        self.pushButton.setText(_translate("Karma", "+"))
        self.pushButton_3.setText(_translate("Karma", "  00:00 KARMA NAME"))
        self.pushButton_4.setText(_translate("Karma", "  00:00 KARMA NAME"))
        self.pushButton_5.setText(_translate("Karma", "  00:00 KARMA NAME"))
        self.pushButton_6.setText(_translate("Karma", "  00:00 KARMA NAME"))
        self.pushButton_7.setText(_translate("Karma", "  00:00 KARMA NAME"))
        self.pushButton_8.setText(_translate("Karma", "  00:00 KARMA NAME"))
        self.pushButton_9.setText(_translate("Karma", "  00:00 KARMA NAME"))
        self.pushButton_10.setText(_translate("Karma", "  00:00 KARMA NAME"))
        self.pushButton_11.setText(_translate("Karma", "  00:00 KARMA NAME"))
        self.pushButton_12.setText(_translate("Karma", "  00:00 KARMA NAME"))
        self.pushButton_13.setText(_translate("Karma", "  00:00 KARMA NAME"))
        self.pushButton_14.setText(_translate("Karma", "  00:00 KARMA NAME"))
        self.label_3.setText(_translate("Karma", "SUNDAY"))
        self.label_4.setText(_translate("Karma", "MONDAY"))
        self.label_5.setText(_translate("Karma", "TUESDAY"))
        self.label_6.setText(_translate("Karma", "WEDNESDAY"))
        self.label_7.setText(_translate("Karma", "THURSDAY"))
        self.pushButton_15.setText(_translate("Karma", "  00:00 KARMA NAME"))
        self.label_8.setText(_translate("Karma", "FRIDAY"))
        self.pushButton_16.setText(_translate("Karma", "  00:00 KARMA NAME"))
        self.label_9.setText(_translate("Karma", "09:30 AM"))
        self.label_10.setText(_translate("Karma", "11:30 AM"))
        self.label_11.setText(_translate("Karma", "02:45 PM"))
        self.label_20.setText(_translate("Karma", "05:45 PM"))
        self.label_21.setText(_translate("Karma", "09:30 PM"))
        self.label_12.setText(_translate("Karma", "SATURDAY"))
        self.pushButton_17.setText(_translate("Karma", "  00:00 KARMA NAME"))
        self.pushButton_18.setText(_translate("Karma", "  00:00 KARMA NAME"))
        self.pushButton_19.setText(_translate("Karma", "  00:00 KARMA NAME"))
        self.label_13.setText(_translate("Karma", "10/7"))
        self.label_14.setText(_translate("Karma", "11/7"))
        self.label_15.setText(_translate("Karma", "12/7"))
        self.label_16.setText(_translate("Karma", "13/7"))
        self.label_17.setText(_translate("Karma", "14/7"))
        self.label_18.setText(_translate("Karma", "15/7"))
        self.label_19.setText(_translate("Karma", "10:30 AM"))


