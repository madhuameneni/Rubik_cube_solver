import cv2
import numpy as np


class Cube_2d:
    def __init__(self):
        self.img = np.zeros(shape=(512,512,3), dtype=np.int16)

    def cube_rep(self, colors):

        cv2.rectangle(self.img, pt1=(400, 20), pt2=(500, 120), color=(0, 255, 0), thickness=5)
        return True
