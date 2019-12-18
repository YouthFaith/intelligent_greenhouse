# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(600, 471)
        font = QtGui.QFont()
        font.setPointSize(20)
        mainwindow.setFont(font)
        mainwindow.setStyleSheet("color: rgb(86, 118, 162);")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(mainwindow)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(143, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(mainwindow)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.passwd_verify = QtWidgets.QPushButton(mainwindow)
        self.passwd_verify.setMinimumSize(QtCore.QSize(200, 50))
        self.passwd_verify.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(15)
        self.passwd_verify.setFont(font)
        self.passwd_verify.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(149, 187, 209, 255), stop:1 rgba(218, 238, 249, 255));\n"
"    border-style: outset;\n"
"    border-radius: 8px;\n"
"    color:rgb(86, 118, 162);\n"
"    }\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(17, 100, 162, 255), stop:1 rgba(61, 140, 201, 255));\n"
"    border-style: inset;\n"
"    border-radius: 8px;\n"
"    color:white;\n"
"    }")
        self.passwd_verify.setObjectName("passwd_verify")
        self.verticalLayout.addWidget(self.passwd_verify)
        self.face_verify = QtWidgets.QPushButton(mainwindow)
        self.face_verify.setMinimumSize(QtCore.QSize(200, 50))
        self.face_verify.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(15)
        self.face_verify.setFont(font)
        self.face_verify.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(149, 187, 209, 255), stop:1 rgba(218, 238, 249, 255));\n"
"    border-style: outset;\n"
"    border-radius: 8px;\n"
"    color:rgb(86, 118, 162);\n"
"    }\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(17, 100, 162, 255), stop:1 rgba(61, 140, 201, 255));\n"
"    border-style: inset;\n"
"    border-radius: 8px;\n"
"    color:white;\n"
"    }")
        self.face_verify.setObjectName("face_verify")
        self.verticalLayout.addWidget(self.face_verify)
        self.turn_off = QtWidgets.QPushButton(mainwindow)
        self.turn_off.setMinimumSize(QtCore.QSize(200, 50))
        self.turn_off.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(15)
        self.turn_off.setFont(font)
        self.turn_off.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(149, 187, 209, 255), stop:1 rgba(218, 238, 249, 255));\n"
"    border-style: outset;\n"
"    border-radius: 8px;\n"
"    color:rgb(86, 118, 162);\n"
"    }\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(17, 100, 162, 255), stop:1 rgba(61, 140, 201, 255));\n"
"    border-style: inset;\n"
"    border-radius: 8px;\n"
"    color:white;\n"
"    }")
        self.turn_off.setObjectName("turn_off")
        self.verticalLayout.addWidget(self.turn_off)
        self.init_verify = QtWidgets.QPushButton(mainwindow)
        self.init_verify.setMinimumSize(QtCore.QSize(200, 50))
        self.init_verify.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(15)
        self.init_verify.setFont(font)
        self.init_verify.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(149, 187, 209, 255), stop:1 rgba(218, 238, 249, 255));\n"
"    border-style: outset;\n"
"    border-radius: 8px;\n"
"    color:rgb(86, 118, 162);\n"
"    }\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(17, 100, 162, 255), stop:1 rgba(61, 140, 201, 255));\n"
"    border-style: inset;\n"
"    border-radius: 8px;\n"
"    color:white;\n"
"    }")
        self.init_verify.setObjectName("init_verify")
        self.verticalLayout.addWidget(self.init_verify)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(143, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "MainWindow"))
        self.label.setText(_translate("mainwindow", "欢迎使用智能大棚系统"))
        self.passwd_verify.setText(_translate("mainwindow", "密码验证"))
        self.face_verify.setText(_translate("mainwindow", "人脸验证"))
        self.turn_off.setText(_translate("mainwindow", "关门"))
        self.init_verify.setText(_translate("mainwindow", "系统初始化"))

