class Common:

    def __init__(self):
        self.appended_colors = ""
        self.Green_L = 0
        self.Black_U = 0
        self.Red_F = 0
        self.Blue_D = 0
        self.Yellow_R = 0
        self.pink_B = 0
        self.go_no_go = False

    def get_boundaries(self):
        colors = {
            'B': ([40, 50, 45], [100, 210, 255]), # Green
            'R': ([0, 50, 50], [19, 255, 255]),  # Red
            'F': ([93, 90, 70], [130, 255, 255]), # Blue
            'U': ([20, 75, 25], [44, 255, 255]), # yellow
            'D': ([85, 85, 70], [179, 255, 255]), # pink
            'L': ([0, 0, 0], [179, 255, 255])  # Black
        }
        return colors

    def get_boundaries_colors(self):
        colors1 = {
            'Green': ([40, 50, 45], [100, 210, 255]),
            'Red': ([0, 50, 50], [19, 255, 255]),
            'Blue': ([93, 90, 70], [130, 255, 255]),
            'Yellow': ([20, 75, 25], [44, 255, 255]),
            'pink': ([85, 85, 70], [179, 255, 255]),
            'black': ([0, 0, 0], [179, 255, 255])
        }
        return colors1

    def get_camera_colors(self, ranges_color, camera_color, colors):
        for idx, value in enumerate(camera_color):
            if len(colors) == idx:
                for color, (lower, upper) in ranges_color.items():
                    if (lower[0] <= value[0] <= upper[0]) & (lower[1] <= value[1] <= upper[1]) & (
                            lower[2] <= value[2] <= upper[2]):
                        colors.append(color)
                        break
            else:
                colors.append("NA")
                for color, (lower, upper) in ranges_color.items():
                    if (lower[0] <= value[0] <= upper[0]) & (lower[1] <= value[1] <= upper[1]) & (
                            lower[2] <= value[2] <= upper[2]):
                        colors.append(color)
                        break
        if len(colors) == 12:
                colors.append("NA")

        return colors

    def get_camera_only_colors(self, ranges_color_x, camera_color_x, colors_x):
        for idx, value in enumerate(camera_color_x):
            if len(colors_x) == idx:
                for color, (lower, upper) in ranges_color_x.items():
                    if (lower[0] <= value[0] <= upper[0]) & (lower[1] <= value[1] <= upper[1]) & (
                            lower[2] <= value[2] <= upper[2]):
                        colors_x.append(color)
                        break
            else:
                colors_x.append("NA")
                for color, (lower, upper) in ranges_color_x.items():
                    if (lower[0] <= value[0] <= upper[0]) & (lower[1] <= value[1] <= upper[1]) & (
                            lower[2] <= value[2] <= upper[2]):
                        colors_x.append(color)
                        break


        return colors_x

    def sanity_check(self, detected_camera_data):
        if "NA" in detected_camera_data:
            return False
        return True

    def appending_data(self, detected_color, up_U, right_R, front_F, down_D, left_L, back_B):
        detected_color.append(up_U)
        detected_color.append(right_R)
        detected_color.append(front_F)
        detected_color.append(down_D)
        detected_color.append(left_L)
        detected_color.append(back_B)
        for val in detected_color:
            for i in val:
                if i == "L":
                    self.Green_L += 1
                    self.appended_colors += str(i)
                elif i == "U":
                    self.Black_U += 1
                    self.appended_colors += str(i)
                elif i == "F":
                    self.Red_F += 1
                    self.appended_colors += str(i)
                elif i == "D":
                    self.Blue_D += 1
                    self.appended_colors += str(i)
                elif i == "R":
                    self.Yellow_R += 1
                    self.appended_colors += str(i)
                elif i == "B":
                    self.pink_B += 1
                    self.appended_colors += str(i)
        if self.pink_B != 9 or self.Yellow_R != 9 or self.Blue_D != 9 or self.Red_F != 9 or self.Black_U != 9 or self.Green_L != 9:
            print("U : " + str(self.Black_U))
            print("R : " + str(self.Yellow_R))
            print("B : " + str(self.pink_B))
            print("D : " + str(self.Blue_D))
            print("L : " + str(self.Green_L))
            print("F : " + str(self.Red_F))
            self.go_no_go = False
        else:
            self.go_no_go = True
        return self.appended_colors, self.go_no_go

