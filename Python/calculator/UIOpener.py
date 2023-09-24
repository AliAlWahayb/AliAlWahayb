import sys
import os
import time
import PyQt5
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QMainWindow,QPushButton,QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import uic


class MyWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)

        # Load the UI Page - added path too
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "Calcularor.ui"), self)
        #Num pad definitions & functions
        self.BN0.clicked.connect(self.method_0)
        self.BN1.clicked.connect(self.method_1)
        self.BN2.clicked.connect(self.method_2)
        self.BN3.clicked.connect(self.method_3)
        self.BN4.clicked.connect(self.method_4)
        self.BN5.clicked.connect(self.method_5)
        self.BN6.clicked.connect(self.method_6)
        self.BN7.clicked.connect(self.method_7)
        self.BN8.clicked.connect(self.method_8)
        self.BN9.clicked.connect(self.method_9)
        self.PanelLable=self.findChild(QLabel,"PanelLable")
        #operation defintions & functions
        self.BDot.clicked.connect(self.method_Dot)
        self.BDivide.clicked.connect(self.method_Divide)
        self.BPlus.clicked.connect(self.method_Plus)
        self.BMinus.clicked.connect(self.method_Minus)
        self.BMultible.clicked.connect(self.method_Multible)
        self.BEqual.clicked.connect(self.method_Equal)
        self.BDelet.clicked.connect(self.method_Delet)
        self.BClear.clicked.connect(self.method_Clear)
        

    def method_0 (self):
            text = self.PanelLable.text()
            self.PanelLable.setText(text+"0")
    def method_1 (self):
            text = self.PanelLable.text()
            self.PanelLable.setText(text+"1")        
    def method_2 (self):
            text = self.PanelLable.text()
            self.PanelLable.setText(text+"2")
    def method_3 (self):
            text = self.PanelLable.text()
            self.PanelLable.setText(text+"3")
    def method_4 (self):
            text = self.PanelLable.text()
            self.PanelLable.setText(text+"4")
    def method_5 (self):
            text = self.PanelLable.text()
            self.PanelLable.setText(text+"5")
    def method_6 (self):
            text = self.PanelLable.text()
            self.PanelLable.setText(text+"6")
    def method_7 (self):
            text = self.PanelLable.text()
            self.PanelLable.setText(text+"7")
    def method_8 (self):
            text = self.PanelLable.text()
            self.PanelLable.setText(text+"8")
    def method_9 (self):
            text = self.PanelLable.text()
            self.PanelLable.setText(text+"9")
    def method_Dot (self):
            text = self.PanelLable.text()
            self.PanelLable.setText(text+".")
    def method_Plus (self):
            text = self.PanelLable.text()
            self.PanelLable.setText(text+"+")
    def method_Minus (self):
            text = self.PanelLable.text()
            self.PanelLable.setText(text+"-")
    def method_Divide (self):
            text = self.PanelLable.text()
            self.PanelLable.setText(text+"/")
    def method_Multible (self):
            text = self.PanelLable.text()
            self.PanelLable.setText(text+"*")
    def method_Delet (self):
            text = self.PanelLable.text()
            self.PanelLable.setText(text[:len(text)-1])
    def method_Clear (self):
            self.PanelLable.setText("")
    def method_Equal (self):
            text = self.PanelLable.text()
            try:
                answer=eval(text)
                self.PanelLable.setText(str(answer))
            except:
                self.PanelLable.setText("wrong Input")
                







if __name__ == '__main__':  
    app = QtWidgets.QApplication(sys.argv)
    main = MyWindow()
    main.show()
    sys.exit(app.exec_())