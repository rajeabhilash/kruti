from PyQt5 import QtCore, QtGui, QtWidgets
from krutiWidgets import Money,Karma,Contacts
import dateTime as dt
import dash_resource_rc
import resource_list_rc
import sys
from krutiWidgets import all_resource_rc

class Dashboard(QtWidgets.QMainWindow):

    shown = QtCore.pyqtSignal()
    hidden = QtCore.pyqtSignal()
    logout = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.tasks = []
        self.totalTasks = 0
        self.taskX = 65
        self.dateTime = dt.dateTime()
        self.startShow = False
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ICON.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setObjectName("Dashboard")
        self.centralwidget = QtWidgets.QWidget()
        self.setWindowState(QtCore.Qt.WindowFullScreen)
        self.setStyleSheet("#Dashboard{\n"
                           "border-image: url(:/images/Back.png);\n"
                           "}")
        self.setupUi()

    def showEvent(self, *args, **kwargs):
        self.shown.emit()

    def hideEvent(self, *args, **kwargs):
        self.hidden.emit()

    def setupUi(self):
        self.centralwidget.setObjectName("centralwidget")

        self.titleBar = QtWidgets.QWidget(self.centralwidget)
        self.deskPane = QtWidgets.QWidget(self.centralwidget)

        self.deskPane.setObjectName("Desktop")
        self.deskPane.setGeometry(0,60,1920,968)
        self.deskPane.setStyleSheet("#Desktop{background-color: rgba(240,240,240,120); border:2px solid #24292E;}")

        self.titleBar.setGeometry(QtCore.QRect(0, 0, 1920, 60))
        self.titleBar.setStyleSheet("#titleBar { border: 2px solid #24292E; }")
        self.titleBar.setObjectName("titleBar")

        self.Karma = Karma.KarmaUI(self.deskPane)
        self.Karma.setGeometry(0, 10, 1920, 975)

        self.Money = Money.MoneyUI(self.deskPane)
        self.Money.setGeometry(0, 0, 0, 0)

        self.Contacts = Contacts.ContactsUI(self.deskPane)
        self.Contacts.setGeometry(0, 0, 0, 0)


        self.blr = QtWidgets.QGraphicsBlurEffect()
        self.blr.setBlurRadius(125)
        self.blurLabel = QtWidgets.QLabel(self.titleBar)
        self.blurLabel.setGeometry(QtCore.QRect(0,0,1920,60))
        self.blurLabel.setGraphicsEffect(self.blr)
        self.blurLabel.setStyleSheet("background-color:rgb(255,255,255,125)")

        self.OwnerTitle = QtWidgets.QPushButton(self.titleBar)
        self.OwnerTitle.setGeometry(QtCore.QRect(66, 0, 342, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.OwnerTitle.setFont(font)
        self.OwnerTitle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.OwnerTitle.setStyleSheet("#OwnerTitle\n"
                                      "{\n border: 2px solid #24292E;"
                                      "    color:#24292E;\n"
                                      "    background-color: #fcfcfc;\n"
                                      "}\n"
                                      "#OwnerTitle:hover\n"
                                      "{\n "
                                      "   color:#fcfcfc;\n"
                                      "    background-color: #24292E;\n"
                                      "}")
        self.OwnerTitle.setObjectName("OwnerTitle")
        self.OwnerPic = QtWidgets.QLabel(self.titleBar)
        self.OwnerPic.setGeometry(QtCore.QRect(2, 2, 56, 56))
        self.OwnerPic.setText("")
        self.OwnerPic.setPixmap(QtGui.QPixmap(":/icons/RAJEABHILASH.png"))
        self.OwnerPic.setScaledContents(True)
        self.OwnerPic.setObjectName("OwnerPic")
        self.krSearch = QtWidgets.QLineEdit(self.titleBar)
        self.krSearch.setGeometry(QtCore.QRect(406, 0, 1003, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(16)
        self.krSearch.setFont(font)
        self.krSearch.setStyleSheet("#krSearch {\n"
                                    "    font-family: \"Roboto Medium\";\n"
                                    "    background-color: rgb(0,0,0,0);\n"
                                    "    padding-left: 25px;\n"
                                    "    padding-right: 25px;\n"
                                    "    color: #24292E;\n"
                                    "    border: 2px solid #24292E;\n"
                                    "}")
        self.krSearch.setText("")
        self.krSearch.setObjectName("krSearch")
        self.krVoice = QtWidgets.QPushButton(self.titleBar)
        self.krVoice.setGeometry(QtCore.QRect(1408, 0, 60, 60))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.krVoice.setFont(font)
        self.krVoice.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.krVoice.setStyleSheet("#krVoice {    background-color: #24292E; }")
        self.krVoice.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/InVoiceL.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.krVoice.setIcon(icon)
        self.krVoice.setIconSize(QtCore.QSize(35, 35))
        self.krVoice.setObjectName("krVoice")
        self.krLogout = QtWidgets.QPushButton(self.titleBar)
        self.krLogout.setGeometry(QtCore.QRect(1860, 0, 60, 60))
        self.krLogout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.krLogout.setStyleSheet("#krLogout { background-color: #24292E; }\n"
                                    "#krLogout:hover {background-color: rgb(121, 2, 2);}\n"
                                    "")
        self.krLogout.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/DLogout.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.krLogout.setIcon(icon1)
        self.krLogout.setIconSize(QtCore.QSize(35, 35))
        self.krLogout.setObjectName("krLogout")
        self.krTime = QtWidgets.QLabel(self.titleBar)
        self.krTime.setGeometry(QtCore.QRect(1681, 0, 181, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(57)
        self.krTime.setFont(font)
        self.krTime.setStyleSheet("#krTime { border: 2px solid #24292E; color: #24292E;}")
        self.krTime.setAlignment(QtCore.Qt.AlignCenter)
        self.krTime.setObjectName("krTime")
        self.krDay = QtWidgets.QLabel(self.titleBar)
        self.krDay.setGeometry(QtCore.QRect(1467, 0, 216, 35))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.krDay.setFont(font)
        self.krDay.setStyleSheet("#krDay {border: 2px solid #24292E; color: #24292E; padding-right: 5px; text-transform: capitalize;}")
        self.krDay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.krDay.setObjectName("krDay")
        self.krDate = QtWidgets.QLabel(self.titleBar)
        self.krDate.setGeometry(QtCore.QRect(1467, 33, 216, 27))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.krDate.setFont(font)
        self.krDate.setStyleSheet("#krDate {border: 2px solid #24292E; color: #24292E; padding-right: 5px;}")
        self.krDate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.krDate.setObjectName("krDate")
        self.taskBar = QtWidgets.QWidget(self.centralwidget)
        self.taskBar.setGeometry(QtCore.QRect(0, 1030, 1920, 50))
        self.taskBar.setStyleSheet("#taskBar { border: 0px solid rgba(0,0,0,0); border-top: 0.5px solid #ff00ff; background-color:#24292E;}")
        self.taskBar.setObjectName("taskBar")
        self.startButton = QtWidgets.QPushButton(self.taskBar)
        self.startButton.setGeometry(0,3,60,45)
        self.startButton.setObjectName("startButton")
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startButton.setStyleSheet("#startButton { border: 2px solid #24292E; background-color:#24292E; border: 0px solid #24292E; border-right: 2px solid #FCFCFC}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("startKruti.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startButton.setIcon(icon)
        self.startButton.setIconSize(QtCore.QSize(50,50))

        self.taskList = QtWidgets.QWidget(self.centralwidget)
        self.taskList.setObjectName("taskList")
        #self.taskList.setGeometry(QtCore.QRect(0, 860, 200, 170))
        self.taskList.setGeometry(QtCore.QRect(0, 1050, 0, 0))
        self.taskList.setStyleSheet("#taskList { border: 0px solid #24292E; border-bottom: 2px solid #fcfcfc;background-color:#24292E;}")

        self.taskContact = QtWidgets.QPushButton(self.taskList)
        self.taskMoney = QtWidgets.QPushButton(self.taskList)
        self.taskNew = QtWidgets.QPushButton(self.taskList)

        conIcon = QtGui.QIcon()
        conIcon.addPixmap(QtGui.QPixmap(":/icons/contacts-agenda.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        monIcon = QtGui.QIcon()
        monIcon.addPixmap(QtGui.QPixmap(":/icons/wallet-filled-money-tool.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.taskContact.setGeometry(0, 0, 200, 50)
        self.taskContact.setIcon(conIcon)
        self.taskContact.setIconSize(QtCore.QSize(35, 35))
        self.taskContact.setStyleSheet("padding-left: 5px; color: #fcfcfc;border: 0px solid #24292E; border-bottom: 2px solid #fcfcfc;background-color:#24292E;")
        self.taskContact.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.taskContact.setText("Contacts")
        self.taskContact.setFont(QtGui.QFont("Caviar Dreams", 16))

        self.taskMoney.setGeometry(0, 60, 200, 50)
        self.taskMoney.setStyleSheet("color: #fcfcfc;border: 0px solid #24292E; border-bottom: 2px solid #fcfcfc;background-color:#24292E;")
        self.taskMoney.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.taskMoney.setText("Money")
        self.taskMoney.setFont(QtGui.QFont("Caviar Dreams", 16))
        self.taskMoney.setIcon(monIcon)
        self.taskMoney.setIconSize(QtCore.QSize(35,35))

        self.taskNew.setGeometry(0, 120, 200, 50)
        self.taskNew.setStyleSheet("color: #fcfcfc;border: 0px solid #24292E; border-bottom: 2px solid #fcfcfc;background-color:#24292E;")
        self.taskNew.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.taskNew.setText("Create")
        self.taskNew.setFont(QtGui.QFont("Caviar Dreams", 16))

        self.dateTime.dateTimeChange.connect(self.updateDateTime)
        self.dateTime.start()
        self.OwnerTitle.setText("RAJE ABHILASH MOHITE")
        self.krSearch.setPlaceholderText("Press F2 or Say \'Kruti\'")
        self.setWindowTitle("{} - Artificial Intelligent Kruti.".format(self.OwnerTitle.text()))
        self.setCentralWidget(self.centralwidget)
        self.krLogout.clicked.connect(self.logoutDash)
        self.startButton.clicked.connect(self.start)
        self.blr = QtWidgets.QGraphicsBlurEffect()
        self.taskMoney.clicked.connect(self.showMoney)
        self.taskContact.clicked.connect(self.showContacts)
        #self.taskNew.clicked.connect()

    def logoutDash(self):
        self.logout.emit()
        self.hide()
        sys.exit()

    def updateDateTime(self):
        self.krTime.setText(QtCore.QDateTime.currentDateTime().toString("hh:mm:ssA"))
        self.krDay.setText((QtCore.QDateTime.currentDateTime().toString("dddd")).upper())
        self.krDate.setText((QtCore.QDateTime.currentDateTime().toString("dd MMMM yyyy")).upper())

    def start(self):
        if not self.startShow:
            self.taskList.setGeometry(QtCore.QRect(0, 860, 200, 170))
            self.startShow = True
        else:
            self.taskList.setGeometry(QtCore.QRect(0, 1050, 0, 0))
            self.startShow = False

    def showContacts(self):
        self.Contacts.setGeometry(0, 10, 1920, 955)
        self.Contacts.raise_()
        self.taskList.setGeometry(0, 1050, 0, 0)
        self.task = Tasks(self.taskBar)
        self.task.setGeometry(self.taskX,2,200,self.taskBar.height()-2)
        self.task.setName("index : {}".format(self.totalTasks))
        self.task.setIndex(self.totalTasks)
        self.totalTasks += 1
        self.taskX += 205
        self.task.closed.connect(self.closeTask)
        self.task.clicked.connect(self.openTask)
        self.task.show()
        self.tasks.append(self.task)
        self.startShow = False

    def showMoney(self):
        self.Money.setGeometry(0, 10, 1920, 955)
        self.Money.raise_()
        self.taskList.setGeometry(0, 1050, 0, 0)
        self.task = Tasks(self.taskBar)
        self.task.setGeometry(self.taskX, 2, 200, self.taskBar.height() - 2)
        self.task.setName("index : {}".format(self.totalTasks))
        self.task.setIndex(self.totalTasks)
        self.totalTasks += 1
        self.taskX += 205
        self.task.show()
        self.tasks.append(self.task)
        self.startShow = False

    def showNew(self):
        pass

    def closeTask(self,index):
        tot = len(self.tasks)
        self.tasks[index].setGeometry(0,0,0,0)
        del self.tasks[index]

    def openTask(self, index):
        pass


class Tasks(QtWidgets.QWidget):

    closed = QtCore.pyqtSignal(int)
    clicked = QtCore.pyqtSignal()
    index = 0

    def __init__(self,parent):
        super().__init__(parent)
        self.pack = QtWidgets.QWidget(self)
        self.taskView = QtWidgets.QPushButton(self.pack)
        self.taskClose = QtWidgets.QPushButton(self.pack)
        self.resize(250,50)

        self.pack.setStyleSheet("background-color: #24292E; border: 2px solid #FCFCFC;")
        self.taskView.setStyleSheet("background-color: rgba(0,0,0,0);color:#FCFCFC; text-align:left; padding-left:10px")
        self.taskView.setFont(QtGui.QFont("Caviar Dreams",14, QtGui.QFont.Bold))
        self.taskView.setText("TASK NAME")
        self.taskClose.setObjectName("taskClose")
        self.taskClose.setStyleSheet("background-color: rgba(0,0,0,0); color: rgba(0,0,0,0); border: 0px solid #24292E")
        self.taskClose.setFont(QtGui.QFont("Caviar Dreams",14))
        self.taskClose.setText('X')
        self.taskClose.setCursor(QtCore.Qt.PointingHandCursor)
        self.taskClose.clicked.connect(self.closeClicked)
        self.taskView.clicked.connect(self.viewClicked)

    def getName(self):
        return self.taskView.text()

    def getIndex(self):
        return self.index

    def closeClicked(self):
        self.closed.emit(self.index)

    def viewClicked(self):
        self.clicked.emit()

    def setName(self,name):
        self.taskView.setText(name)

    def setIndex(self,index):
        self.index =  index

    def showEvent(self, QShowEvent):
        self.pack.setGeometry(0,0,self.width(),self.height())
        self.taskView.setGeometry(1,1,self.width()-2,self.height()-2)
        self.taskClose.setGeometry(self.width()-53,3,50,self.height()-6)

    def enterEvent(self, QEvent):
        self.taskClose.setStyleSheet("#taskClose {background-color: #24292E; color: #FCFCFC; border: 0px solid #24292E; border-left: 2px solid #FCFCFC}"
            "#taskClose:hover{background-color: rgb(128,0,0); color:#FCFCFC;}")

    def leaveEvent(self, QEvent):
        self.taskClose.setStyleSheet("background-color: rgba(0,0,0,0); color: rgba(0,0,0,0); border: 0px solid #24292E")
        pass

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dash = Dashboard()
    dash.show()
    sys.exit(app.exec_())
