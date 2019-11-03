import numpy as np
from math_fns import *

def rotate(points, angle):
    theta = np.radians(angle)
    c, s = np.cos(theta), np.sin(theta)
    R = np.array(((c,-s), (s, c)))
    return np.array([R @ p for p in points])

def translate(points, x_translation, y_translation):
    return np.array([(x+x_translation, y+y_translation) for (x, y) in points])

def scale(points, x_scale, y_scale):
    R = np.array(((x_scale,0), (0, y_scale)))
    return np.array([R @ p for p in points])

def ang_to_vec(angle):
    theta = np.radians(angle)

    return np.array([np.cos(theta), np.sin(theta)])

def sign(x):
    return 1 if x > 0 else -1
