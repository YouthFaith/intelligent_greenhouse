# -*- coding: utf-8 -*-
from module.alert import Alert
import cv2
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication
from PyQt5.QtCore import QThread
from PyQt5.QtNetwork import QUdpSocket
import keras
from keras import backend as K
from threading import Thread
import time
import zlib
import numpy as np

def get_result(x):
    return x[0] + x[1] > 0

class MyThread(QThread):
    def run(self):
        Monitor.send_video = QUdpSocket()
        while 1:
            _, frame = Monitor.cap.read()
            Monitor.frame = cv2.resize(frame, (100, 100))
            time.sleep(2)
            if Monitor.flag:
                enfra = cv2.imencode('.jpg', Monitor.frame)[1]
                data = zlib.compress(enfra, zlib.Z_BEST_COMPRESSION)
                data_encode = np.array(data)
                str_encode = data_encode.tostring()
                Monitor.send_video.writeDatagram(str_encode, Monitor.ip, Monitor.port)
                Monitor.send_video.flush()
            else:
                pass

class Monitor:
    ip = None
    port = None
    cap = cv2.VideoCapture(0)
    classifier = cv2.CascadeClassifier("classifier/haarcascade_frontalface_alt2.xml")
    thread = None
    init_thread = MyThread()
    monitor_count = 0
    alert_count = 0
    flag = False
    frame = None
    send_video = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
            print("test")
            Monitor.init_thread.start()
            Monitor.thread = Thread(target=Monitor.monitor)
            Monitor.thread.start()
            if not cls.cap.isOpened():
                QMessageBox.critical(QWidget(), "错误", "无法获取摄像头！")
                exit(1)
        return cls.instance

    def __del__(self):
        Monitor.cap.release()

    @staticmethod
    def monitor():
        def categorical_squared_hinge(y_true, y_pred):
            y_true = 2. * y_true - 1
            vvvv = K.maximum(1. - y_true * y_pred, 0.)
            vv = K.sum(vvvv, 1, keepdims=False)
            v = K.mean(vv, axis=-1)
            return v

        model = keras.models.load_model("model/flowers.model", custom_objects={'categorical_squared_hinge': categorical_squared_hinge})
        while 1:
            Monitor.monitor_count += 1
            if Monitor.frame is None:
                time.sleep(1)
                continue
            if Monitor.monitor_count > 10:
                Monitor.monitor_count = 0
                image = np.array(Monitor.frame.reshape(1, 100, 100, 3)).astype(float)
                if not get_result(model.predict(image)[0]):
                    Monitor.alert_count += 1
                    if Monitor.alert_count == 3:
                        Monitor.alert_count = 0
                        Alert.turn_on_alert()
                else:
                    Monitor.alert_count = 0
                    Alert.turn_off_alert()
            time.sleep(1)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    Monitor()
    # Monitor.flag = True
    sys.exit(app.exec())
