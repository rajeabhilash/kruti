from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import Qt
import sys
from tendo import singleton
import startKruti as kruti

if __name__ =='__main__':
    try :
        print("OM NAMAH SHIVAY")
        krutiInstance = singleton.SingleInstance()
        krutiAI = QApplication(sys.argv)
        loginWindow = QMainWindow()
        ui = kruti.Ui_MainWindow()
        ui.deviceWidth = krutiAI.desktop().width()
        ui.deviceHeight = krutiAI.desktop().height()
        ui.setupUi(loginWindow)
        loginWindow.setWindowState(Qt.WindowFullScreen)
        loginWindow.show()
        sys.exit(krutiAI.exec_())

    except singleton.SingleInstanceException:
        print('-'*55)
        print("   |\t\t KRUTI IS RUNNING  \t\t | ")
        print('-'*55)
        print("  See previous instance of kruti in the TaskBar..!")
        print('-'*55)
    except TypeError:
        print("closed.")
