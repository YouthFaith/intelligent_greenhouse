# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passwd_verify.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from widget.number_button import MyPushButton

class Ui_passwd(object):
    def setupUi(self, passwd):
        passwd.setObjectName("passwd")
        passwd.resize(642, 426)
        passwd.setStyleSheet("color: rgb(86, 118, 162);")
        self.gridLayout_2 = QtWidgets.QGridLayout(passwd)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(159, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.show_passwd = QtWidgets.QLabel(passwd)
        self.show_passwd.setMinimumSize(QtCore.QSize(281, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.show_passwd.setFont(font)
        self.show_passwd.setStyleSheet("    border-style: outset;\n"
"    border-radius: 8px;\n"
"    color: rgb(86, 118, 162);\n"
"    border:2px solid rgb(186, 189, 182);")
        self.show_passwd.setText("")
        self.show_passwd.setAlignment(QtCore.Qt.AlignCenter)
        self.show_passwd.setObjectName("show_passwd")
        self.verticalLayout.addWidget(self.show_passwd)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.number_1 = MyPushButton(passwd)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.number_1.setFont(font)
        self.number_1.setStyleSheet("QPushButton{\n"
"    background-color:rgba(100,225,100,30);\n"
"    border-style:outset;\n"
"    border-width:4px;\n"
"    border-radius:10px;\n"
"    border-color:rgba(255,255,255,30);\n"
"    color:rgba(0,0,0,100);\n"
"}\n"
"\n"
"QPushButton:hover:pressed{\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-color:rgb(170, 170, 255);\n"
"    border-style:outside;\n"
"    color:rgb(0, 170, 127);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed{\n"
"    background-color:rgb(0, 255, 127);\n"
"    border-color:rgb(170, 255, 255);\n"
"    color:rgb(85, 170, 255);\n"
"}")
        self.number_1.setObjectName("number_1")
        self.gridLayout.addWidget(self.number_1, 0, 0, 1, 1)
        self.number_2 = MyPushButton(passwd)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.number_2.setFont(font)
        self.number_2.setStyleSheet("QPushButton{\n"
"    background-color:rgba(100,225,100,30);\n"
"    border-style:outset;\n"
"    border-width:4px;\n"
"    border-radius:10px;\n"
"    border-color:rgba(255,255,255,30);\n"
"    color:rgba(0,0,0,100);\n"
"}\n"
"\n"
"QPushButton:hover:pressed{\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-color:rgb(170, 170, 255);\n"
"    border-style:outside;\n"
"    color:rgb(0, 170, 127);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed{\n"
"    background-color:rgb(0, 255, 127);\n"
"    border-color:rgb(170, 255, 255);\n"
"    color:rgb(85, 170, 255);\n"
"}")
        self.number_2.setObjectName("number_2")
        self.gridLayout.addWidget(self.number_2, 0, 1, 1, 1)
        self.number_3 = MyPushButton(passwd)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.number_3.setFont(font)
        self.number_3.setStyleSheet("QPushButton{\n"
"    background-color:rgba(100,225,100,30);\n"
"    border-style:outset;\n"
"    border-width:4px;\n"
"    border-radius:10px;\n"
"    border-color:rgba(255,255,255,30);\n"
"    color:rgba(0,0,0,100);\n"
"}\n"
"\n"
"QPushButton:hover:pressed{\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-color:rgb(170, 170, 255);\n"
"    border-style:outside;\n"
"    color:rgb(0, 170, 127);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed{\n"
"    background-color:rgb(0, 255, 127);\n"
"    border-color:rgb(170, 255, 255);\n"
"    color:rgb(85, 170, 255);\n"
"}")
        self.number_3.setObjectName("number_3")
        self.gridLayout.addWidget(self.number_3, 0, 2, 1, 1)
        self.number_4 = MyPushButton(passwd)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.number_4.setFont(font)
        self.number_4.setStyleSheet("QPushButton{\n"
"    background-color:rgba(100,225,100,30);\n"
"    border-style:outset;\n"
"    border-width:4px;\n"
"    border-radius:10px;\n"
"    border-color:rgba(255,255,255,30);\n"
"    color:rgba(0,0,0,100);\n"
"}\n"
"\n"
"QPushButton:hover:pressed{\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-color:rgb(170, 170, 255);\n"
"    border-style:outside;\n"
"    color:rgb(0, 170, 127);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed{\n"
"    background-color:rgb(0, 255, 127);\n"
"    border-color:rgb(170, 255, 255);\n"
"    color:rgb(85, 170, 255);\n"
"}")
        self.number_4.setObjectName("number_4")
        self.gridLayout.addWidget(self.number_4, 1, 0, 1, 1)
        self.number_5 = MyPushButton(passwd)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.number_5.setFont(font)
        self.number_5.setStyleSheet("QPushButton{\n"
"    background-color:rgba(100,225,100,30);\n"
"    border-style:outset;\n"
"    border-width:4px;\n"
"    border-radius:10px;\n"
"    border-color:rgba(255,255,255,30);\n"
"    color:rgba(0,0,0,100);\n"
"}\n"
"\n"
"QPushButton:hover:pressed{\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-color:rgb(170, 170, 255);\n"
"    border-style:outside;\n"
"    color:rgb(0, 170, 127);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed{\n"
"    background-color:rgb(0, 255, 127);\n"
"    border-color:rgb(170, 255, 255);\n"
"    color:rgb(85, 170, 255);\n"
"}")
        self.number_5.setObjectName("number_5")
        self.gridLayout.addWidget(self.number_5, 1, 1, 1, 1)
        self.number_6 = MyPushButton(passwd)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.number_6.setFont(font)
        self.number_6.setStyleSheet("QPushButton{\n"
"    background-color:rgba(100,225,100,30);\n"
"    border-style:outset;\n"
"    border-width:4px;\n"
"    border-radius:10px;\n"
"    border-color:rgba(255,255,255,30);\n"
"    color:rgba(0,0,0,100);\n"
"}\n"
"\n"
"QPushButton:hover:pressed{\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-color:rgb(170, 170, 255);\n"
"    border-style:outside;\n"
"    color:rgb(0, 170, 127);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed{\n"
"    background-color:rgb(0, 255, 127);\n"
"    border-color:rgb(170, 255, 255);\n"
"    color:rgb(85, 170, 255);\n"
"}")
        self.number_6.setObjectName("number_6")
        self.gridLayout.addWidget(self.number_6, 1, 2, 1, 1)
        self.number_7 = MyPushButton(passwd)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.number_7.setFont(font)
        self.number_7.setStyleSheet("QPushButton{\n"
"    background-color:rgba(100,225,100,30);\n"
"    border-style:outset;\n"
"    border-width:4px;\n"
"    border-radius:10px;\n"
"    border-color:rgba(255,255,255,30);\n"
"    color:rgba(0,0,0,100);\n"
"}\n"
"\n"
"QPushButton:hover:pressed{\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-color:rgb(170, 170, 255);\n"
"    border-style:outside;\n"
"    color:rgb(0, 170, 127);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed{\n"
"    background-color:rgb(0, 255, 127);\n"
"    border-color:rgb(170, 255, 255);\n"
"    color:rgb(85, 170, 255);\n"
"}")
        self.number_7.setObjectName("number_7")
        self.gridLayout.addWidget(self.number_7, 2, 0, 1, 1)
        self.number_8 = MyPushButton(passwd)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.number_8.setFont(font)
        self.number_8.setStyleSheet("QPushButton{\n"
"    background-color:rgba(100,225,100,30);\n"
"    border-style:outset;\n"
"    border-width:4px;\n"
"    border-radius:10px;\n"
"    border-color:rgba(255,255,255,30);\n"
"    color:rgba(0,0,0,100);\n"
"}\n"
"\n"
"QPushButton:hover:pressed{\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-color:rgb(170, 170, 255);\n"
"    border-style:outside;\n"
"    color:rgb(0, 170, 127);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed{\n"
"    background-color:rgb(0, 255, 127);\n"
"    border-color:rgb(170, 255, 255);\n"
"    color:rgb(85, 170, 255);\n"
"}")
        self.number_8.setObjectName("number_8")
        self.gridLayout.addWidget(self.number_8, 2, 1, 1, 1)
        self.number_9 = MyPushButton(passwd)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.number_9.setFont(font)
        self.number_9.setStyleSheet("QPushButton{\n"
"    background-color:rgba(100,225,100,30);\n"
"    border-style:outset;\n"
"    border-width:4px;\n"
"    border-radius:10px;\n"
"    border-color:rgba(255,255,255,30);\n"
"    color:rgba(0,0,0,100);\n"
"}\n"
"\n"
"QPushButton:hover:pressed{\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-color:rgb(170, 170, 255);\n"
"    border-style:outside;\n"
"    color:rgb(0, 170, 127);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed{\n"
"    background-color:rgb(0, 255, 127);\n"
"    border-color:rgb(170, 255, 255);\n"
"    color:rgb(85, 170, 255);\n"
"}")
        self.number_9.setObjectName("number_9")
        self.gridLayout.addWidget(self.number_9, 2, 2, 1, 1)
        self.number_symbol = MyPushButton(passwd)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.number_symbol.setFont(font)
        self.number_symbol.setStyleSheet("QPushButton{\n"
"    background-color:rgba(100,225,100,30);\n"
"    border-style:outset;\n"
"    border-width:4px;\n"
"    border-radius:10px;\n"
"    border-color:rgba(255,255,255,30);\n"
"    color:rgba(0,0,0,100);\n"
"}\n"
"\n"
"QPushButton:hover:pressed{\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-color:rgb(170, 170, 255);\n"
"    border-style:outside;\n"
"    color:rgb(0, 170, 127);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed{\n"
"    background-color:rgb(0, 255, 127);\n"
"    border-color:rgb(170, 255, 255);\n"
"    color:rgb(85, 170, 255);\n"
"}")
        self.number_symbol.setObjectName("number_symbol")
        self.gridLayout.addWidget(self.number_symbol, 3, 0, 1, 1)
        self.number_0 = MyPushButton(passwd)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.number_0.setFont(font)
        self.number_0.setStyleSheet("QPushButton{\n"
"    background-color:rgba(100,225,100,30);\n"
"    border-style:outset;\n"
"    border-width:4px;\n"
"    border-radius:10px;\n"
"    border-color:rgba(255,255,255,30);\n"
"    color:rgba(0,0,0,100);\n"
"}\n"
"\n"
"QPushButton:hover:pressed{\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-color:rgb(170, 170, 255);\n"
"    border-style:outside;\n"
"    color:rgb(0, 170, 127);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed{\n"
"    background-color:rgb(0, 255, 127);\n"
"    border-color:rgb(170, 255, 255);\n"
"    color:rgb(85, 170, 255);\n"
"}")
        self.number_0.setObjectName("number_0")
        self.gridLayout.addWidget(self.number_0, 3, 1, 1, 1)
        self.backspace = QtWidgets.QPushButton(passwd)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.backspace.setFont(font)
        self.backspace.setStyleSheet("QPushButton{\n"
"    background-color:rgba(100,225,100,30);\n"
"    border-style:outset;\n"
"    border-width:4px;\n"
"    border-radius:10px;\n"
"    border-color:rgba(255,255,255,30);\n"
"    color:rgba(0,0,0,100);\n"
"}\n"
"\n"
"QPushButton:hover:pressed{\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-color:rgb(170, 170, 255);\n"
"    border-style:outside;\n"
"    color:rgb(0, 170, 127);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed{\n"
"    background-color:rgb(0, 255, 127);\n"
"    border-color:rgb(170, 255, 255);\n"
"    color:rgb(85, 170, 255);\n"
"}")
        self.backspace.setObjectName("backspace")
        self.gridLayout.addWidget(self.backspace, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 99, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 2, 1, 1, 1)

        self.retranslateUi(passwd)
        QtCore.QMetaObject.connectSlotsByName(passwd)

    def retranslateUi(self, passwd):
        _translate = QtCore.QCoreApplication.translate
        passwd.setWindowTitle(_translate("passwd", "Form"))
        self.number_1.setText(_translate("passwd", "1"))
        self.number_2.setText(_translate("passwd", "2"))
        self.number_3.setText(_translate("passwd", "3"))
        self.number_4.setText(_translate("passwd", "4"))
        self.number_5.setText(_translate("passwd", "5"))
        self.number_6.setText(_translate("passwd", "6"))
        self.number_7.setText(_translate("passwd", "7"))
        self.number_8.setText(_translate("passwd", "8"))
        self.number_9.setText(_translate("passwd", "9"))
        self.number_symbol.setText(_translate("passwd", "*"))
        self.number_0.setText(_translate("passwd", "0"))
        self.backspace.setText(_translate("passwd", "<--"))
