# -*- coding: utf-8 -*-
import os
import json
import time
from PyQt5.QtWidgets import QMessageBox, QWidget
from aliyunsdkcore.client import AcsClient
from aliyunsdkiot.request.v20180120.QueryDeviceDesiredPropertyRequest import QueryDeviceDesiredPropertyRequest
from aliyunsdkiot.request.v20180120.RegisterDeviceRequest import RegisterDeviceRequest
from aliyunsdkiot.request.v20180120.QueryProductRequest import QueryProductRequest
from aliyunsdkiot.request.v20180120.UpdateProductRequest import UpdateProductRequest
from aliyunsdkiot.request.v20180120.QueryDevicePropertyStatusRequest import QueryDevicePropertyStatusRequest
from aliyunsdkiot.request.v20180120.QueryDevicePropertyDataRequest import QueryDevicePropertyDataRequest

class ALiApi:
    accessKeyId = ""
    accessSecret = ""
    productKey = ""
    client = AcsClient(accessKeyId, accessSecret, 'cn-shanghai')

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
            if os.path.exists("config/productkey.config"):
                with open("config/productkey.config", "r") as f:
                    ALiApi.productKey = f.readline()
                    ALiApi().get_infor_data()
            else:
                QMessageBox.critical(QWidget(), "错误", "请设置有效产品验证码！")
                exit(1)
        return cls.instance

    @staticmethod
    def get_current_th(devicename):
        request = QueryDevicePropertyStatusRequest()
        request.set_accept_format('json')
        request.set_ProductKey(ALiApi.productKey)
        request.set_DeviceName(devicename)
        response = ALiApi.client.do_action_with_exception(request)
        data = json.loads(str(response, encoding='utf-8'))
        return data["Data"]["List"]["PropertyStatusInfo"][0]["Value"], data["Data"]["List"]["PropertyStatusInfo"][1]["Value"]

    @staticmethod
    def get_history_data():
        pass

    @staticmethod
    def get_infor_version(devicename):
        request = QueryDeviceDesiredPropertyRequest()
        request.set_accept_format('json')
        request.set_ProductKey(ALiApi.productKey)
        request.set_DeviceName(devicename)
        request.set_Identifiers(["infor"])
        response = ALiApi.client.do_action_with_exception(request)
        data = json.loads(str(response, encoding='utf-8'))
        return int(data["Data"]["List"]["DesiredPropertyInfo"][0]["Version"])

    @staticmethod
    def get_infor_data():
        request = QueryProductRequest()
        request.set_accept_format('json')
        request.set_ProductKey(ALiApi.productKey)
        response = ALiApi.client.do_action_with_exception(request)
        data = json.loads(str(response, encoding='utf-8'))
        if not data["Success"]:
            QMessageBox.critical(QWidget(), "错误", "产品验证码有误！")
            exit(1)
            return False
        else:
            data_list = str(data["Data"]["Description"]).split("\n")
            return data_list[0], data_list[1], data_list[2]

    @staticmethod
    def get_propertyinfo(devicename, property_name, start_time, end_time):
        request = QueryDevicePropertyDataRequest()
        request.set_accept_format('json')
        request.set_StartTime(ALiApi.to_datatime(start_time))
        request.set_EndTime(ALiApi.to_datatime(end_time))
        request.set_Asc("0")
        request.set_PageSize(50)
        request.set_Identifier(property_name)
        request.set_ProductKey(ALiApi.productKey)
        request.set_DeviceName(devicename)
        response = ALiApi.client.do_action_with_exception(request)
        data = json.loads(str(response, encoding='utf-8'))
        return data

    @staticmethod
    def set_infor_data(username, passwd, email):
        request = UpdateProductRequest()
        request.set_accept_format('json')
        request.set_ProductName("温湿度监测")
        request.set_ProductKey(ALiApi.productKey)
        data = username + "\n" + passwd + "\n" + email + "\n"
        request.set_Description(data)
        response = ALiApi.client.do_action_with_exception(request)
        data = json.loads(str(response, encoding='utf-8'))
        if not data["Success"]:
            return False
        else:
            return True

    @staticmethod
    def register_device(device_name):
        request = RegisterDeviceRequest()
        request.set_accept_format('json')
        request.set_ProductKey(ALiApi.productKey)
        request.set_DeviceName(device_name)
        response = ALiApi.client.do_action_with_exception(request)
        data = json.loads(str(response, encoding='utf-8'))
        if not data["Success"]:
            return False, data["ErrorMessage"]
        else:
            return True, "注册成功"

    @staticmethod
    def to_datatime(string):
        time_array = time.strptime(string, "%Y/%m/%d %H:%M:%S")
        time_stamp = int(time.mktime(time_array))
        return int(str(time_stamp) + "000")
