# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(379, 246)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        login.setFont(font)
        login.setStyleSheet("color: rgb(86, 118, 162);")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(login)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(login)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ui_account = QtWidgets.QLineEdit(login)
        self.ui_account.setMinimumSize(QtCore.QSize(200, 12))
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
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(login)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.ui_passwd = QtWidgets.QLineEdit(login)
        self.ui_passwd.setMinimumSize(QtCore.QSize(200, 12))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.ui_passwd.setFont(font)
        self.ui_passwd.setStyleSheet("    border-style: outset;\n"
"    border-radius: 8px;\n"
"    color: rgb(86, 118, 162);\n"
"    border:2px solid rgb(186, 189, 182);")
        self.ui_passwd.setMaxLength(15)
        self.ui_passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui_passwd.setAlignment(QtCore.Qt.AlignCenter)
        self.ui_passwd.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.ui_passwd.setObjectName("ui_passwd")
        self.horizontalLayout_2.addWidget(self.ui_passwd)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(login)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.ui_repasswd = QtWidgets.QLineEdit(login)
        self.ui_repasswd.setMinimumSize(QtCore.QSize(200, 12))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.ui_repasswd.setFont(font)
        self.ui_repasswd.setStyleSheet("    border-style: outset;\n"
"    border-radius: 8px;\n"
"    color: rgb(86, 118, 162);\n"
"    border:2px solid rgb(186, 189, 182);")
        self.ui_repasswd.setMaxLength(15)
        self.ui_repasswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui_repasswd.setAlignment(QtCore.Qt.AlignCenter)
        self.ui_repasswd.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.ui_repasswd.setObjectName("ui_repasswd")
        self.horizontalLayout_3.addWidget(self.ui_repasswd)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(login)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.ui_email = QtWidgets.QLineEdit(login)
        self.ui_email.setMinimumSize(QtCore.QSize(200, 12))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.ui_email.setFont(font)
        self.ui_email.setStyleSheet("    border-style: outset;\n"
"    border-radius: 8px;\n"
"    color: rgb(86, 118, 162);\n"
"    border:2px solid rgb(186, 189, 182);")
        self.ui_email.setMaxLength(100)
        self.ui_email.setAlignment(QtCore.Qt.AlignCenter)
        self.ui_email.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.ui_email.setObjectName("ui_email")
        self.horizontalLayout_4.addWidget(self.ui_email)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.ui_register = QtWidgets.QPushButton(login)
        self.ui_register.setMinimumSize(QtCore.QSize(120, 30))
        self.ui_register.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.ui_register.setFont(font)
        self.ui_register.setStyleSheet("QPushButton{\n"
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
        self.ui_register.setObjectName("ui_register")
        self.horizontalLayout_5.addWidget(self.ui_register)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "智能大棚---注册"))
        self.label.setText(_translate("login", "账    号:"))
        self.label_2.setText(_translate("login", "密    码:"))
        self.label_3.setText(_translate("login", "确认密码:"))
        self.label_4.setText(_translate("login", "邮    箱:"))
        self.ui_register.setText(_translate("login", "确定"))

