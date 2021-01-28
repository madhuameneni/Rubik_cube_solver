import cv2
import imutils

from common import Common


class Camera_3_data:

    def __init__(self):
        self.camera_3_data_x = [126, 95, 64, 40, 113, 108, 85, 84, 80, 39, 139]
        self.camera_3_data_y = [137, 122, 135, 146, 58, 89, 27, 51, 90, 119, 112]
        self.camera_3 = []
        self.colors_3 = []
        self.colors_dummy = []

    def get_final_camera3(self, down_face, front_face, left_face):
        image = self.get_image_cam_3()
        camera_data_3 = self.get_camera_3_coordinates(self.camera_3_data_x, self.camera_3_data_y, image, self.camera_3)
        com = Common()
        ranges = com.get_boundaries()
        colors = com.get_camera_colors(ranges, camera_data_3, self.colors_3)
        ranges_colors = com.get_boundaries_colors()
        colors_colors = com.get_camera_only_colors(ranges_colors, camera_data_3, self.colors_dummy)
        print(colors_colors)
        down_face, front_face, left_face = self.data_camera_3_faces(colors, down_face, front_face, left_face)
        return down_face, front_face, left_face

    def get_image_cam_3(self):
        try:
            cap = cv2.VideoCapture(4)
            if cap.isOpened():
                ret, image_3 = cap.read()
                cap.release()
                image_3 = imutils.resize(image_3, width=300, height=300)
                cv2.imwrite("cube3.jpg", image_3)
                image_hsv = cv2.cvtColor(image_3, cv2.COLOR_BGR2HSV)
            else:
                print("Camera 3 did not open")
        except:
            print("camera 3 problem")
        return image_hsv

    def get_camera_3_coordinates(self, data_x, data_y, image_data, camera_3):
        for axis_x, axis_y in zip(data_x, data_y):
            color = image_data[axis_y, axis_x]
            camera_3.append(color)
        print(camera_3)
        return camera_3

    def data_camera_3_faces(self, camera_top, down, front, left):
        comm = Common()
        print(camera_top)
        if comm.sanity_check(camera_top):
            for idx, data in enumerate(camera_top):
                if idx == 0: down[1] = data
                if idx == 1: down[0] = data
                if idx == 2: down[3] = data
                if idx == 3: down[6] = data
                if idx == 4: front[3] = data
                if idx == 5: front[6] = data
                if idx == 6: left[2] = data
                if idx == 7: left[5] = data
                if idx == 8: left[8] = data
                if idx == 9: left[7] = data
                else:
                    front[7] = data
        else:
            print("Camera_3 data wrong Faces top front left")
        return down, front, left
