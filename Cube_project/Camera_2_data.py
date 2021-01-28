import cv2
import imutils

from common import Common


class Camera_2_data:

    def __init__(self):
        self.camera_2_data_x = [71, 92, 91, 90, 141, 117, 118, 120, 152, 142, 122, 79, 55]
        self.camera_2_data_y = [52, 29, 62, 98, 39, 29, 60, 94, 109, 131, 124, 142, 161]
        self.camera_2 = []
        self.colors_2 = []
        self.colors_dummy = []

    def get_final_camera2(self, right_face, back_face, down_face):
        image = self.get_image_cam_2()
        camera_data_2 = self.get_camera_2_coordinates(self.camera_2_data_x, self.camera_2_data_y, image, self.camera_2)
        com = Common()
        ranges = com.get_boundaries()
        colors = com.get_camera_colors(ranges, camera_data_2, self.colors_2)
        ranges_colors = com.get_boundaries_colors()
        colors_colors = com.get_camera_only_colors(ranges_colors, camera_data_2, self.colors_dummy)
        print(colors_colors)
        right_face, back_face, down_face = self.data_camera_2_faces(colors,  right_face, back_face, down_face)
        return  right_face, back_face, down_face

    def get_image_cam_2(self):
        try:
            cap = cv2.VideoCapture(0)
            if cap.isOpened():
                ret, image_2 = cap.read()
                cap.release()
                image_2 = imutils.resize(image_2, width=300, height=300)
                cv2.imwrite("cube2.jpg", image_2)
                image_hsv = cv2.cvtColor(image_2, cv2.COLOR_BGR2HSV)
            else:
                print("Camera 2 did not open")
        except:
            print("camera 2 problem")
        return image_hsv

    def get_camera_2_coordinates(self, data_x, data_y, image_data, camera_2):
        for axis_x, axis_y in zip(data_x, data_y):
            color = image_data[axis_y, axis_x]
            camera_2.append(color)
        print(camera_2)
        return camera_2

    def data_camera_2_faces(self, camera_top, right, back, down):
        comm = Common()
        print(camera_top)
        if comm.sanity_check(camera_top):
            for idx, data in enumerate(camera_top):
                if idx == 0: right[1] = data
                if idx == 1: right[2] = data
                if idx == 2: right[5] = data
                if idx == 3: right[8] = data
                if idx == 4: back[1] = data
                if idx == 5: back[0] = data
                if idx == 6: back[3] = data
                if idx == 7: back[6] = data
                if idx == 8: back[7] = data
                if idx == 9: down[7] = data
                if idx == 10: down[8] = data
                if idx == 11:down[5] = data
                else:
                    down[2] = data
        else:
            print("Camera_2 data wrong Faces top front left")
        return right, back, down
