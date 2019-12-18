# -*- coding: utf-8 -*-
from ui.register_ui import Ui_login
from PyQt5.QtWidgets import QDialog, QMessageBox
from aliyun_api import ALiApi
import re
from data_handle import encryption

class Register(QDialog, Ui_login):
    def __init__(self, parent=None):
        super(Register, self).__init__(parent)
        self.setupUi(self)
        self.set_connect()

    def set_connect(self):
        self.ui_register.clicked.connect(self.ok)

    def ok(self):
        if self.ui_account.text() == "":
            QMessageBox.critical(self, "警告", "请输入账号！")
            return
        passwd_pattern = re.compile(r"^[1-9]{6}$")
        if passwd_pattern.match(self.ui_passwd.text()) is None:
            QMessageBox.critical(self, "警告", "密码格式不正确！")
            return
        if self.ui_passwd.text() == "" or self.ui_repasswd.text() == "":
            QMessageBox.critical(self, "警告", "请输入两次密码！")
            return
        if self.ui_passwd.text() != self.ui_repasswd.text():
            QMessageBox.critical(self, "警告", "密码不一致！")
            return
        if self.ui_email.text() == "":
            QMessageBox.critical(self, "警告", "请输入邮箱！")
            return
        email_pattern = re.compile(
            r"[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?")
        email = self.ui_email.text()
        if email_pattern.match(email) is None:
            QMessageBox.critical(self, "警告", "邮箱格式不正确！")
            return
        ALiApi.set_infor_data(self.ui_account.text(), encryption(self.ui_passwd.text()), self.ui_email.text())
        QMessageBox.information(self, "注册", "注册成功！")
        self.accept()
