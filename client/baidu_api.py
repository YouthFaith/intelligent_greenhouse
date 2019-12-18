# -*- coding: utf-8 -*-
from aip import AipImageClassify
class BaiduAPi:
    appId = ""
    apiKey = ""
    secretKey = ""
    client = AipImageClassify(appId, apiKey, secretKey)

    @staticmethod
    def get_plant_name(image):
        return BaiduAPi.client.plantDetect(image)["result"][0]["name"]
