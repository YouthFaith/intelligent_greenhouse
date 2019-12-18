from ui.face_verify_ui import Ui_show_face
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
from module.monitor import Monitor
from module.door import Door
import face_recognition
from prompt import Prompt
import numpy as np
import cv2

class FaceVerify(QWidget, Ui_show_face):
    def __init__(self, parent=None, mainwindow=None):
        super(FaceVerify, self).__init__(parent)
        self.setupUi(self)
        self.main = mainwindow
        self.thread = None
        self.mode = 0
        self.save_num = 0
        self.verify_num = 0
        self.verify_count = 0
        self.error = 0
        self.face_verify_timer = QTimer()
        self.face_save_timer = QTimer()
        self.face_encoding = None
        self.set_connect()

    def set_connect(self):
        self.face_verify_timer.timeout.connect(self.face_verify)
        self.face_save_timer.timeout.connect(self.face_save)

    def showEvent(self, a0):
        self.showFullScreen()
        if self.mode == 0:
            self.face_save_timer.start(1)
        else:
            if self.face_encoding is None:
                image = face_recognition.load_image_file("user_face/user.jpg")
                self.face_encoding = face_recognition.face_encodings(image)[0]
            self.face_verify_timer.start(1)

    def set_mode(self, mode):
        self.mode = mode

    def face_save(self):
        _, frame = Monitor.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        self.video_label.setPixmap(QPixmap.fromImage(image).scaled(self.video_label.width(), self.video_label.height()))
        face_rect = Monitor.classifier.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        if len(face_rect) == 1:
            self.save_num = self.save_num + 1
            if self.save_num == 100:
                self.ui_prompt.setText("请眨下眼睛！")
            if self.save_num == 200:
                self.ui_prompt.setText("请张开嘴巴！")
            if self.save_num == 300:
                self.ui_prompt.setText("请摇晃脑袋！")
            if self.save_num == 400:
                self.save_num = 0
                cv2.imwrite("user_face/user.jpg", frame)
                self.face_save_timer.stop()
                self.hide()
                self.main.showFullScreen()
                self.ui_prompt.clear()
                self.face_save_timer.stop()

    def face_verify(self):
        known_face_encodings = [self.face_encoding]
        known_face_names = ["user"]
        process_this_frame = True
        ret, frame = Monitor.cap.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.3)
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    if name == "user":
                        self.ui_prompt.setText("请保持不动！")
                        self.verify_num = self.verify_num + 1
                else:
                    self.ui_prompt.clear()
                    self.verify_num = 0
                    self.verify_count += 1
                if self.verify_count == 50:
                    Prompt("识别失败！", self).show()
                    self.verify_count = 0
                    self.error += 1
                    if self.error == 3:
                        self.error = 0
                        self.hide()
                        self.main.showFullScreen()
                        self.face_verify_timer.stop()
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        self.video_label.setPixmap(QPixmap.fromImage(image).scaled(self.video_label.width(), self.video_label.height()))
        if self.verify_num == 10:
            self.verify_num = 0
            Door.turn_on_door()
            self.face_verify_timer.stop()
            self.hide()
            self.main.showFullScreen()
            self.ui_prompt.clear()
