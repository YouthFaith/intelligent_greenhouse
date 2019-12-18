# -*- coding: utf-8 -*-
from ui.devide_ui import Ui_device
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QBuffer, QByteArray, QIODevice
from aliyun_api import ALiApi
from baidu_api import BaiduAPi
import re
import urllib.request
from bs4 import BeautifulSoup
import urllib.parse

class Device(QWidget, Ui_device):
    def __init__(self, monitor, parent=None):
        super(Device, self).__init__(parent)
        self.setupUi(self)
        self.monitor = monitor
        self.timer = 0

    def show_detail(self, name):
        self.name.setText(name)
        if name == "非植物":
            self.information.setText("百度云图像识别Api未识别出该植物！")
            return
        search_item = name
        try:
            url = 'https://baike.baidu.com/item/' + urllib.parse.quote(search_item)
            html = urllib.request.urlopen(url)
            content = html.read().decode('utf-8')
            html.close()
            soup = BeautifulSoup(content, "lxml")
            text = soup.find('div', class_="lemma-summary").children
            res = ""
            for x in text:
                word = re.sub(re.compile(r"<(.+?)>"), '', str(x))
                words = re.sub(re.compile(r"\[(.+?)\]"), '', word)
                res += words
            res = res.replace("（", "(").replace("）", ")").replace("：", ":").replace("\n", "")
            pattern = re.compile(r"[(](.*?)[)]")
            while pattern.search(res):
                res = res.replace(pattern.search(res).group(0), "")
            self.information.setText(res)
        except AttributeError:
            return None

    def get_plant_name(self, image):
        data = QByteArray()
        buffer = QBuffer(data)
        buffer.open(QIODevice.WriteOnly)
        image = image.toImage()
        image.save(buffer, "jpg")
        return BaiduAPi.get_plant_name(buffer.data())

    def showEvent(self, a0):
        self.startTimer(10)
        name = self.get_plant_name(self.monitor.get_current_image())
        self.show_detail(name)

    def hideEvent(self, a0):
        self.killTimer(self.timer)

    def timerEvent(self, a0):
        temperature, humidity = ALiApi.get_current_th(self.monitor.monitor.text())
        self.current_temp.setText("{:3.2}".format(temperature))
        self.current_hum.setText("{:3.2}".format(humidity))
        self.timer = a0.timerId()
