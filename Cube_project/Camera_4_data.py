import cv2
import imutils

from common import Common


class Camera_4_data:

    def __init__(self):
        self.camera_4_data_x = [144, 126, 145, 163, 200, 180, 178, 177, 157, 155, 153]
        self.camera_4_data_y = [71, 78, 86, 95, 110, 115, 140, 167, 113, 138, 168]
        self.camera_4 = []
        self.colors_4 = []
        self.colors_dummy = []

    def get_final_camera4(self, up_face, back_face, left_face):
        image = self.get_image_cam_4()
        camera_data_4 = self.get_camera_4_coordinates(self.camera_4_data_x, self.camera_4_data_y, image, self.camera_4)
        com = Common()
        ranges = com.get_boundaries()
        colors = com.get_camera_colors(ranges, camera_data_4, self.colors_4)
        ranges_colors = com.get_boundaries_colors()
        colors_colors = com.get_camera_only_colors(ranges_colors, camera_data_4, self.colors_dummy)
        print(colors_colors)
        up_face, back_face, left_face = self.data_camera_4_faces(colors, up_face, back_face, left_face)
        return up_face, back_face, left_face

    def get_image_cam_4(self):
        try:
            cap = cv2.VideoCapture(2)
            if cap.isOpened():
                ret, image_4 = cap.read()
                cap.release()
                image_4 = imutils.resize(image_4, width=300, height=300)
                cv2.imwrite("cube4.jpg", image_4)
                image_hsv = cv2.cvtColor(image_4, cv2.COLOR_BGR2HSV)
            else:
                print("Camera 1 did not open")
        except:
            print("camera 1 problem")
        return image_hsv

    def get_camera_4_coordinates(self, data_x, data_y, image_data, camera_4):
        for axis_x, axis_y in zip(data_x, data_y):
            color = image_data[axis_y, axis_x]
            camera_4.append(color)
        print(camera_4)
        return camera_4

    def data_camera_4_faces(self, camera_top, up, back, left):
        comm = Common()
        print(camera_top)
        if comm.sanity_check(camera_top):
            for idx, data in enumerate(camera_top):
                if idx == 0: up[5] = data
                if idx == 1: up[2] = data
                if idx == 2: up[1] = data
                if idx == 3: up[0] = data
                if idx == 4: left[1] = data
                if idx == 5: left[0] = data
                if idx == 6: left[3] = data
                if idx == 7: left[6] = data
                if idx == 8: back[2] = data
                if idx == 9: back[5] = data
                else:
                    back[8] = data
        else:
            print("Camera_4 data wrong Faces top front left")
        return up, back, left

