# -*- coding: utf-8 -*-
from ui.mainwindow_ui import Ui_mainwindow
from sign import Sign
import psutil
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtNetwork import QUdpSocket, QHostAddress
from aliyun_api import ALiApi
from monitor import Monitor
from queue import Queue
import sys

NETWORK = "wlp3s0"

class MainWindow(QWidget, Ui_mainwindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.ip = self.get_ip()
        self.socket_1 = Monitor(self.ip, self.ui_scroll_area)
        self.socket_2 = Monitor(self.ip, self.ui_scroll_area)
        self.socket_3 = Monitor(self.ip, self.ui_scroll_area)
        self.socket_4 = Monitor(self.ip, self.ui_scroll_area)
        self.ports = Queue()
        self.find_device = QUdpSocket()
        self.set_find_device_bind()
        self.add_monitor()
        self.add_ports()
        self.set_connect()
        self.current_device_num = 0
        self.sign_in = Sign(mainwindow=self)
        self.sign_in.show()

    def set_find_device_bind(self):
        self.find_device.bind(QHostAddress(self.ip), 8888, QUdpSocket.ReuseAddressHint)

    def add_ports(self):
        for i in range(8889, 8894):
            self.ports.put(i)

    def add_monitor(self):
        self.ui_layout.addLayout(self.socket_1.verticalLayout, 0, 1, 1, 1)
        self.ui_layout.addLayout(self.socket_2.verticalLayout, 0, 2, 1, 1)
        self.ui_layout.addLayout(self.socket_3.verticalLayout, 1, 1, 1, 1)
        self.ui_layout.addLayout(self.socket_4.verticalLayout, 1, 2, 1, 1)

    def set_connect(self):
        self.ui_refresh.clicked.connect(self.refresh)
        self.find_device.readyRead.connect(self.add_device)

    def add_device(self):
        size = self.find_device.pendingDatagramSize()
        data, ip, _ = self.find_device.readDatagram(size)
        data = data.decode('utf-8')
        self.handle_add_device(data, ip)

    def handle_add_device(self, data, ip):
        data = data.split('\n')
        port_ = self.ports.get()
        [self.socket_1, self.socket_2, self.socket_3, self.socket_4][self.current_device_num].show_item(data[0], port_)
        self.current_device_num += 1
        self.find_device.writeDatagram(("set " + str(port_)).encode("utf-8"), ip, 8888)
        self.find_device.flush()
        if len(data) != 3:
            self.handle_add_device("\n".join(data[2:]), ip)

    def refresh(self):
        self.find_device.writeDatagram(b'hello', QHostAddress.Broadcast, 8887)
        self.find_device.flush()

    def show_register_user(self):
        pass

    def get_ip(self):
        netcard_info = []
        info = psutil.net_if_addrs()
        for k, v in info.items():
            for item in v:
                if item[0] == 2 and not item[1] == '127.0.0.1':
                    netcard_info.append((k, item[1]))
        return netcard_info[0][1]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ALiApi()
    main = MainWindow()
    sys.exit(app.exec_())
