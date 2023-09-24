import sys
import os
import PyQt5
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QMainWindow,QLabel
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5 import uic




class MyWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)

        # Load the UI Page - added path too
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "HangMan.ui"), self)
        #My code
        self.ImageLabel=self.findChild(QLabel,"ImageLabel")

        self.Image0 = QPixmap(os.path.join("HangManPics","hang0.png"))
        self.Image1 = QPixmap(os.path.join("HangManPics","hang1.png"))
        self.ImageLabel.setPixmap(QtGui.QPixmap("HangManPics/hang1.png"))



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MyWindow()
    main.show()
    sys.exit(app.exec_())