import cv2
import numpy as np


class Cube_rep:
    def __init__(self):
        self.axis = {
            0 : ([210, 50], [240, 80], []),
            1: ([250, 50], [280, 80]),
            2: ([290, 50], [320, 80]),
            3: ([210, 90], [240, 120]),
            4: ([250, 90], [280, 120]),
            5: ([290, 90], [320, 120]),
            6: ([210, 130], [240, 160]),
            7: ([250, 130], [280, 160]),
            8: ([290, 130], [320, 160]),

            18: ([210, 170], [240, 200]),
            19: ([250, 170], [280, 200]),
            20: ([290, 170], [320, 200]),
            21: ([210, 210], [240, 240]),
            22: ([250, 210], [280, 240]),
            23: ([290, 210], [320, 240]),
            24: ([210, 250], [240, 280]),
            25: ([250, 250], [280, 280]),
            26: ([290, 250], [320, 280]),

            27: ([210, 290], [240, 320]),
            28: ([250, 290], [280, 320]),
            29: ([290, 290], [320, 320]),
            30: ([210, 330], [240, 360]),
            31: ([250, 330], [280, 360]),
            32: ([290, 330], [320, 360]),
            33: ([210, 370], [240, 400]),
            34: ([250, 370], [280, 400]),
            35: ([290, 370], [320, 400]),

            36: ([90, 170], [120, 200]),
            37: ([130, 170], [160, 200]),
            38: ([170, 170], [200, 200]),
            39: ([90, 210], [120, 240]),
            40: ([130, 210], [160, 240]),
            41: ([170, 210], [200, 240]),
            42: ([90, 250], [120, 280]),
            43: ([130, 250], [160, 280]),
            44: ([170, 250], [200, 280]),

            9: ([330, 170], [360, 200]),
            10: ([370, 170], [400, 200]),
            11: ([410, 170], [440, 200]),
            12: ([330, 210], [360, 240]),
            13: ([370, 210], [400, 240]),
            14: ([410, 210], [440, 240]),
            15: ([330, 250], [360, 280]),
            16: ([370, 250], [400, 280]),
            17: ([410, 250], [440, 280]),

            45: ([450, 170], [480, 200]),
            46: ([490, 170], [520, 200]),
            47: ([530, 170], [560, 200]),
            48: ([450, 210], [480, 240]),
            49: ([490, 210], [520, 240]),
            50: ([530, 210], [560, 240]),
            51: ([450, 250], [480, 280]),
            52: ([490, 250], [520, 280]),
            53: ([530, 250], [560, 280])

        }

    def full_cube(self):
        img = np.zeros(shape=(512, 700, 3), dtype=np.int16)
        for ax, (x, y) in self.axis.items():
            if (ax >= 0) and (ax <= 8):
                cv2.rectangle(img, pt1=(x[0], x[1]), pt2=(y[0], y[1]), color=(0, 255, 255), thickness=-1)
            elif (ax >= 9) and (ax <= 17):
                cv2.rectangle(img, pt1=(x[0], x[1]), pt2=(y[0], y[1]), color=(0, 0, 255), thickness=-1)
            elif (ax >= 18) and (ax <= 26):
                cv2.rectangle(img, pt1=(x[0], x[1]), pt2=(y[0], y[1]), color=(255, 0, 0), thickness=-1)
            elif (ax >= 27) and (ax <= 35):
                cv2.rectangle(img, pt1=(x[0], x[1]), pt2=(y[0], y[1]), color=(147, 20, 255), thickness=-1)
            elif (ax >= 36) and (ax <= 44):
                cv2.rectangle(img, pt1=(x[0], x[1]), pt2=(y[0], y[1]), color=(255, 255, 255), thickness=-1)
            else:
                cv2.rectangle(img, pt1=(x[0], x[1]), pt2=(y[0], y[1]), color=(0, 255, 0), thickness=-1)
        cv2.imwrite("full_cube.jpg", img)

    def current_full_cube(self, colors, img):
        color_1 = []
        color_1[:] = colors
        for idx, i in enumerate(color_1):
            if i == "U":
                cv2.rectangle(img, pt1=(self.axis[idx][0][0], self.axis[idx][0][1]),
                              pt2=(self.axis[idx][1][0], self.axis[idx][1][1]), color=(0, 255, 255), thickness=-1)
            elif i == "F":
                cv2.rectangle(img, pt1=(self.axis[idx][0][0], self.axis[idx][0][1]),
                              pt2=(self.axis[idx][1][0], self.axis[idx][1][1]), color=(0, 0, 255), thickness=-1)
            elif i == "R":
                cv2.rectangle(img, pt1=(self.axis[idx][0][0], self.axis[idx][0][1]),
                              pt2=(self.axis[idx][1][0], self.axis[idx][1][1]), color=(255, 0, 0), thickness=-1)
            elif i == "D":
                cv2.rectangle(img, pt1=(self.axis[idx][0][0], self.axis[idx][0][1]),
                              pt2=(self.axis[idx][1][0], self.axis[idx][1][1]), color=(147, 20, 255), thickness=-1)
            elif i == "L":
                cv2.rectangle(img, pt1=(self.axis[idx][0][0], self.axis[idx][0][1]),
                              pt2=(self.axis[idx][1][0], self.axis[idx][1][1]), color=(255, 255, 255), thickness=-1)
            else:
                data = self.axis[0][1][0]
                cv2.rectangle(img, pt1=(self.axis[idx][0][0], self.axis[idx][0][1]),
                              pt2=(self.axis[idx][1][0], self.axis[idx][1][1]), color=(0, 255, 0), thickness=-1)
        cv2.imwrite("full_current_cube.jpg", img)







