# -*- coding: utf-8 -*-
import cv2
import os
import numpy as np

IMAGE_SIZE = 64

def resize_image(image, height=IMAGE_SIZE, width=IMAGE_SIZE):
    top, bottom, left, right = (0, 0, 0, 0)
    h, w, _ = image.shape
    longest_edge = max(h, w)
    if h < longest_edge:
        dh = longest_edge - h
        top = dh // 2
        bottom = dh - top
    elif w < longest_edge:
        dw = longest_edge - w
        left = dw // 2
        right = dw - left
    else:
        pass
    BLACK = [0, 0, 0]
    constant = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=BLACK)
    image = cv2.cvtColor(cv2.resize(constant, (height, width)), cv2.COLOR_RGB2GRAY)
    return image.reshape(height, width, 1)

def save_face(camera_idx, catch_pic_num=1000, path_name="./user_face_data"):
    images = []
    labels = []
    cap = cv2.VideoCapture(camera_idx)
    classifier = cv2.CascadeClassifier("./haarcascade_frontalface_alt2.xml")
    num = 0
    if os.path.exists(path_name):
        if len(os.listdir(path_name)) != 0:
            os.system("rm " + os.path.join(path_name, "*"))
    else:
        os.mkdir(path_name)
    while cap.isOpened():
        ok, frame = cap.read()
        if not ok:
            break
        face_rects = classifier.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        if len(face_rects) > 0:
            for faceRect in face_rects:
                x, y, w, h = faceRect
                image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                images.append(resize_image(image))
                labels.append(0)
                num += 1
                if num >= catch_pic_num:
                    cap.release()
                    break
    np.save(os.path.join(path_name, "user_face_images.npy"), np.array(images))
    np.save(os.path.join(path_name, "user_face_labels.npy"), np.array(labels))

if __name__ == '__main__':
    # save_face(0)
    # images = np.load("./user_face_data/user_face_images.npy")
    # labels = np.load("./user_face_data/user_face_labels.npy")
    # print(images.shape)
    # print(labels.shape)
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        _, image = cap.read()
        classifier = cv2.CascadeClassifier("/usr/local/share/opencv4/haarcascades/haarcascade_frontalface_alt2.xml")
        face_rects = classifier.detectMultiScale(image, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        if len(face_rects) > 0:
            # for faceRect in face_rects:
            cv2.imwrite("./zoujin.jpg", image)
                # print("end")
            # exit(1)
        cv2.imshow("test", image)
        cv2.waitKey(10)
