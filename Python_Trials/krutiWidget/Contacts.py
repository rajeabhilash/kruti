from PyQt5 import QtCore, QtGui, QtWidgets
from . import res_contacts_rc
#import res_contacts_rc
import cv2

class ContactsUI(QtWidgets.QWidget):

    minimized = QtCore.pyqtSignal()
    closed = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        ConWid = QtWidgets.QWidget(self)
        ConWid.setObjectName("Contacts")
        ConWid.resize(1920, 955)
        self.backPanel = QtWidgets.QWidget(ConWid)
        self.backPanel.setGeometry(0, 0, 1920, 955)
        self.backPanel.setObjectName("backPanel")
        ConWid.setStyleSheet("#Contacts\n"
"{\n"
"    background-color: rgba(0,0,0,125);\n"
"    border: 2px solid #24292E;\n"
"}\n"
"#backPanel\n"
"{\n"
"    background-color: rgba(255,255,255,200);\n"
"}\n"
"#krutiBar\n"
"{\n"
"    border: 2px solid #24292E;\n"
"    background-color: #24292E;\n"
"}\n"
"#contactsTitle\n"
"{\n"
"    color: #FCFCFC;\n"
"}\n"
"#conBack\n"
"{    \n"
"    background-color: rgb(36, 41, 46);\n"
"    border: 0px solid #FCFCFC;\n"
"    border-right: 2px solid #FCFCFC;\n"
"}\n"
"#krutiSearch\n"
"{\n"
"    background-color: #FCFCFC;\n"
"    border: 2px solid #24292E;\n"
"    padding-left: 25px;\n"
"    padding-right: 25px;\n"
"    padding-top: 7px;\n"
"}\n"
"#krutiVoice\n"
"{\n"
"    background-color: #FCFCFC;\n"
"    border: 2px solid #24292E;\n"
"}\n"
"#conClose\n"
"{\n"
"    border: 2px solid #24292E;\n"
"    background-color: #24292E;\n"
"    color : #FCFCFC;\n"
"    border-left: 2px solid #FCFCFC;\n"
"}\n"
"#conClose:hover{\n"
"    border: 2px solid #24292E;\n"
"    background-color: rgb(128,0,0);\n"
"    color : #FCFCFC;\n"
"    border-left: 2px solid #FCFCFC;\n"
"}\n"
"#conMini\n"
"{\n"
"    border: 2px solid #24292E;\n"
"    background-color: #24292E;\n"
"    border-left: 2px solid #FCFCFC;\n"
"}\n"
"#conAdd\n"
"{\n"
"    border: 2px solid #24292E;\n"
"    background-color: #24292E;\n"
"    color : #FCFCFC;\n"
"}\n"
"#conGroup\n"
"{\n"
"    border: 2px solid #24292E;\n"
"    background-color: #24292E;\n"
"    border-left: 2px solid #FCFCFC;\n"
"}\n"
"#conView\n"
"{\n"
"    border: 2px solid #24292E;\n"
"    background-color: #24292E;\n"
"    border-left: 2px solid #FCFCFC;\n"
"}\n"
"#conSort\n"
"{\n"
"    border: 2px solid #24292E;\n"
"    background-color: #24292E;\n"
"    border-left: 2px solid #FCFCFC;\n"
"\n"
"}")

        self.krutiBar = QtWidgets.QWidget(self.backPanel)
        self.krutiBar.setGeometry(QtCore.QRect(0, 0, 1920, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.krutiBar.sizePolicy().hasHeightForWidth())
        self.krutiBar.setSizePolicy(sizePolicy)
        self.krutiBar.setStyleSheet("")
        self.krutiBar.setObjectName("krutiBar")
        self.contactsTitle = QtWidgets.QLabel(self.krutiBar)
        self.contactsTitle.setGeometry(QtCore.QRect(100, 15, 211, 35))
        font = QtGui.QFont()
        font.setFamily("Caviar Dreams")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.contactsTitle.setFont(font)
        self.contactsTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.contactsTitle.setObjectName("contactsTitle")

        self.krutiSearch = QtWidgets.QLineEdit(self.krutiBar)
        #self.krutiSearch = LineEdit(self.krutiBar)
        self.krutiSearch.setGeometry(QtCore.QRect(501, 0, 1090, 60))
        font = QtGui.QFont()
        font.setFamily("Caviar Dreams")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.krutiSearch.setFont(font)
        self.krutiSearch.setObjectName("krutiSearch")

        self.conBack = QtWidgets.QPushButton(self.krutiBar)
        self.conBack.setEnabled(True)
        self.conBack.setGeometry(QtCore.QRect(0, 0, 50, 60))
        self.conBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.conBack.setStyleSheet("")
        self.conBack.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/backLight.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.conBack.setIcon(icon)
        self.conBack.setIconSize(QtCore.QSize(25, 25))
        self.conBack.setObjectName("conBack")
        self.krutiVoice = QtWidgets.QPushButton(self.krutiBar)
        self.krutiVoice.setGeometry(QtCore.QRect(1590, 0, 60, 60))
        self.krutiVoice.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.krutiVoice.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/InVoice.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.krutiVoice.setIcon(icon1)
        self.krutiVoice.setIconSize(QtCore.QSize(35, 35))
        self.krutiVoice.setObjectName("krutiVoice")
        self.conMini = QtWidgets.QPushButton(self.krutiBar)
        self.conMini.setGeometry(QtCore.QRect(1796, 0, 60, 60))
        self.conMini.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.conMini.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/minimize Light.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.conMini.setIcon(icon2)
        self.conMini.setIconSize(QtCore.QSize(25, 25))
        self.conMini.setObjectName("conMini")
        self.contactsLogo = QtWidgets.QLabel(self.krutiBar)
        self.contactsLogo.setGeometry(QtCore.QRect(68, 10, 40, 40))
        self.contactsLogo.setStyleSheet("border-image: url(:/icons/contacts-agenda.svg);")
        self.contactsLogo.setText("")
        self.contactsLogo.setObjectName("contactsLogo")
        self.conClose = QtWidgets.QPushButton(self.krutiBar)
        self.conClose.setGeometry(QtCore.QRect(1860, 0, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Caviar Dreams")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.conClose.setFont(font)
        self.conClose.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.conClose.setIconSize(QtCore.QSize(0, 0))
        self.conClose.setObjectName("conClose")
        self.conAdd = QtWidgets.QPushButton(self.krutiBar)
        self.conAdd.setGeometry(QtCore.QRect(1650, 0, 141, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.conAdd.setFont(font)
        self.conAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/new-userLight.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.conAdd.setIcon(icon3)
        self.conAdd.setIconSize(QtCore.QSize(30, 30))
        self.conAdd.setObjectName("conAdd")
        self.conView = QtWidgets.QPushButton(self.krutiBar)
        self.conView.setGeometry(QtCore.QRect(440, 0, 60, 60))
        self.conView.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/view-list-button.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.conView.setIcon(icon4)
        self.conView.setIconSize(QtCore.QSize(25, 25))
        self.conView.setObjectName("conView")
        self.conGroup = QtWidgets.QPushButton(self.krutiBar)
        self.conGroup.setGeometry(QtCore.QRect(380, 0, 60, 60))
        self.conGroup.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/group.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.conGroup.setIcon(icon5)
        self.conGroup.setIconSize(QtCore.QSize(25, 25))
        self.conGroup.setObjectName("conGroup")
        self.conSort = QtWidgets.QPushButton(self.krutiBar)
        self.conSort.setGeometry(QtCore.QRect(320, 0, 60, 60))
        self.conSort.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/funnel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.conSort.setIcon(icon6)
        self.conSort.setIconSize(QtCore.QSize(25, 25))
        self.conSort.setObjectName("conSort")

        self.viewContacts = ContactViewer(self.backPanel)
        self.viewContacts.setGeometry(QtCore.QRect(0, 67, 1920, 835))
        self.viewContacts.setObjectName("addContacts")

        self.viewDetails = QtWidgets.QWidget(self.backPanel)
        self.viewDetails.setGeometry(QtCore.QRect(0, 907, 1920, 50))
        self.viewDetails.setObjectName("addContacts")
        self.viewDetails.setStyleSheet("background-color:  #1A1A1D; border: 2px solid #24292E ")

        # VIEW DETAILS ----------------------------------------------------------------------------------
        self.det_Lab01 = QtWidgets.QLabel(self.viewDetails)
        self.det_Lab01.setGeometry(QtCore.QRect(30, 5, 141, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(16)
        self.det_Lab01.setFont(font)
        self.det_Lab01.setStyleSheet("color: #fcfcfc;\n"
                                     "border: 0px;")
        self.det_Lab01.setObjectName("det_Lab01")
        self.det_Lab01_2 = QtWidgets.QLabel(self.viewDetails)
        self.det_Lab01_2.setGeometry(QtCore.QRect(165, 5, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(16)
        self.det_Lab01_2.setFont(font)
        self.det_Lab01_2.setStyleSheet("color: #fcfcfc;\n"
                                       "border: 0px;")
        self.det_Lab01_2.setObjectName("det_Lab01_2")
        self.Sep00 = QtWidgets.QWidget(self.viewDetails)
        self.Sep00.setGeometry(QtCore.QRect(1465, 5, 3, 37))
        self.Sep00.setStyleSheet("background-color: #FCFCFC;\n"
                                 "border: 0px;")
        self.Sep00.setObjectName("Sep00")
        self.det_Lab01_3 = QtWidgets.QLabel(self.viewDetails)
        self.det_Lab01_3.setGeometry(QtCore.QRect(1280, 5, 141, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(16)
        self.det_Lab01_3.setFont(font)
        self.det_Lab01_3.setStyleSheet("color: #fcfcfc;\n"
                                       "border: 0px;")
        self.det_Lab01_3.setObjectName("det_Lab01_3")
        self.tolFamily = QtWidgets.QLabel(self.viewDetails)
        self.tolFamily.setGeometry(QtCore.QRect(1385, 5, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(16)
        self.tolFamily.setFont(font)
        self.tolFamily.setStyleSheet("color: #fcfcfc;\n"
                                     "border: 0px;")
        self.tolFamily.setObjectName("tolFamily")
        self.totFriends = QtWidgets.QLabel(self.viewDetails)
        self.totFriends.setGeometry(QtCore.QRect(1595, 5, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(16)
        self.totFriends.setFont(font)
        self.totFriends.setStyleSheet("color: #fcfcfc;\n"
                                      "border: 0px;")
        self.totFriends.setObjectName("totFriends")
        self.det_Lab01_6 = QtWidgets.QLabel(self.viewDetails)
        self.det_Lab01_6.setGeometry(QtCore.QRect(1480, 5, 141, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(16)
        self.det_Lab01_6.setFont(font)
        self.det_Lab01_6.setStyleSheet("color: #fcfcfc;\n"
                                       "border: 0px;")
        self.det_Lab01_6.setObjectName("det_Lab01_6")
        self.Sep00_2 = QtWidgets.QWidget(self.viewDetails)
        self.Sep00_2.setGeometry(QtCore.QRect(1685, 5, 3, 37))
        self.Sep00_2.setStyleSheet("background-color: #FCFCFC;\n"
                                   "border: 0px;")
        self.Sep00_2.setObjectName("Sep00_2")
        self.totOthers = QtWidgets.QLabel(self.viewDetails)
        self.totOthers.setGeometry(QtCore.QRect(1810, 5, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(16)
        self.totOthers.setFont(font)
        self.totOthers.setStyleSheet("color: #fcfcfc;\n"
                                     "border: 0px;")
        self.totOthers.setObjectName("totOthers")
        self.det_Lab01_8 = QtWidgets.QLabel(self.viewDetails)
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
        # VIEW DETAILS ----------------------------------------------------------------------------------

        #self.krutiSearch.setFocus(QtCore.Qt.OtherFocusReason)
        self.krutiSearch.releaseKeyboard()
        self.conMini.clicked.connect(self.minimize)
        self.conClose.clicked.connect(self.closeClicked)
        self.conAdd.clicked.connect(self.addContact)

        self.retranslateUi(ConWid)
        QtCore.QMetaObject.connectSlotsByName(ConWid)

    def retranslateUi(self, Contacts):
        _translate = QtCore.QCoreApplication.translate
        Contacts.setWindowTitle(_translate("Contacts", "Form"))
        self.contactsTitle.setText(_translate("Contacts", "CONTACTS"))
        self.krutiSearch.setPlaceholderText(_translate("Contacts", "OPERATIONS ON CONTACTS"))
        self.krutiSearch.setText(_translate("Contacts", "OPERATIONS ON CONTACTS"))
        self.conClose.setText(_translate("Contacts", "X"))
        self.conAdd.setText(_translate("Contacts", "ADD"))
        self.det_Lab01.setText(_translate("Form", "Contacts : "))
        self.det_Lab01_2.setText(_translate("Form", "250"))
        self.det_Lab01_3.setText(_translate("Form", "Family :"))
        self.tolFamily.setText(_translate("Form", "25"))
        self.totFriends.setText(_translate("Form", "150"))
        self.det_Lab01_6.setText(_translate("Form", "Friends : "))
        self.totOthers.setText(_translate("Form", "50"))
        self.det_Lab01_8.setText(_translate("Form", "Others : "))

    def showEvent(self, QShowEvent):
        #LOAD DATA : [CONTACT DISPLAY]
        self.viewContacts.addContact()
        pass

    def minimize(self):
        self.minimized.emit()

    def closeClicked(self):
        self.closed.emit()
        sys.exit()

    def addContact(self):
        pass

class LineEdit(QtWidgets.QLineEdit):

    def __init__(self,parent):
        super().__init__(parent)

    def cursorPositionChanged(self, p_int, p_int_1):
        print("> [p_int : {}, p_int_1 : {}]".format(p_int,p_int_1))

class ContactViewer(QtWidgets.QWidget):

    mouseChanged = QtCore.pyqtSignal(int, int)
    scrollChanged = QtCore.pyqtSignal()
    currentPos = 0

    def __init__(self, parent):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.grabKeyboard()
        self.startX = 30
        self.startY = 30
        self.boundX = self.startX
        self.boundY = self.startY
        self.key = 0

    def showEvent(self, QShowEvent):
        pass

    def paintEvent(self, QPaintEvent):
        paint = QtGui.QPainter(self)
        pen = QtGui.QPen()
        pen.setWidth(2)
        pen.setColor(QtGui.QColor(36,41,46))
        paint.setPen(pen)
        paint.drawRect(0,0,self.width(),self.height())

    def addContact(self):
        print("Called...")
        for i in range(0, 3):
            for j in range(1, 5):
                self.contact = Contact(self)
                self.contact.setGeometry(QtCore.QRect(self.startX, self.startY, self.contact.width(), self.contact.height()))
                self.contact.show()
                self.startX += (self.contact.width() + 25)
            self.boundX = self.startX
            self.startX = 30
            self.startY += (self.contact.height() + 15)
        print("Done Adding...")

    def wheelEvent(self, event):
        if (event.angleDelta() / 120).y() > 0:
            # Khali Kela : Move Right
            if self.currentPos > 0:
                self.currentPos = self.currentPos - 50
                self.scroll(50, 0)
        else:
            if self.currentPos < self.boundX - self.width():
                self.currentPos = self.currentPos + 50
                self.scroll(-50, 0)

"""
    def keyPressEvent(self, event):
        self.key = event.key()  # Opposite for keys L-R
        if self.key == QtCore.Qt.Key_Left:
            if self.currentPos > 0:
                self.currentPos = self.currentPos - 50
                self.scroll(50, 0)

        elif self.key == QtCore.Qt.Key_Right:
            if self.currentPos < self.boundX - self.width():
                self.currentPos = self.currentPos + 50
                self.scroll(-50, 0)
"""

class Contact(QtWidgets.QWidget):

    update = QtCore.pyqtSignal()
    delete = QtCore.pyqtSignal()
    view = QtCore.pyqtSignal()

    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(500,250)
        Form = QtWidgets.QWidget(self)
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
                                  "{ border: 2px solid #24292E;\n"
                                  "border-radius: 15px;\n"
                                  "}")
        self.Avatar.setText("")
        self.Avatar.setObjectName("Avatar")
        pic = QtGui.QPixmap("C:\\Users\\RAJEABHILASH\\Documents\\Kruti\\krutiData\\uploads\\images\\kari.JPG")
        """"
        cascPath = "C:\\Users\\RAJEABHILASH\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
        imagepath = "C:\\Users\\RAJEABHILASH\\Documents\\Kruti\\krutiData\\uploads\\images\\PratikPatil.JPG"
        faceCascade = cv2.CascadeClassifier(cascPath)

        foundFace = False
        image = cv2.imread(imagepath)
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for (x, y, w, h) in faces:
            print("X : {} | Y : {} | [FACE : W : {} | H: {}] | [IMAGE : W : {} | H : {} ]".format(x,y,w,h, pic.width(),pic.height()))
            xPos = x - (500-w)/2
            yPos = y - (250-h)/2
            foundFace = True
        """
        foundFace = False

        if foundFace:
            self.Avatar.setPixmap(pic.copy(QtCore.QRect(xPos,yPos,500,250)))
        else:
            self.Avatar.setPixmap(pic)

        self.infoPanel = QtWidgets.QWidget(self.Panel)
        self.infoPanel.setGeometry(QtCore.QRect(0, 200, 500, 46))
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
                                "#View:hover{ background-color: #b2b200;}")
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
                                "#Edit:hover{ background-color: #009999;}")
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
                                  "#Delete:hover{ background-color: #990099; }")
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

    def enterEvent(self, QEvent):
        #self.infoPanel.setGeometry(QtCore.QRect(0, 135, 500, 115))
        self.pullUP = QtCore.QPropertyAnimation(self.infoPanel, b'geometry')
        self.pullUP.setDuration(1000)
        self.pullUP.setEasingCurve(QtCore.QEasingCurve.OutElastic)
        self.pullUP.setStartValue(QtCore.QRect(0, 200, 500, 46))
        self.pullUP.setEndValue(QtCore.QRect(0, 135, 500, 115))
        self.pullUP.start()


    def leaveEvent(self, QEvent):
        #self.infoPanel.setGeometry(QtCore.QRect(0, 200, 500, 46))
        self.pushDown = QtCore.QPropertyAnimation(self.infoPanel, b'geometry')
        self.pushDown.setStartValue(QtCore.QRect(0, 135, 500, 115))
        self.pushDown.setEndValue(QtCore.QRect(0, 200, 500, 46))
        self.pushDown.setEasingCurve(QtCore.QEasingCurve.OutElastic)
        self.pushDown.setDuration(1000)
        self.pushDown.start()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = ContactsUI()
    ui.show()
    sys.exit(app.exec_())
