import sys
import os
import PyQt5
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import uic


class MyWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)

        # Load the UI Page - added path too
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "FileName.ui"), self)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MyWindow()
    main.show()
    sys.exit(app.exec_())