# -*- coding: utf-8 -*-
from ui.password_ui import Ui_password
from PyQt5.QtWidgets import QDialog, QMessageBox
from aliyun_api import ALiApi
from data_handle import encryption
import random
import smtplib
from email.mime.text import MIMEText
import re

class Password(QDialog, Ui_password):
    def __init__(self, parent=None):
        super(Password, self).__init__(parent)
        self.setupUi(self)
        self.verify_code = ""
        self.ui_code.clicked.connect(self.send_code)

    def showEvent(self, a0):
        self.ui_email.clear()
        self.ui_repasswd.clear()
        self.ui_passwd.clear()
        self.ui_verification.clear()
        self.ui_code.setText("获取验证码")
        self.ui_verification_label.hide()
        self.ui_verification.hide()
        self.ui_passwd.hide()
        self.ui_repasswd.hide()
        self.ui_passwd_label.hide()
        self.ui_repasswd_label.hide()

    def generate_code(self):
        code = ""
        for i in range(4):
            choose = random.randrange(0, 4)
            if choose == 1:
                item = random.randrange(0, 10)
                code = code + str(item)
            elif choose == 2:
                item = chr(random.randrange(65, 91))
                code = code + item
            else:
                item = chr(random.randrange(97, 123))
                code = code + item
        self.verify_code = code

    def send_code(self):
        if self.ui_code.text() == "获取验证码":
            if self.ui_email.text() == "":
                QMessageBox(self, "警告", "请输入邮箱！")
                return
            else:
                pattern = re.compile(r"[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?")
                email = self.ui_email.text()
                if pattern.match(email) is None:
                    QMessageBox.critical(self, "警告", "邮箱格式不正确！")
                    return
                self.generate_code()
                self.ui_verification_label.show()
                self.ui_verification.show()
                self.ui_passwd.show()
                self.ui_repasswd.show()
                self.ui_repasswd_label.show()
                self.ui_passwd_label.show()
                body = '<h1>验证码:{0}</h1><p></p>'.format(self.verify_code)
                msg = MIMEText(body, 'html')
                msg['subject'] = '验证码'
                msg['from'] = 'youthfaith_test@163.com'
                msg['to'] = email
                try:
                    s = smtplib.SMTP_SSL('smtp.163.com', 465)
                    s.login('youthfaith_test@163.com', 'asdf1234')
                    s.sendmail('youthfaith_test@163.com', email, msg.as_string())
                    self.ui_code.setText("修改密码")
                except smtplib.SMTPException:
                    QMessageBox.critical(self, "验证码", "您输入的邮箱不存在！")
                    return
        else:
            if self.ui_verification.text() != self.verify_code:
                QMessageBox.critical(self, "验证码", "验证码不正确！")
                return
            passwd_pattern = re.compile(r"^[1-9]{6}$")
            if passwd_pattern.match(self.ui_passwd.text()) is None:
                QMessageBox.critical(self, "警告", "密码格式不正确！")
                return
            if self.ui_passwd.text() != self.ui_repasswd.text():
                QMessageBox.critical(self, "验证码", "两次密码不一致！")
                return
            if self.ui_passwd.text() == "" or self.ui_repasswd.text() == "":
                QMessageBox.critical(self, "验证码", "请输出两次密码！")
                return
            else:
                ALiApi.set_infor_data(ALiApi.get_infor_data()[0], encryption(self.ui_passwd.text()), self.ui_email.text())
                QMessageBox.information(self, "修改密码", "密码修改成功！")
                self.accept()
