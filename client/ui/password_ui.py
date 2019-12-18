# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'password.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_password(object):
    def setupUi(self, password):
        password.setObjectName("password")
        password.resize(322, 231)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        password.setFont(font)
        password.setStyleSheet("color: rgb(86, 118, 162);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(password)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(password)
        self.label.setMinimumSize(QtCore.QSize(80, 25))
        self.label.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ui_email = QtWidgets.QLineEdit(password)
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
        self.horizontalLayout.addWidget(self.ui_email)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ui_verification_label = QtWidgets.QLabel(password)
        self.ui_verification_label.setMinimumSize(QtCore.QSize(80, 25))
        self.ui_verification_label.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.ui_verification_label.setFont(font)
        self.ui_verification_label.setObjectName("ui_verification_label")
        self.horizontalLayout_2.addWidget(self.ui_verification_label)
        self.ui_verification = QtWidgets.QLineEdit(password)
        self.ui_verification.setMinimumSize(QtCore.QSize(200, 12))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.ui_verification.setFont(font)
        self.ui_verification.setStyleSheet("    border-style: outset;\n"
"    border-radius: 8px;\n"
"    color: rgb(86, 118, 162);\n"
"    border:2px solid rgb(186, 189, 182);")
        self.ui_verification.setMaxLength(4)
        self.ui_verification.setAlignment(QtCore.Qt.AlignCenter)
        self.ui_verification.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.ui_verification.setObjectName("ui_verification")
        self.horizontalLayout_2.addWidget(self.ui_verification)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ui_passwd_label = QtWidgets.QLabel(password)
        self.ui_passwd_label.setMinimumSize(QtCore.QSize(80, 25))
        self.ui_passwd_label.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.ui_passwd_label.setFont(font)
        self.ui_passwd_label.setObjectName("ui_passwd_label")
        self.horizontalLayout_3.addWidget(self.ui_passwd_label)
        self.ui_passwd = QtWidgets.QLineEdit(password)
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
        self.horizontalLayout_3.addWidget(self.ui_passwd)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ui_repasswd_label = QtWidgets.QLabel(password)
        self.ui_repasswd_label.setMinimumSize(QtCore.QSize(80, 25))
        self.ui_repasswd_label.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.ui_repasswd_label.setFont(font)
        self.ui_repasswd_label.setObjectName("ui_repasswd_label")
        self.horizontalLayout_4.addWidget(self.ui_repasswd_label)
        self.ui_repasswd = QtWidgets.QLineEdit(password)
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
        self.horizontalLayout_4.addWidget(self.ui_repasswd)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.ui_code = QtWidgets.QPushButton(password)
        self.ui_code.setMinimumSize(QtCore.QSize(120, 30))
        self.ui_code.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.ui_code.setFont(font)
        self.ui_code.setStyleSheet("QPushButton{\n"
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
        self.ui_code.setObjectName("ui_code")
        self.horizontalLayout_5.addWidget(self.ui_code)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        spacerItem4 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)

        self.retranslateUi(password)
        QtCore.QMetaObject.connectSlotsByName(password)

    def retranslateUi(self, password):
        _translate = QtCore.QCoreApplication.translate
        password.setWindowTitle(_translate("password", "智能大棚---找回密码"))
        self.label.setText(_translate("password", "邮    箱:"))
        self.ui_verification_label.setText(_translate("password", "验 证 码:"))
        self.ui_passwd_label.setText(_translate("password", "密    码:"))
        self.ui_repasswd_label.setText(_translate("password", "确认密码:"))
        self.ui_code.setText(_translate("password", "获取验证码"))

