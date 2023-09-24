import sys
import os
import PyQt5
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QMainWindow,QLabel
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5 import uic
from PyQt5.QtCore import QTimer,QEventLoop

#True = x Turn/ False = O Turn
global Turn
Turn = True

#Xicon = QtGui.QIcon(os.path.join("icons","icons8_close_480px_1.png"))
#Oicon = QtGui.QIcon(os.path.join("icons","icons8-full-moon-100 .png"))

class MyWindow(QMainWindow):

    

    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)

        # Load the UI Page - added path too
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "tictactoe.ui"), self)
        #  1  2  3
        #A #  #  #
        #B #  #  #
        #C #  #  #
        self.A1.clicked.connect(self.A1GamePlaye)
        self.A2.clicked.connect(self.A2GamePlaye)
        self.A3.clicked.connect(self.A3GamePlaye)
        self.B1.clicked.connect(self.B1GamePlaye)
        self.B2.clicked.connect(self.B2GamePlaye)
        self.B3.clicked.connect(self.B3GamePlaye)
        self.C1.clicked.connect(self.C1GamePlaye)
        self.C2.clicked.connect(self.C2GamePlaye)
        self.C3.clicked.connect(self.C3GamePlaye)
        self.MainLabel=self.findChild(QLabel,"MainLabel")
    

    def A1GamePlaye(self):
        global Turn
        if self.A1.text()!="X" and self.A1.text()!="O":
            if Turn:
                self.A1.setText("X")
                Turn = False
                self.MainLabel.setText("O Turn")
            else:
                self.A1.setText("O")
                Turn = True
                self.MainLabel.setText("X Turn")
        winner(self)
    def A2GamePlaye(self):
        global Turn
        if self.A2.text()!="X" and self.A2.text()!="O":
            if Turn:
                self.A2.setText("X")
                Turn = False
                self.MainLabel.setText("O Turn")
            else:
                self.A2.setText("O")
                Turn = True
                self.MainLabel.setText("X Turn")
        winner(self)
    def A3GamePlaye(self):
        global Turn
        if self.A3.text()!="X" and self.A3.text()!="O":
            if Turn:
                self.A3.setText("X")
                Turn = False
                self.MainLabel.setText("O Turn")
            else:
                self.A3.setText("O")
                Turn = True
                self.MainLabel.setText("X Turn")
        winner(self)
    def B1GamePlaye(self):
        global Turn
        if self.B1.text()!="X" and self.B1.text()!="O":
            if Turn:
                self.B1.setText("X")
                Turn = False
                self.MainLabel.setText("O Turn")
            else:
                self.B1.setText("O")
                Turn = True
                self.MainLabel.setText("X Turn")
        winner(self)
    def B2GamePlaye(self):
        global Turn
        if self.B2.text()!="X" and self.B2.text()!="O":
            if Turn:
                self.B2.setText("X")
                Turn = False
                self.MainLabel.setText("O Turn")
            else:
                self.B2.setText("O")
                Turn = True
                self.MainLabel.setText("X Turn")
        winner(self)
    def B3GamePlaye(self):
        global Turn
        if self.B3.text()!="X" and self.B3.text()!="O":
            if Turn:
                self.B3.setText("X")
                Turn = False
                self.MainLabel.setText("O Turn")
            else:
                self.B3.setText("O")
                Turn = True
                self.MainLabel.setText("X Turn")
        winner(self)
    def C1GamePlaye(self):
        global Turn
        if self.C1.text()!="X" and self.C1.text()!="O":
            if Turn:
                self.C1.setText("X")
                Turn = False
                self.MainLabel.setText("O Turn")
            else:
                self.C1.setText("O")
                Turn = True
                self.MainLabel.setText("X Turn")
        winner(self)
    def C2GamePlaye(self):
        global Turn
        if self.C2.text()!="X" and self.C2.text()!="O":
            if Turn:
                self.C2.setText("X")
                Turn = False
                self.MainLabel.setText("O Turn")
            else:
                self.C2.setText("O")
                Turn = True
                self.MainLabel.setText("X Turn")
        winner(self)
    def C3GamePlaye(self):
        global Turn
        if self.C3.text()!="X" and self.C3.text()!="O":
            if Turn:
                self.C3.setText("X")
                Turn = False
                self.MainLabel.setText("O Turn")
            else:
                self.C3.setText("O")
                Turn = True
                self.MainLabel.setText("X Turn")
        winner(self)
    
