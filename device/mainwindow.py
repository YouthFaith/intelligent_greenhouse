# -*- coding: utf-8 -*-
from ui.mainwindow_ui import Ui_mainwindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from face_verify import FaceVerify
from passwd_verify import PasswordVerify
import os
from PyQt5.QtNetwork import QUdpSocket, QHostAddress
from PyQt5.QtCore import QByteArray
from prompt import Prompt
import psutil
from module.door import Door
from module.aliyun_api import ALApi
from module.monitor import Monitor


class MainWindow(QWidget, Ui_mainwindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.password_ui = PasswordVerify(mainwindow=self)
        self.face_ui = FaceVerify(mainwindow=self)
        self.find_device = QUdpSocket()
        self.video_send = QUdpSocket()
        self.set_bind()
        self.showFullScreen()
        self.set_connect()

    def set_bind(self):
        self.find_device.bind(QHostAddress.Broadcast, 8887, QUdpSocket.ReuseAddressHint)
        self.find_device.readyRead.connect(self.send_device)

    def send_device(self):
        size = self.find_device.pendingDatagramSize()
        data, ip, _ = self.find_device.readDatagram(size)
        if data == b"hello":
            send_data = ALApi.mac + '\n' + self.get_ip() + '\n'
            send_data = send_data.encode('utf-8')
            self.find_device.writeDatagram(send_data, ip, 8888)
            if not Monitor.flag:
                self.video_send.bind(QHostAddress(self.get_ip()), 8888)
                self.video_send.readyRead.connect(self.handle_data)

    def handle_data(self):
        size = self.video_send.pendingDatagramSize()
        data, ip, _ = self.video_send.readDatagram(size)
        data = data.decode('utf-8')
        if not Monitor.flag:
            Monitor.ip = ip
            Monitor.port = int(data[4:])
        Monitor.flag = True

    def set_connect(self):
        self.passwd_verify.clicked.connect(self.passwd_verify_clicked)
        self.face_verify.clicked.connect(self.face_verify_clicked)
        self.init_verify.clicked.connect(self.init_verify_clicked)
        self.turn_off.clicked.connect(self.turn_off_door)

    def turn_off_door(self):
        Door.turn_off_door()

    def passwd_verify_clicked(self):
        self.password_ui.showFullScreen()
        self.hide()

    def face_verify_clicked(self):
        if not os.path.exists("user_face/user.jpg"):
            Prompt("系统未录入人脸数据，请进行初始化系统!", self).show()
            return
        self.face_ui.set_mode(1)
        self.hide()
        self.face_ui.show()

    def init_verify_clicked(self):
        if os.path.exists("user_face/user.jpg"):
            Prompt("已经录入人脸数据，请直接进行验证！", self).show()
            return
        self.face_ui.set_mode(0)
        self.hide()
        self.face_ui.show()

    def get_ip(self):
        netcard_info = []
        info = psutil.net_if_addrs()
        for k, v in info.items():
            for item in v:
                if item[0] == 2 and not item[1] == '127.0.0.1':
                    netcard_info.append((k, item[1]))
        return netcard_info[0][1]

    def keyPressEvent(self, a0):
        if a0.key() == Qt.Key_Q:
            exit(1)
