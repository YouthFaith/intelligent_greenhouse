# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Sign_in(object):
    def setupUi(self, Sign_in):
        Sign_in.setObjectName("Sign_in")
        Sign_in.resize(518, 232)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/png/ui_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Sign_in.setWindowIcon(icon)
        Sign_in.setStyleSheet("color: rgb(86, 118, 162);")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Sign_in)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(Sign_in)
        self.label_3.setMaximumSize(QtCore.QSize(200, 200))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/png/ui_login.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Sign_in)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ui_account = QtWidgets.QLineEdit(Sign_in)
        self.ui_account.setMinimumSize(QtCore.QSize(150, 12))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.ui_account.setFont(font)
        self.ui_account.setStyleSheet("    border-style: outset;\n"
"    border-radius: 8px;\n"
"    color: rgb(86, 118, 162);\n"
"    border:2px solid rgb(186, 189, 182);")
        self.ui_account.setMaxLength(15)
        self.ui_account.setAlignment(QtCore.Qt.AlignCenter)
        self.ui_account.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.ui_account.setObjectName("ui_account")
        self.horizontalLayout.addWidget(self.ui_account)
        self.ui_register_account = QtWidgets.QPushButton(Sign_in)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setUnderline(True)
        self.ui_register_account.setFont(font)
        self.ui_register_account.setStyleSheet("QPushButton{\n"
"    color: rgb(138, 226, 52);\n"
"    }\n"
"QPushButton:hover {\n"
"    color: rgb(115, 210, 22);\n"
"    }\n"
"QPushButton:pressed {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: rgb(86, 118, 162);\n"
"    }\n"
"")
        self.ui_register_account.setFlat(True)
        self.ui_register_account.setObjectName("ui_register_account")
        self.horizontalLayout.addWidget(self.ui_register_account)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Sign_in)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.ui_password = QtWidgets.QLineEdit(Sign_in)
        self.ui_password.setMinimumSize(QtCore.QSize(150, 12))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.ui_password.setFont(font)
        self.ui_password.setStyleSheet("    border-style: outset;\n"
"    border-radius: 8px;\n"
"    color: rgb(86, 118, 162);\n"
"    border:2px solid rgb(186, 189, 182);")
        self.ui_password.setMaxLength(15)
        self.ui_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui_password.setAlignment(QtCore.Qt.AlignCenter)
        self.ui_password.setObjectName("ui_password")
        self.horizontalLayout_2.addWidget(self.ui_password)
        self.ui_forget_password = QtWidgets.QPushButton(Sign_in)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setUnderline(True)
        self.ui_forget_password.setFont(font)
        self.ui_forget_password.setStyleSheet("QPushButton{\n"
"    color: rgb(138, 226, 52);\n"
"    }\n"
"QPushButton:hover {\n"
"    color: rgb(115, 210, 22);\n"
"    }\n"
"QPushButton:pressed {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: rgb(86, 118, 162);\n"
"    }")
        self.ui_forget_password.setFlat(True)
        self.ui_forget_password.setObjectName("ui_forget_password")
        self.horizontalLayout_2.addWidget(self.ui_forget_password)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.ui_save_password = QtWidgets.QCheckBox(Sign_in)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setUnderline(True)
        self.ui_save_password.setFont(font)
        self.ui_save_password.setStyleSheet("text-decoration: underline;")
        self.ui_save_password.setObjectName("ui_save_password")
        self.horizontalLayout_3.addWidget(self.ui_save_password)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.ui_sign_in = QtWidgets.QPushButton(Sign_in)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        self.ui_sign_in.setFont(font)
        self.ui_sign_in.setStyleSheet("QPushButton{\n"
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
        self.ui_sign_in.setObjectName("ui_sign_in")
        self.verticalLayout.addWidget(self.ui_sign_in)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem8 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem8)

        self.retranslateUi(Sign_in)
        QtCore.QMetaObject.connectSlotsByName(Sign_in)

    def retranslateUi(self, Sign_in):
        _translate = QtCore.QCoreApplication.translate
        Sign_in.setWindowTitle(_translate("Sign_in", "智能大棚---登录"))
        self.label.setText(_translate("Sign_in", "账号"))
        self.ui_register_account.setText(_translate("Sign_in", "注册账号"))
        self.label_2.setText(_translate("Sign_in", "密码"))
        self.ui_forget_password.setText(_translate("Sign_in", "忘记密码"))
        self.ui_save_password.setText(_translate("Sign_in", "记住账号"))
        self.ui_sign_in.setText(_translate("Sign_in", "登录"))

from resource import resource
