# -*- coding: utf-8 -*-
import keras
import keras.backend as K

def categorical_squared_hinge(y_true, y_pred):
    y_true = 2. * y_true - 1
    vvvv = K.maximum(1. - y_true * y_pred, 0.)
    vv = K.sum(vvvv, 1, keepdims=False)
    v = K.mean(vv, axis=-1)
    return v

class Model:
    model = keras.models.load_model("model/flowers.model",
                                    custom_objects={'categorical_squared_hinge': categorical_squared_hinge})
