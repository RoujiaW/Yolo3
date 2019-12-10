#credit to https://github.com/qqwweee/keras-yolo3

import cv2
import numpy as np
import os
from .bbox import BoundBox, bbox_iou
from scipy.special import expit

def _sigmoid(x):
    return expit(x)

def makedirs(path):
    try:
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise

def normalize(image):
    return image/255.
       
def _softmax(x, axis=-1):
    x = x - np.amax(x, axis, keepdims=True)
    e_x = np.exp(x)
    
    return e_x / e_x.sum(axis, keepdims=True)
