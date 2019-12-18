# -*- coding: utf-8 -*-
from ui.sign_ui import Ui_Sign_in
from register import Register
from password import Password
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from aliyun_api import ALiApi
from data_handle import encryption
import sys
import os

class Sign(QWidget, Ui_Sign_in):
    def __init__(self, parent=None, mainwindow=None):
        super(Sign, self).__init__(parent)
        self.setupUi(self)
        self.main = mainwindow
        self.register = Register(self)
        self.passwd = Password(self)
        self.set_connect()

    def set_connect(self):
        self.ui_register_account.clicked.connect(self.register_account)
        self.ui_forget_password.clicked.connect(self.forget_passwd)
        self.ui_sign_in.clicked.connect(self.sign_in)

    def register_account(self):
        self.register.exec()

    def forget_passwd(self):
        self.passwd.exec()

    def sign_in(self):
        info = ALiApi.get_infor_data()
        if self.ui_account.text() != info[0]:
            QMessageBox.critical(self, "登录", "该账号不存在！")
        elif encryption(self.ui_password.text()) != info[1]:
            QMessageBox.critical(self, "登录", "用户名与密码不匹配！")
        else:
            self.hide()
            self.main.show()

    def hideEvent(self, a0):
        if self.ui_save_password.isChecked():
            with open("./config/user.config", "w") as f:
                f.write(self.ui_account.text() + '\n')
                f.write(self.ui_password.text() + '\n')
        else:
            if os.path.exists("./config/user.config"):
                os.remove("./config/user.config")

    def showEvent(self, a0):
        if os.path.exists("./config/user.config"):
            with open("./config/user.config", "r") as f:
                self.ui_account.setText(f.readline()[:-1])
                self.ui_password.setText(f.readline()[:-1])
                self.ui_save_password.setChecked(True)
        else:
            self.ui_save_password.setChecked(False)
