from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class karmaDash(QWidget):

    xpos = 0
    ypos = 0

    def __init__(self, parent):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.xpos = self.ypos = 0


    def paintEvent(self, QPaintEvent):
        paint = QPainter(self)
        paint.setRenderHint(QPainter.Antialiasing)
        paint.setPen(QPen(Qt.red,2))
        paint.drawRoundedRect(5,5,self.width()-10,self.height()-10,55,55)

        paint.drawEllipse(self.xpos-5,self.ypos-5,10,10)

        # DRAWING AXIS :--------------------------
        self.drawAxis(paint)

    def drawAxis(self,paint):
        paint.setPen(QPen(Qt.white,1))
        # Y AXIS
        paint.drawLine(75,100,75,self.height()-75)
        # X AXIS
        paint.drawLine(50,self.height()-100,self.width()-75,self.height()-100)

    def mouseMoveEvent(self, event):
        self.xpos = event.x()
        self.ypos = event.y()
        self.repaint()