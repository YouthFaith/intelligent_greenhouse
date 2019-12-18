# -*- coding: utf-8 -*-
from keras import Sequential, regularizers
import keras
import numpy as np
from keras import backend as K
import cv2

def categorical_squared_hinge(y_true, y_pred):
    y_true = 2. * y_true - 1
    vvvv = K.maximum(1. - y_true * y_pred, 0.)
    vv = K.sum(vvvv, 1, keepdims=False)
    v = K.mean(vv, axis=-1)
    return v

# image = np.array(list(np.load("flowers_data/images_0.npy")) + list(np.load("flowers_data/images_1.npy")))
# label = np.array(list(np.load("flowers_data/labels_0.npy")) + list(np.load("flowers_data/labels_1.npy")))
# model = Sequential([
#     keras.layers.Conv2D(128, 3, padding='same', input_shape=(100, 100, 3)),
#     keras.layers.MaxPooling2D(),
#     keras.layers.Conv2D(256, 3, padding='same'),
#     keras.layers.MaxPooling2D(),
#     keras.layers.Flatten(),
#     keras.layers.Dense(2, activation='linear', kernel_regularizer=regularizers.l2(0.5))
# ])
# model.compile(optimizer='adam',
#               loss=categorical_squared_hinge,
#               metrics=['accuracy'])
# model.summary()
# model.fit(image[:-2], label[:-2], batch_size=20, epochs=30, shuffle=True, validation_split=0.3)
# model.save("model/flowers.model")

def get_result(x):
    return x[0] + x[1] > 0
from model import Model
if __name__ == "__main__":
    image = cv2.imread("flowers_data/image_0/103.jpg")
    image = np.load("flowers_data/images_1.npy")
    print(image[-1:].shape)
    score = Model.model.predict(image[-1:])
    for i in score:
        print(get_result(i))
