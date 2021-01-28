import cv2
import imutils

from common import Common


class Camera_1_data:

    def __init__(self):
        self.camera_1_data_x = [109, 130, 148, 151, 146, 193, 175, 174, 175, 164, 138, 118, 138]
        self.camera_1_data_y = [99, 110, 126, 143, 174, 166, 173, 144, 120, 95, 89, 79, 74]
        self.camera_1 = []
        self.colors_1 = []
        self.colors_dummy = []

    def get_final_camera1(self, front_face, right_face, up_face):
        image = self.get_image_cam_1()
        # image = cv2.imread("cube1.jpg")
        # image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        camera_data_1 = self.get_camera_1_coordinates(self.camera_1_data_x, self.camera_1_data_y, image, self.camera_1)
        com = Common()
        ranges = com.get_boundaries()
        colors = com.get_camera_colors(ranges, camera_data_1, self.colors_1)
        ranges_colors = com.get_boundaries_colors()
        colors_colors = com.get_camera_only_colors(ranges_colors, camera_data_1, self.colors_dummy)
        print(colors_colors)
        front_face, right_face, up_face = self.data_camera_1_faces(colors, front_face, right_face, up_face)
        return front_face, right_face, up_face

    def get_image_cam_1(self):
        try:
            cap = cv2.VideoCapture(3)
            if cap.isOpened():
                ret, image_1 = cap.read()
                cap.release()
                image_1 = imutils.resize(image_1, width=300, height=300)
                cv2.imwrite("cube1.jpg", image_1)
                image_hsv = cv2.cvtColor(image_1, cv2.COLOR_BGR2HSV)
            else:
                print("Camera 1 did not open")
        except:
            print("camera 1 problem")
        return image_hsv

    def get_camera_1_coordinates(self, data_x, data_y, image_data, camera_1):
        for axis_x, axis_y in zip(data_x, data_y):
            color = image_data[axis_y, axis_x]
            camera_1.append(color)
        print(camera_1)
        return camera_1

    def data_camera_1_faces(self, camera_top, front, right, up):
        comm = Common()
        print(camera_top)
        if comm.sanity_check(camera_top):
            for idx, data in enumerate(camera_top):
                if idx == 0: front[0] = data
                if idx == 1: front[1] = data
                if idx == 2: front[2] = data
                if idx == 3: front[5] = data
                if idx == 4:front[8] = data
                if idx == 5:right[7] = data
                if idx == 6: right[6] = data
                if idx == 7:right[3] = data
                if idx == 8:right[0] = data
                if idx == 9: up[8] = data
                if idx == 10: up[7] = data
                if idx == 11:up[6] = data
                else:
                    up[3] = data
        else:
            print("Camera_1 data wrong Faces top front left")
        return front, right, up

