# -*- coding: utf-8 -*-
import time
import Adafruit_DHT as Ada
from module.aliyun_api import ALApi
from linkkit import linkkit
from threading import Thread
from module.threadmanagement import stop_thread
from module.light import Light
from module.waterpump import WaterPump
from module.airconditioner import AirConditioner


class ThSensor:
    humidity_max = 80
    humidity_min = 60
    temperature_max = 25
    temperature_min = 15

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, i2c):
        self.thread = None
        self.current_humidity = None
        self.current_temperature = None
        self.judge_hum_high = True
        self.judge_hum_low = True
        self.judge_temp_high = True
        self.judge_temp_low = True
        self.i2c = i2c
        self.start()

    def __del__(self):
        if self.thread is not None:
            stop_thread(self.thread)
        del self.thread
        del self.current_temperature
        del self.current_humidity
        del self.judge_hum_high

    def start(self):
        self.thread = Thread(target=self.run)
        self.thread.start()

    def temp_high_to_do(self):
        AirConditioner.turn_on_air()

    def temp_normal(self):
        AirConditioner.turn_off_air()
        Light.turn_off_red_light()

    def temp_low_to_do(self):
        Light.turn_on_red_light()

    def hum_high_to_do(self):
        Light.turn_on_red_light()

    def hum_low_to_do(self):
        WaterPump.start_pump()

    def hum_normal(self):
        Light.turn_off_red_light()
        WaterPump.stop_pump()

    def set_humidity(self, hum):
        self.current_humidity = hum
        if hum > ThSensor.humidity_max:
            if self.judge_hum_high:
                self.judge_hum_high = False
                self.judge_hum_low = True
                self.hum_high_to_do()
        elif hum < ThSensor.humidity_min:
            if self.judge_hum_low:
                self.judge_hum_low = False
                self.judge_hum_high = True
                self.hum_low_to_do()
        else:
            self.judge_hum_high = True
            self.judge_hum_low = True
            self.hum_normal()

    def set_temperature(self, temp):
        self.current_temperature = temp
        if temp > ThSensor.temperature_max:
            if self.judge_temp_high:
                self.judge_temp_high = False
                self.judge_temp_low = True
                self.temp_high_to_do()
        elif temp < ThSensor.temperature_min:
            if self.judge_temp_low:
                self.judge_temp_low = False
                self.judge_temp_high = True
                self.temp_low_to_do()
        else:
            self.judge_temp_high = True
            self.judge_temp_low = True
            self.temp_normal()

    @staticmethod
    def set_humidity_max(value):
        ThSensor.humidity_max = value

    @staticmethod
    def set_humidity_min(value):
        ThSensor.humidity_min = value

    @staticmethod
    def set_temperature_max(value):
        ThSensor.temperature_max = value

    @staticmethod
    def set_temperature_min(value):
        ThSensor.temperature_min = value

    def get_current_humidity(self):
        return self.current_humidity

    def get_current_temperature(self):
        return self.current_temperature

    def run(self):
        ALApi.lk = linkkit.LinkKit(
            host_name="cn-shanghai",
            product_key=ALApi.productKey,
            device_name=ALApi.mac,
            device_secret=ALApi.secret
        )
        ALApi.lk.thing_setup("model/model.json")
        ALApi.lk.connect_async()
        while 1:
            rdata = Ada.DHT11
            hum, temp = Ada.read_retry(rdata, self.i2c)
            if hum is not None and temp is not None:
                self.set_temperature(int(temp))
                self.set_humidity(int(hum))
                prop_data = {
                    "Temperature": temp,
                    "Humidity": hum
                }
                ALApi.lk.thing_post_property(prop_data)
            time.sleep(1)
