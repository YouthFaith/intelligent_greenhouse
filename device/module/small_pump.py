from equipment import water_pump
import threading
import time
import inspect
import ctypes

class steer_engine(water_pump.water_pump):

    def __init__(self, pin, temp_hum):
        water_pump.water_pump.__init__(self, pin)
        self.thread = None
        self.pulse = 0
        self.temp_hum = temp_hum
        self.hum = None
        self.manual_open = True
        self.start()

    def open_pump(self):
        self.manual_open = False
        self.sprinkling(30)

    def close_pump(self):
        self.sprinkling(0)
        self.manual_open = True

    def start(self):
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def end(self):
        stop_thread(self.thread)

    def run(self):
        while True:
            self.hum = self.temp_hum.get_humidity()
            if self.manual_open:
                if self.hum > self.temp_hum.hum_max:
                    if self.pulse < 30:
                        self.pulse = self.pulse + 10
                        self.sprinkling(self.pulse)
                if self.temp_hum.hum_min < self.hum < self.temp_hum.hum_max:
                    if self.pulse > 0:
                        self.pulse = self.pulse - 10
                        self.sprinkling(self.pulse)
                time.sleep(0.5)
