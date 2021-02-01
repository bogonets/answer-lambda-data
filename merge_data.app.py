import cv2
import json
import numpy as np
from base64 import encodebytes, decodebytes
import base64
import sys



##------------------------------##
# input : data, data2 (string or np.array(np.uint8))
# output : se_list (string)
##------------------------------##

def array_to_string(data):

    if (str(type(data)) == "<class 'numpy.ndarray'>"):
        x = encodebytes(json.dumps(data.tolist()).encode('utf-8')).decode('utf-8')
    return x
 



def on_run(array):

    se_list = array_to_string(array)

    return {"data" : se_list}

