# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NumberRandomizer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NumberRandomizer(object):
    def setupUi(self, NumberRandomizer):
        
        NumberRandomizer.setObjectName("NumberRandomizer")
        NumberRandomizer.setEnabled(True)
        NumberRandomizer.resize(432, 340)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NumberRandomizer.sizePolicy().hasHeightForWidth())
        NumberRandomizer.setSizePolicy(sizePolicy)
        NumberRandomizer.setMinimumSize(QtCore.QSize(432, 340))
        NumberRandomizer.setMaximumSize(QtCore.QSize(432, 340))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/die_icon31024.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NumberRandomizer.setWindowIcon(icon)
        NumberRandomizer.setIconSize(QtCore.QSize(512, 512))
        NumberRandomizer.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(NumberRandomizer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(432, 320))
        self.centralwidget.setObjectName("centralwidget")
        self.NumbersFrame = QtWidgets.QFrame(self.centralwidget)
        self.NumbersFrame.setGeometry(QtCore.QRect(10, 20, 411, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NumbersFrame.sizePolicy().hasHeightForWidth())
        self.NumbersFrame.setSizePolicy(sizePolicy)
        self.NumbersFrame.setStyleSheet("QFrame{\n"
"border-color: rgba(212, 212, 212, 1);\n"
"border-width : 1px;\n"
"border-style: solid;\n"
"border-radius: 7px;\n"
"}")
        self.NumbersFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.NumbersFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.NumbersFrame.setObjectName("NumbersFrame")
        self.Btn7 = QtWidgets.QPushButton(self.NumbersFrame)
        self.Btn7.setGeometry(QtCore.QRect(278, 29, 40, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn7.sizePolicy().hasHeightForWidth())
        self.Btn7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Btn7.setFont(font)
        self.Btn7.setMouseTracking(False)
        self.Btn7.setText("7")
        self.Btn7.setObjectName("Btn7")
        self.buttonGroup = QtWidgets.QButtonGroup(NumberRandomizer)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.Btn7)
        self.Btn9 = QtWidgets.QPushButton(self.NumbersFrame)
        self.Btn9.setGeometry(QtCore.QRect(370, 29, 40, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn9.sizePolicy().hasHeightForWidth())
        self.Btn9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Btn9.setFont(font)
        self.Btn9.setMouseTracking(False)
        self.Btn9.setText("9")
        self.Btn9.setObjectName("Btn9")
        self.buttonGroup.addButton(self.Btn9)
        self.Btn2 = QtWidgets.QPushButton(self.NumbersFrame)
        self.Btn2.setGeometry(QtCore.QRect(48, 29, 40, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn2.sizePolicy().hasHeightForWidth())
        self.Btn2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Btn2.setFont(font)
        self.Btn2.setMouseTracking(False)
        self.Btn2.setText("2")
        self.Btn2.setObjectName("Btn2")
        self.buttonGroup.addButton(self.Btn2)
        self.Btn4 = QtWidgets.QPushButton(self.NumbersFrame)
        self.Btn4.setGeometry(QtCore.QRect(140, 29, 40, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn4.sizePolicy().hasHeightForWidth())
        self.Btn4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Btn4.setFont(font)
        self.Btn4.setMouseTracking(False)
        self.Btn4.setText("4")
        self.Btn4.setObjectName("Btn4")
        self.buttonGroup.addButton(self.Btn4)
        self.Btn8 = QtWidgets.QPushButton(self.NumbersFrame)
        self.Btn8.setGeometry(QtCore.QRect(324, 29, 40, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn8.sizePolicy().hasHeightForWidth())
        self.Btn8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Btn8.setFont(font)
        self.Btn8.setMouseTracking(False)
        self.Btn8.setText("8")
        self.Btn8.setObjectName("Btn8")
        self.buttonGroup.addButton(self.Btn8)
        self.Btn5 = QtWidgets.QPushButton(self.NumbersFrame)
        self.Btn5.setGeometry(QtCore.QRect(186, 29, 40, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn5.sizePolicy().hasHeightForWidth())
        self.Btn5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Btn5.setFont(font)
        self.Btn5.setMouseTracking(False)
        self.Btn5.setText("5")
        self.Btn5.setObjectName("Btn5")
        self.buttonGroup.addButton(self.Btn5)
        self.Btn6 = QtWidgets.QPushButton(self.NumbersFrame)
        self.Btn6.setGeometry(QtCore.QRect(232, 29, 40, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn6.sizePolicy().hasHeightForWidth())
        self.Btn6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Btn6.setFont(font)
        self.Btn6.setMouseTracking(False)
        self.Btn6.setText("6")
        self.Btn6.setObjectName("Btn6")
        self.buttonGroup.addButton(self.Btn6)
        self.Btn1 = QtWidgets.QPushButton(self.NumbersFrame)
        self.Btn1.setGeometry(QtCore.QRect(1, 29, 40, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn1.sizePolicy().hasHeightForWidth())
        self.Btn1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Btn1.setFont(font)
        self.Btn1.setMouseTracking(False)
        self.Btn1.setText("1")
        self.Btn1.setObjectName("Btn1")
        self.buttonGroup.addButton(self.Btn1)
        self.Btn3 = QtWidgets.QPushButton(self.NumbersFrame)
        self.Btn3.setGeometry(QtCore.QRect(94, 29, 40, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn3.sizePolicy().hasHeightForWidth())
        self.Btn3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Btn3.setFont(font)
        self.Btn3.setMouseTracking(False)
        self.Btn3.setText("3")
        self.Btn3.setObjectName("Btn3")
        self.buttonGroup.addButton(self.Btn3)
        self.RepeatFrame = QtWidgets.QFrame(self.centralwidget)
        self.RepeatFrame.setGeometry(QtCore.QRect(281, 110, 140, 120))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RepeatFrame.sizePolicy().hasHeightForWidth())
        self.RepeatFrame.setSizePolicy(sizePolicy)
        self.RepeatFrame.setStyleSheet("QFrame{\n"
"border-color: rgba(212, 212, 212, 1);\n"
"border-width : 1px;\n"
"border-style: solid;\n"
"border-radius: 7px;\n"
"}")
        self.RepeatFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RepeatFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RepeatFrame.setObjectName("RepeatFrame")
        self.RepeatSpinBox = QtWidgets.QSpinBox(self.RepeatFrame)
        self.RepeatSpinBox.setGeometry(QtCore.QRect(80, 30, 42, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RepeatSpinBox.sizePolicy().hasHeightForWidth())
        self.RepeatSpinBox.setSizePolicy(sizePolicy)
        self.RepeatSpinBox.setMinimum(1)
        self.RepeatSpinBox.setMaximum(999)
        self.RepeatSpinBox.setObjectName("RepeatSpinBox")
        self.RepeatRadioButton = QtWidgets.QRadioButton(self.RepeatFrame)
        self.RepeatRadioButton.setGeometry(QtCore.QRect(10, 30, 60, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RepeatRadioButton.sizePolicy().hasHeightForWidth())
        self.RepeatRadioButton.setSizePolicy(sizePolicy)
        self.RepeatRadioButton.setIconSize(QtCore.QSize(16, 16))
        self.RepeatRadioButton.setChecked(False)
        self.RepeatRadioButton.setAutoRepeat(False)
        self.RepeatRadioButton.setAutoExclusive(True)
        self.RepeatRadioButton.setAutoRepeatDelay(0)
        self.RepeatRadioButton.setObjectName("RepeatRadioButton")
        self.InfiniteRadioButton = QtWidgets.QRadioButton(self.RepeatFrame)
        self.InfiniteRadioButton.setGeometry(QtCore.QRect(10, 70, 132, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InfiniteRadioButton.sizePolicy().hasHeightForWidth())
        self.InfiniteRadioButton.setSizePolicy(sizePolicy)
        self.InfiniteRadioButton.setChecked(True)
        self.InfiniteRadioButton.setObjectName("InfiniteRadioButton")
        self.bottomBtnFrame = QtWidgets.QFrame(self.centralwidget)
        self.bottomBtnFrame.setGeometry(QtCore.QRect(10, 240, 411, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottomBtnFrame.sizePolicy().hasHeightForWidth())
        self.bottomBtnFrame.setSizePolicy(sizePolicy)
        self.bottomBtnFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottomBtnFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottomBtnFrame.setObjectName("bottomBtnFrame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.bottomBtnFrame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 281, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalLayoutWidget.sizePolicy().hasHeightForWidth())
        self.horizontalLayoutWidget.setSizePolicy(sizePolicy)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.StartBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartBtn.sizePolicy().hasHeightForWidth())
        self.StartBtn.setSizePolicy(sizePolicy)
        self.StartBtn.setObjectName("StartBtn")
        self.horizontalLayout.addWidget(self.StartBtn)
        self.StopBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.StopBtn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StopBtn.sizePolicy().hasHeightForWidth())
        self.StopBtn.setSizePolicy(sizePolicy)
        self.StopBtn.setAutoDefault(False)
        self.StopBtn.setObjectName("StopBtn")
        self.horizontalLayout.addWidget(self.StopBtn)
        self.ShortcutFrame = QtWidgets.QFrame(self.bottomBtnFrame)
        self.ShortcutFrame.setGeometry(QtCore.QRect(280, 0, 131, 81))
        self.ShortcutFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ShortcutFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ShortcutFrame.setObjectName("ShortcutFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ShortcutFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.shortcut_edit = QtWidgets.QKeySequenceEdit(self.ShortcutFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shortcut_edit.sizePolicy().hasHeightForWidth())
        self.shortcut_edit.setSizePolicy(sizePolicy)
        self.shortcut_edit.setStyleSheet("qproperty-alignment: AlignCenter;")
        self.shortcut_edit.setKeySequence("")
        self.shortcut_edit.setObjectName("shortcut_edit")
        self.verticalLayout_2.addWidget(self.shortcut_edit)
        self.HotkeyBtn = QtWidgets.QPushButton(self.ShortcutFrame)
        self.HotkeyBtn.setObjectName("HotkeyBtn")
        self.verticalLayout_2.addWidget(self.HotkeyBtn)
        self.DelayLabel = QtWidgets.QLabel(self.centralwidget)
        self.DelayLabel.setGeometry(QtCore.QRect(20, 103, 30, 13))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DelayLabel.sizePolicy().hasHeightForWidth())
        self.DelayLabel.setSizePolicy(sizePolicy)
        self.DelayLabel.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.DelayLabel.setObjectName("DelayLabel")
        self.NumbersLabel = QtWidgets.QLabel(self.centralwidget)
        self.NumbersLabel.setGeometry(QtCore.QRect(20, 13, 44, 13))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NumbersLabel.sizePolicy().hasHeightForWidth())
        self.NumbersLabel.setSizePolicy(sizePolicy)
        self.NumbersLabel.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.NumbersLabel.setObjectName("NumbersLabel")
        self.RepeatLabel = QtWidgets.QLabel(self.centralwidget)
        self.RepeatLabel.setGeometry(QtCore.QRect(291, 103, 37, 13))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RepeatLabel.sizePolicy().hasHeightForWidth())
        self.RepeatLabel.setSizePolicy(sizePolicy)
        self.RepeatLabel.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"")
        self.RepeatLabel.setObjectName("RepeatLabel")
        self.MiddleFrame = QtWidgets.QFrame(self.centralwidget)
        self.MiddleFrame.setGeometry(QtCore.QRect(160, 110, 111, 121))
        self.MiddleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MiddleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MiddleFrame.setObjectName("MiddleFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.MiddleFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SelectAllBtn = QtWidgets.QPushButton(self.MiddleFrame)
        self.SelectAllBtn.setObjectName("SelectAllBtn")
        self.verticalLayout.addWidget(self.SelectAllBtn)
        self.DeselectAllBtn = QtWidgets.QPushButton(self.MiddleFrame)
        self.DeselectAllBtn.setObjectName("DeselectAllBtn")
        self.verticalLayout.addWidget(self.DeselectAllBtn)
        self.DelayFrame = QtWidgets.QFrame(self.centralwidget)
        self.DelayFrame.setGeometry(QtCore.QRect(10, 110, 140, 120))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DelayFrame.sizePolicy().hasHeightForWidth())
        self.DelayFrame.setSizePolicy(sizePolicy)
        self.DelayFrame.setStyleSheet("QFrame{\n"
"border-color: rgba(212, 212, 212, 1);\n"
"border-width : 1px;\n"
"border-style: solid;\n"
"border-radius: 7px;\n"
"}")
        self.DelayFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DelayFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DelayFrame.setObjectName("DelayFrame")
        self.TimeSpinBox = QtWidgets.QSpinBox(self.DelayFrame)
        self.TimeSpinBox.setGeometry(QtCore.QRect(88, 30, 48, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TimeSpinBox.sizePolicy().hasHeightForWidth())
        self.TimeSpinBox.setSizePolicy(sizePolicy)
        self.TimeSpinBox.setMinimum(0)
        self.TimeSpinBox.setMaximum(9999)
        self.TimeSpinBox.setObjectName("TimeSpinBox")
        self.TimeRadioButton = QtWidgets.QRadioButton(self.DelayFrame)
        self.TimeRadioButton.setGeometry(QtCore.QRect(10, 30, 75, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TimeRadioButton.sizePolicy().hasHeightForWidth())
        self.TimeRadioButton.setSizePolicy(sizePolicy)
        self.TimeRadioButton.setIconSize(QtCore.QSize(16, 16))
        self.TimeRadioButton.setChecked(False)
        self.TimeRadioButton.setAutoRepeat(False)
        self.TimeRadioButton.setAutoExclusive(True)
        self.TimeRadioButton.setAutoRepeatDelay(0)
        self.TimeRadioButton.setObjectName("TimeRadioButton")
        self.OnClickRadioButton = QtWidgets.QRadioButton(self.DelayFrame)
        self.OnClickRadioButton.setGeometry(QtCore.QRect(10, 70, 132, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OnClickRadioButton.sizePolicy().hasHeightForWidth())
        self.OnClickRadioButton.setSizePolicy(sizePolicy)
        self.OnClickRadioButton.setChecked(True)
        self.OnClickRadioButton.setObjectName("OnClickRadioButton")
        self.DelayFrame.raise_()
        self.NumbersFrame.raise_()
        self.RepeatFrame.raise_()
        self.bottomBtnFrame.raise_()
        self.DelayLabel.raise_()
        self.NumbersLabel.raise_()
        self.RepeatLabel.raise_()
        self.MiddleFrame.raise_()
        NumberRandomizer.setCentralWidget(self.centralwidget)

        self.retranslateUi(NumberRandomizer)
        QtCore.QMetaObject.connectSlotsByName(NumberRandomizer)
        NumberRandomizer.setTabOrder(self.Btn1, self.Btn2)
        NumberRandomizer.setTabOrder(self.Btn2, self.Btn3)
        NumberRandomizer.setTabOrder(self.Btn3, self.Btn4)
        NumberRandomizer.setTabOrder(self.Btn4, self.Btn5)
        NumberRandomizer.setTabOrder(self.Btn5, self.Btn6)
        NumberRandomizer.setTabOrder(self.Btn6, self.Btn7)
        NumberRandomizer.setTabOrder(self.Btn7, self.Btn8)
        NumberRandomizer.setTabOrder(self.Btn8, self.Btn9)

    def retranslateUi(self, NumberRandomizer):
        _translate = QtCore.QCoreApplication.translate
        NumberRandomizer.setWindowTitle(_translate("NumberRandomizer", "Number Randomizer"))
        self.Btn7.setShortcut(_translate("NumberRandomizer", "7"))
        self.Btn9.setShortcut(_translate("NumberRandomizer", "9"))
        self.Btn2.setShortcut(_translate("NumberRandomizer", "2"))
        self.Btn4.setShortcut(_translate("NumberRandomizer", "4"))
        self.Btn8.setShortcut(_translate("NumberRandomizer", "8"))
        self.Btn5.setShortcut(_translate("NumberRandomizer", "5"))
        self.Btn6.setShortcut(_translate("NumberRandomizer", "6"))
        self.Btn1.setShortcut(_translate("NumberRandomizer", "1"))
        self.Btn3.setShortcut(_translate("NumberRandomizer", "3"))
        self.RepeatRadioButton.setText(_translate("NumberRandomizer", "Repeat"))
        self.InfiniteRadioButton.setText(_translate("NumberRandomizer", "Repeat Until Stopped"))
        self.StartBtn.setText(_translate("NumberRandomizer", "Start"))
        self.StopBtn.setText(_translate("NumberRandomizer", "Stop"))
        self.HotkeyBtn.setText(_translate("NumberRandomizer", "Save"))
        self.DelayLabel.setText(_translate("NumberRandomizer", "Delay"))
        self.NumbersLabel.setText(_translate("NumberRandomizer", "Numbers"))
        self.RepeatLabel.setText(_translate("NumberRandomizer", "Repeat"))
        self.SelectAllBtn.setText(_translate("NumberRandomizer", "Select All"))
        self.DeselectAllBtn.setText(_translate("NumberRandomizer", "Deselect All"))
        self.TimeRadioButton.setText(_translate("NumberRandomizer", "Milliseconds"))
        self.OnClickRadioButton.setText(_translate("NumberRandomizer", "On Click"))
import images
