import ctypes
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream

#from "the .py file" import "the class inside the .py"


# for taskbar icon
myappid = u'App Name'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
# i dont understand it

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.ui = "the class inside the .py"
        self.ui.setupUi(self)
        self.initUI()#intilization function



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())