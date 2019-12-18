# -*- coding: utf-8 -*-
import hashlib

def encryption(string):
    data = hashlib.sha224()
    data.update(string.encode('utf-8'))
    return data.hexdigest()