# -*- coding: utf-8 -*-
import os
import json
import uuid
from PyQt5.QtWidgets import QMessageBox, QWidget
from aliyunsdkcore.client import AcsClient
from aliyunsdkiot.request.v20180120.QueryProductRequest import QueryProductRequest
from aliyunsdkiot.request.v20180120.RegisterDeviceRequest import RegisterDeviceRequest

class ALApi:
    lk = None
    accessKeyId = ""
    accessSecret = ""
    productKey = ""
    mac = ""
    secret = ""
    client = AcsClient(accessKeyId, accessSecret, 'cn-shanghai')

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
            if os.path.exists("config/productkey.config"):
                with open("config/productkey.config", "r") as f:
                    ALApi.productKey = f.readline()
                    ALApi.get_infor_data()
                    ALApi.is_device()
                    ALApi.secret = ALApi.get_device_secret()
            else:
                QMessageBox.critical(QWidget(), "错误", "请设置有效产品验证码！")
                exit(1)
        return cls.instance

    @staticmethod
    def get_infor_data():
        request = QueryProductRequest()
        request.set_accept_format('json')
        request.set_ProductKey(ALApi.productKey)
        response = ALApi.client.do_action_with_exception(request)
        data = json.loads(str(response, encoding='utf-8'))
        if not data["Success"]:
            QMessageBox.critical(QWidget(), "错误", "产品验证码有误！")
            exit(1)
            return False
        else:
            ALApi.mac = ALApi.get_mac_address()
            data_list = str(data["Data"]["Description"]).split("\n")
            return data_list[0], data_list[1], data_list[2]

    @staticmethod
    def is_device():
        request = RegisterDeviceRequest()
        request.set_accept_format('json')
        request.set_ProductKey(ALApi.productKey)
        request.set_DeviceName(ALApi.mac)
        ALApi.client.do_action_with_exception(request)

    @staticmethod
    def get_mac_address():
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])

    @staticmethod
    def get_device_secret():
        from aliyunsdkiot.request.v20180120.QueryDeviceDetailRequest import QueryDeviceDetailRequest
        request = QueryDeviceDetailRequest()
        request.set_accept_format('json')
        request.set_ProductKey(ALApi.productKey)
        request.set_DeviceName(ALApi.mac)
        response = ALApi.client.do_action_with_exception(request)
        data = json.loads(str(response, encoding='utf-8'))
        return data["Data"]["DeviceSecret"]