def winner(self):
    global Turn
    #X win
    #horzantol line
    if (self.A1.text() =="X" and self.A2.text() =="X" and self.A3.text() =="X") or (self.B1.text() =="X" and self.B2.text() =="X" and self.B3.text() =="X") or (self.C1.text() =="X" and self.C2.text() =="X" and self.C3.text() =="X"):
        self.MainLabel.setText("X Wins")
        self.A1.setEnabled(False)
        self.A2.setEnabled(False)
        self.A3.setEnabled(False)
        self.B1.setEnabled(False)
        self.B2.setEnabled(False)
        self.B3.setEnabled(False)
        self.C1.setEnabled(False)
        self.C2.setEnabled(False)
        self.C3.setEnabled(False)
        loop = QEventLoop()
        QTimer.singleShot(2000, loop.quit)
        loop.exec_()
        Turn=True
        self.MainLabel.setText("X Turn")
        self.A1.setText("")
        self.A2.setText("")
        self.A3.setText("")
        self.B1.setText("")
        self.B2.setText("")
        self.B3.setText("")
        self.C1.setText("")
        self.C2.setText("")
        self.C3.setText("")
        self.A1.setEnabled(True)
        self.A2.setEnabled(True)
        self.A3.setEnabled(True)
        self.B1.setEnabled(True)
        self.B2.setEnabled(True)
        self.B3.setEnabled(True)
        self.C1.setEnabled(True)
        self.C2.setEnabled(True)
        self.C3.setEnabled(True)
    #vertical line
    if (self.A1.text() =="X" and self.B1.text() =="X" and self.C1.text() =="X") or (self.A2.text() =="X" and self.B2.text() =="X" and self.C2.text() =="X") or (self.A3.text() =="X" and self.B3.text() =="X" and self.C3.text() =="X"):
        self.MainLabel.setText("X Wins")
        self.A1.setEnabled(False)
        self.A2.setEnabled(False)
        self.A3.setEnabled(False)
        self.B1.setEnabled(False)
        self.B2.setEnabled(False)
        self.B3.setEnabled(False)
        self.C1.setEnabled(False)
        self.C2.setEnabled(False)
        self.C3.setEnabled(False)
        loop = QEventLoop()
        QTimer.singleShot(2000, loop.quit)
        loop.exec_()
        Turn=True
        self.MainLabel.setText("X Turn")
        self.A1.setText("")
        self.A2.setText("")
        self.A3.setText("")
        self.B1.setText("")
        self.B2.setText("")
        self.B3.setText("")
        self.C1.setText("")
        self.C2.setText("")
        self.C3.setText("")
        self.A1.setEnabled(True)
        self.A2.setEnabled(True)
        self.A3.setEnabled(True)
        self.B1.setEnabled(True)
        self.B2.setEnabled(True)
        self.B3.setEnabled(True)
        self.C1.setEnabled(True)
        self.C2.setEnabled(True)
        self.C3.setEnabled(True)
    #cross line
    if (self.A1.text() =="X" and self.B2.text() =="X" and self.C3.text() =="X") or (self.A3.text() =="X" and self.B2.text() =="X" and self.C1.text() =="X"):
        self.MainLabel.setText("X Wins")
        self.A1.setEnabled(False)
        self.A2.setEnabled(False)
        self.A3.setEnabled(False)
        self.B1.setEnabled(False)
        self.B2.setEnabled(False)
        self.B3.setEnabled(False)
        self.C1.setEnabled(False)
        self.C2.setEnabled(False)
        self.C3.setEnabled(False)
        loop = QEventLoop()
        QTimer.singleShot(2000, loop.quit)
        loop.exec_()
        Turn=True
        self.MainLabel.setText("X Turn")
        self.A1.setText("")
        self.A2.setText("")
        self.A3.setText("")
        self.B1.setText("")
        self.B2.setText("")
        self.B3.setText("")
        self.C1.setText("")
        self.C2.setText("")
        self.C3.setText("")
        self.A1.setEnabled(True)
        self.A2.setEnabled(True)
        self.A3.setEnabled(True)
        self.B1.setEnabled(True)
        self.B2.setEnabled(True)
        self.B3.setEnabled(True)
        self.C1.setEnabled(True)
        self.C2.setEnabled(True)
        self.C3.setEnabled(True)
    #O Win
    #horzantol line
    if (self.A1.text() =="O" and self.A2.text() =="O" and self.A3.text() =="O") or (self.B1.text() =="O" and self.B2.text() =="O" and self.B3.text() =="O") or (self.C1.text() =="O" and self.C2.text() =="O" and self.C3.text() =="O"):
        self.MainLabel.setText("O Wins")
        self.A1.setEnabled(False)
        self.A2.setEnabled(False)
        self.A3.setEnabled(False)
        self.B1.setEnabled(False)
        self.B2.setEnabled(False)
        self.B3.setEnabled(False)
        self.C1.setEnabled(False)
        self.C2.setEnabled(False)
        self.C3.setEnabled(False)
        loop = QEventLoop()
        QTimer.singleShot(2000, loop.quit)
        loop.exec_()
        Turn=True
        self.MainLabel.setText("X Turn")
        self.A1.setText("")
        self.A2.setText("")
        self.A3.setText("")
        self.B1.setText("")
        self.B2.setText("")
        self.B3.setText("")
        self.C1.setText("")
        self.C2.setText("")
        self.C3.setText("")
        self.A1.setEnabled(True)
        self.A2.setEnabled(True)
        self.A3.setEnabled(True)
        self.B1.setEnabled(True)
        self.B2.setEnabled(True)
        self.B3.setEnabled(True)
        self.C1.setEnabled(True)
        self.C2.setEnabled(True)
        self.C3.setEnabled(True)
    #vertical line
    if (self.A1.text() =="O" and self.B1.text() =="O" and self.C1.text() =="O") or (self.A2.text() =="O" and self.B2.text() =="O" and self.C2.text() =="O") or (self.A3.text() =="O" and self.B3.text() =="O" and self.C3.text() =="O"):
        self.MainLabel.setText("O Wins")
        self.A1.setEnabled(False)
        self.A2.setEnabled(False)
        self.A3.setEnabled(False)
        self.B1.setEnabled(False)
        self.B2.setEnabled(False)
        self.B3.setEnabled(False)
        self.C1.setEnabled(False)
        self.C2.setEnabled(False)
        self.C3.setEnabled(False)
        loop = QEventLoop()
        QTimer.singleShot(2000, loop.quit)
        loop.exec_()
        Turn=True
        self.MainLabel.setText("X Turn")
        self.A1.setText("")
        self.A2.setText("")
        self.A3.setText("")
        self.B1.setText("")
        self.B2.setText("")
        self.B3.setText("")
        self.C1.setText("")
        self.C2.setText("")
        self.C3.setText("")
        self.A1.setEnabled(True)
        self.A2.setEnabled(True)
        self.A3.setEnabled(True)
        self.B1.setEnabled(True)
        self.B2.setEnabled(True)
        self.B3.setEnabled(True)
        self.C1.setEnabled(True)
        self.C2.setEnabled(True)
        self.C3.setEnabled(True)
    #cross line
    if (self.A1.text() =="O" and self.B2.text() =="O" and self.C3.text() =="O") or (self.A3.text() =="O" and self.B2.text() =="O" and self.C1.text() =="O"):
        self.MainLabel.setText("O Wins")
        self.A1.setEnabled(False)
        self.A2.setEnabled(False)
        self.A3.setEnabled(False)
        self.B1.setEnabled(False)
        self.B2.setEnabled(False)
        self.B3.setEnabled(False)
        self.C1.setEnabled(False)
        self.C2.setEnabled(False)
        self.C3.setEnabled(False)
        loop = QEventLoop()
        QTimer.singleShot(2000, loop.quit)
        loop.exec_()
        Turn=True
        self.MainLabel.setText("X Turn")
        self.A1.setText("")
        self.A2.setText("")
        self.A3.setText("")
        self.B1.setText("")
        self.B2.setText("")
        self.B3.setText("")
        self.C1.setText("")
        self.C2.setText("")
        self.C3.setText("")
        self.A1.setEnabled(True)
        self.A2.setEnabled(True)
        self.A3.setEnabled(True)
        self.B1.setEnabled(True)
        self.B2.setEnabled(True)
        self.B3.setEnabled(True)
        self.C1.setEnabled(True)
        self.C2.setEnabled(True)
        self.C3.setEnabled(True)
    #draw
    if self.A1.text() !="" and self.B1.text() !="" and self.C1.text() !="" and self.A2.text() !="" and self.B2.text() !="" and self.C2.text() !="" and self.A3.text() !="" and self.B3.text() !="" and self.C3.text() !="":
        self.MainLabel.setText("Draw")
        self.A1.setEnabled(False)
        self.A2.setEnabled(False)
        self.A3.setEnabled(False)
        self.B1.setEnabled(False)
        self.B2.setEnabled(False)
        self.B3.setEnabled(False)
        self.C1.setEnabled(False)
        self.C2.setEnabled(False)
        self.C3.setEnabled(False)
        loop = QEventLoop()
        QTimer.singleShot(2000, loop.quit)
        loop.exec_()
        Turn=True
        self.MainLabel.setText("X Turn")
        self.A1.setText("")
        self.A2.setText("")
        self.A3.setText("")
        self.B1.setText("")
        self.B2.setText("")
        self.B3.setText("")
        self.C1.setText("")
        self.C2.setText("")
        self.C3.setText("")
        self.A1.setEnabled(True)
        self.A2.setEnabled(True)
        self.A3.setEnabled(True)
        self.B1.setEnabled(True)
        self.B2.setEnabled(True)
        self.B3.setEnabled(True)
        self.C1.setEnabled(True)
        self.C2.setEnabled(True)
        self.C3.setEnabled(True)









if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MyWindow()
    main.show()
    sys.exit(app.exec_())