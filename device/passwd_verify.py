# -*- coding: utf-8 -*-
from module.door import Door
from module.aliyun_api import ALApi
from module.data_handle import encryption
from ui.passwd_verify_ui import Ui_passwd
from PyQt5.QtWidgets import QWidget
from prompt import Prompt

class PasswordVerify(QWidget, Ui_passwd):
    def __init__(self, parent=None, mainwindow=None):
        super(PasswordVerify, self).__init__(parent)
        self.setupUi(self)
        self.main = mainwindow
        self.save_password = ""
        self.is_have_pwd = True
        self.pwd_connect()

    def pwd_connect(self):
        self.number_0.num_signal.connect(self.key_clicked)
        self.number_1.num_signal.connect(self.key_clicked)
        self.number_2.num_signal.connect(self.key_clicked)
        self.number_3.num_signal.connect(self.key_clicked)
        self.number_4.num_signal.connect(self.key_clicked)
        self.number_5.num_signal.connect(self.key_clicked)
        self.number_6.num_signal.connect(self.key_clicked)
        self.number_7.num_signal.connect(self.key_clicked)
        self.number_8.num_signal.connect(self.key_clicked)
        self.number_9.num_signal.connect(self.key_clicked)
        self.number_symbol.num_signal.connect(self.key_clicked)
        self.backspace.clicked.connect(self.backspace_clicked)

    def change_password_actively(self):
        self.is_have_pwd = False
        self.password = ""

    def key_clicked(self, number):
        self.save_password = self.save_password + str(number)
        self.show_passwd.setText(self.save_password)
        if len(self.save_password) == 6:
            if encryption(self.save_password) == ALApi.get_infor_data()[1]:
                Door.turn_on_door()
                self.hide()
                self.main.showFullScreen()
            else:
                Prompt("密码错误！", self).show()
            self.save_password = ""
            self.show_passwd.clear()

    def backspace_clicked(self):
        self.show_passwd.clear()
        if self.save_password is None or self.save_password == "":
            self.hide()
            self.main.showFullScreen()
        else:
            self.save_password = self.save_password[:-1]
        self.show_passwd.setText(self.save_password)
