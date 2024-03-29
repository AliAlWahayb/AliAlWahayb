# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calcularor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(500, 600)
        icon = QtGui.QIcon(os.path.join("icons","icons8_calculator_100px_2.png"))
        icon.addPixmap(QtGui.QPixmap(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Calculator.setWindowIcon(icon)
        Calculator.setStyleSheet("background-color:#05263B;\n"
"opacity: 0.8;")
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.ButtonFrame = QtWidgets.QFrame(self.centralwidget)
        self.ButtonFrame.setGeometry(QtCore.QRect(50, 270, 400, 250))
        self.ButtonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ButtonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ButtonFrame.setObjectName("ButtonFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.ButtonFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.BMinus = QtWidgets.QPushButton(self.ButtonFrame)
        self.BMinus.setStyleSheet("QPushButton:hover{\n"
"    background-color: #163B50;\n"
"}\n"
"")
        self.BMinus.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(os.path.join("icons","icons8_subtract_100px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BMinus.setIcon(icon1)
        self.BMinus.setIconSize(QtCore.QSize(55, 50))
        self.BMinus.setObjectName("BMinus")
        self.gridLayout.addWidget(self.BMinus, 2, 3, 1, 1)
        self.BN2 = QtWidgets.QPushButton(self.ButtonFrame)
        self.BN2.setStyleSheet("QPushButton:hover{\n"
"    background-color: #163B50;\n"
"}\n"
"")
        self.BN2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(os.path.join("icons","icons8_2_100px_1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BN2.setIcon(icon2)
        self.BN2.setIconSize(QtCore.QSize(55, 50))
        self.BN2.setObjectName("BN2")
        self.gridLayout.addWidget(self.BN2, 2, 1, 1, 1)
        self.BN4 = QtWidgets.QPushButton(self.ButtonFrame)
        self.BN4.setAutoFillBackground(False)
        self.BN4.setStyleSheet("QPushButton:hover{\n"
"    background-color: #163B50;\n"
"}\n"
"")
        self.BN4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(os.path.join("icons","icons8_4_100px_1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BN4.setIcon(icon3)
        self.BN4.setIconSize(QtCore.QSize(55, 50))
        self.BN4.setObjectName("BN4")
        self.gridLayout.addWidget(self.BN4, 1, 0, 1, 1)
        self.BDot = QtWidgets.QPushButton(self.ButtonFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.BDot.sizePolicy().hasHeightForWidth())
        self.BDot.setSizePolicy(sizePolicy)
        self.BDot.setStyleSheet("QPushButton:hover{\n"
"    background-color: #163B50;\n"
"}\n"
"")
        self.BDot.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(os.path.join("icons","icons8_filled_circle_100px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BDot.setIcon(icon4)
        self.BDot.setIconSize(QtCore.QSize(55, 14))
        self.BDot.setObjectName("BDot")
        self.gridLayout.addWidget(self.BDot, 3, 2, 1, 1)
        self.BMultible = QtWidgets.QPushButton(self.ButtonFrame)
        self.BMultible.setStyleSheet("QPushButton:hover{\n"
"    background-color: #163B50;\n"
"}\n"
"")
        self.BMultible.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(os.path.join("icons","icons8_multiply_100px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BMultible.setIcon(icon5)
        self.BMultible.setIconSize(QtCore.QSize(55, 50))
        self.BMultible.setObjectName("BMultible")
        self.gridLayout.addWidget(self.BMultible, 0, 3, 1, 1)
        self.BDivide = QtWidgets.QPushButton(self.ButtonFrame)
        self.BDivide.setAutoFillBackground(False)
        self.BDivide.setStyleSheet("QPushButton:hover{\n"
"    background-color: #163B50;\n"
"}\n"
"")
        self.BDivide.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(os.path.join("icons","icons8_divide_100px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BDivide.setIcon(icon6)
        self.BDivide.setIconSize(QtCore.QSize(55, 50))
        self.BDivide.setObjectName("BDivide")
        self.gridLayout.addWidget(self.BDivide, 1, 3, 1, 1)
        self.BN8 = QtWidgets.QPushButton(self.ButtonFrame)
        self.BN8.setStyleSheet("QPushButton:hover{\n"
"    background-color: #163B50;\n"
"}\n"
"")
        self.BN8.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(os.path.join("icons","icons8_8_100px_1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BN8.setIcon(icon7)
        self.BN8.setIconSize(QtCore.QSize(55, 50))
        self.BN8.setObjectName("BN8")
        self.gridLayout.addWidget(self.BN8, 0, 1, 1, 1)
        self.BEqual = QtWidgets.QPushButton(self.ButtonFrame)
        self.BEqual.setStyleSheet("QPushButton:hover{\n"
"    background-color: #163B50;\n"
"}\n"
"")
        self.BEqual.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(os.path.join("icons","icons8_equal_sign_100px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BEqual.setIcon(icon8)
        self.BEqual.setIconSize(QtCore.QSize(55, 50))
        self.BEqual.setObjectName("BEqual")
        self.gridLayout.addWidget(self.BEqual, 3, 0, 1, 1)
        self.BPlus = QtWidgets.QPushButton(self.ButtonFrame)
        self.BPlus.setStyleSheet("QPushButton:hover{\n"
"    background-color: #163B50;\n"
"}\n"
"")
        self.BPlus.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(os.path.join("icons","icons8_plus_math_100px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BPlus.setIcon(icon9)
        self.BPlus.setIconSize(QtCore.QSize(55, 50))
        self.BPlus.setObjectName("BPlus")
        self.gridLayout.addWidget(self.BPlus, 3, 3, 1, 1)
        self.BN1 = QtWidgets.QPushButton(self.ButtonFrame)
        self.BN1.setStyleSheet("QPushButton:hover{\n"
"    background-color: #163B50;\n"
"}\n"
"")
        self.BN1.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(os.path.join("icons","icons8_1_100px_1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BN1.setIcon(QtGui.QIcon(icon10))
        self.BN1.setIconSize(QtCore.QSize(55, 50))
        self.BN1.setObjectName("BN1")
        self.gridLayout.addWidget(self.BN1, 2, 0, 1, 1)
        self.BN3 = QtWidgets.QPushButton(self.ButtonFrame)
        self.BN3.setStyleSheet("QPushButton:hover{\n"
"    background-color: #163B50;\n"
"}\n"
"")
        self.BN3.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(os.path.join("icons","icons8_3_100px_2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BN3.setIcon(icon11)
        self.BN3.setIconSize(QtCore.QSize(55, 50))
        self.BN3.setObjectName("BN3")
        self.gridLayout.addWidget(self.BN3, 2, 2, 1, 1)
        self.BN0 = QtWidgets.QPushButton(self.ButtonFrame)
        self.BN0.setStyleSheet("QPushButton:hover{\n"
"    background-color: #163B50;\n"
"}\n"
"")
        self.BN0.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(os.path.join("icons","icons8_0_100px_2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BN0.setIcon(icon12)
        self.BN0.setIconSize(QtCore.QSize(55, 50))
        self.BN0.setObjectName("BN0")
        self.gridLayout.addWidget(self.BN0, 3, 1, 1, 1)
        self.BN7 = QtWidgets.QPushButton(self.ButtonFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BN7.sizePolicy().hasHeightForWidth())
        self.BN7.setSizePolicy(sizePolicy)
        self.BN7.setStyleSheet("QPushButton:hover{\n"
"    background-color: #163B50;\n"
"}\n"
"")
        self.BN7.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(os.path.join("icons","icons8_7_100px_1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BN7.setIcon(icon13)
        self.BN7.setIconSize(QtCore.QSize(55, 50))
        self.BN7.setObjectName("BN7")
        self.gridLayout.addWidget(self.BN7, 0, 0, 1, 1)
        self.BN9 = QtWidgets.QPushButton(self.ButtonFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.BN9.sizePolicy().hasHeightForWidth())
        self.BN9.setSizePolicy(sizePolicy)
        self.BN9.setStyleSheet("QPushButton:hover{\n"
"    background-color: #163B50;\n"
"}\n"
"")
        self.BN9.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(os.path.join("icons","icons8_9_100px_1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BN9.setIcon(icon14)
        self.BN9.setIconSize(QtCore.QSize(55, 50))
        self.BN9.setObjectName("BN9")
        self.gridLayout.addWidget(self.BN9, 0, 2, 1, 1)
        self.BN6 = QtWidgets.QPushButton(self.ButtonFrame)
        self.BN6.setMinimumSize(QtCore.QSize(9, 6))
        self.BN6.setSizeIncrement(QtCore.QSize(35, 17))
        self.BN6.setBaseSize(QtCore.QSize(14, 17))
        self.BN6.setStyleSheet("QPushButton:hover{\n"
"    background-color: #163B50;\n"
"}\n"
"")
        self.BN6.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(os.path.join("icons","icons8_6_100px_1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BN6.setIcon(icon15)
        self.BN6.setIconSize(QtCore.QSize(55, 50))
        self.BN6.setObjectName("BN6")
        self.gridLayout.addWidget(self.BN6, 1, 2, 1, 1)
        self.BN5 = QtWidgets.QPushButton(self.ButtonFrame)
        self.BN5.setStyleSheet("QPushButton:hover{\n"
"    background-color: #163B50;\n"
"}\n"
"\n"
"")
        self.BN5.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(os.path.join("icons","icons8_5_100px_1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BN5.setIcon(icon16)
        self.BN5.setIconSize(QtCore.QSize(55, 50))
        self.BN5.setObjectName("BN5")
        self.gridLayout.addWidget(self.BN5, 1, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(60, 40, 371, 111))
        self.frame.setStyleSheet("background-color:#163B50;\n"
"border:#9CA6B8;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.PanelLable = QtWidgets.QLabel(self.frame)
        self.PanelLable.setGeometry(QtCore.QRect(6, 2, 361, 101))
        font = QtGui.QFont()
        font.setFamily("Dosis Light")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.PanelLable.setFont(font)
        self.PanelLable.setStyleSheet("")
        self.PanelLable.setText("")
        self.PanelLable.setObjectName("PanelLable")
        self.BClear = QtWidgets.QPushButton(self.centralwidget)
        self.BClear.setGeometry(QtCore.QRect(60, 210, 91, 53))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BClear.sizePolicy().hasHeightForWidth())
        self.BClear.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(33)
        self.BClear.setFont(font)
        self.BClear.setStyleSheet("\n"
"QPushButton:hover{\n"
"    background-color: #163B50;\n"
"}\n"
"")
        self.BClear.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(os.path.join("icons","icons8_circled_c_100px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BClear.setIcon(icon17)
        self.BClear.setIconSize(QtCore.QSize(55, 50))
        self.BClear.setObjectName("BClear")
        self.BDelet = QtWidgets.QPushButton(self.centralwidget)
        self.BDelet.setGeometry(QtCore.QRect(350, 210, 91, 53))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BDelet.sizePolicy().hasHeightForWidth())
        self.BDelet.setSizePolicy(sizePolicy)
        self.BDelet.setStyleSheet("QPushButton:hover{\n"
"    background-color: #163B50;\n"
"}\n"
"")
        self.BDelet.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(os.path.join("icons","icons8_clear_symbol_100px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BDelet.setIcon(icon18)
        self.BDelet.setIconSize(QtCore.QSize(55, 50))
        self.BDelet.setObjectName("BDelet")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 550, 101, 16))
        self.label.setStyleSheet("color: rgb(255, 248, 246);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 550, 101, 16))
        self.label_2.setStyleSheet("color: rgb(255, 248, 246);")
        self.label_2.setObjectName("label_2")
        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)
        
        #The start of my code
        #number Buttons
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
        #operations buttons
        self.BDot.clicked.connect(self.method_Dot)
        self.BDivide.clicked.connect(self.method_Divide)
        self.BPlus.clicked.connect(self.method_Plus)
        self.BMinus.clicked.connect(self.method_Minus)
        self.BMultible.clicked.connect(self.method_Multible)
        self.BEqual.clicked.connect(self.method_Equal)
        self.BDelet.clicked.connect(self.method_Delet)
        self.BClear.clicked.connect(self.method_Clear)
        
        #Methods
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
        #end of my code


    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.BMinus.setShortcut(_translate("Calculator", "-"))
        self.BN2.setShortcut(_translate("Calculator", "2"))
        self.BN4.setShortcut(_translate("Calculator", "4"))
        self.BDot.setShortcut(_translate("Calculator", "."))
        self.BMultible.setShortcut(_translate("Calculator", "*"))
        self.BDivide.setShortcut(_translate("Calculator", "/"))
        self.BN8.setShortcut(_translate("Calculator", "8"))
        self.BEqual.setShortcut(_translate("Calculator", "Enter"))
        self.BPlus.setShortcut(_translate("Calculator", "+"))
        self.BN1.setShortcut(_translate("Calculator", "1"))
        self.BN3.setShortcut(_translate("Calculator", "3"))
        self.BN0.setShortcut(_translate("Calculator", "0"))
        self.BN7.setShortcut(_translate("Calculator", "7"))
        self.BN9.setShortcut(_translate("Calculator", "9"))
        self.BN6.setShortcut(_translate("Calculator", "6"))
        self.BN5.setShortcut(_translate("Calculator", "5"))
        self.BClear.setShortcut(_translate("Calculator", "C"))
        self.BDelet.setShortcut(_translate("Calculator", "Backspace"))
        self.label.setText(_translate("Calculator", "Crated By Alisaw"))
        self.label_2.setText(_translate("Calculator", "1/12/2023"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
