from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal

class dateTime(QThread):

    dateTimeChange = pyqtSignal()

    def __init__(self):
        super().__init__()

    def __del__(self):
        del self

    def run(self):
        while True:
            self.dateTimeChange.emit()
            self.sleep(1)