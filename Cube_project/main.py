from Camera_1_data import Camera_1_data
from Camera_2_data import Camera_2_data
from Camera_3_data import Camera_3_data
from Camera_4_data import Camera_4_data
from common import Common
from cube_algorithm import Cube_algorithm
import numpy as np

from cube_rep import Cube_rep

face_back = ["none", "none", "none", "none", "B", "none", "none", "none", "none"]
face_right = ["none", "none", "none", "none", "R", "none", "none", "none", "none"]
face_down = ["none", "none", "none", "none", "D", "none", "none", "none", "none"]
face_front = ["none", "none", "none", "none", "F", "none", "none", "none", "none"]
face_left = ["none", "none", "none", "none", "L", "none", "none", "none", "none"]
face_up = ["none", "none", "none", "none", "U", "none", "none", "none", "none"]
final_data_cube = []
current_img = np.zeros(shape=(512, 700, 3), dtype=np.int16)


def main():
    cam_1 = Camera_1_data()
    cam_2 = Camera_2_data()
    cam_3 = Camera_3_data()
    cam_4 = Camera_4_data()
    front1, right1, up1 = cam_1.get_final_camera1(face_front, face_right, face_up)
    right1, back1, down1 = cam_2.get_final_camera2(right1, face_back, face_down)
    down1, front1, left1 = cam_3.get_final_camera3(down1, front1, face_left)
    up1, back1, left1 = cam_4.get_final_camera4(up1, back1, left1)
    print(up1)
    print(right1)
    print(front1)
    print(down1)
    print(left1)
    print(back1)
    com = Common()
    value, go_no_go = com.appending_data(final_data_cube, up1, right1, front1, down1, left1, back1)
    print(value)
    current = Cube_rep()
    # current.full_cube()
    current.current_full_cube(value, current_img)
    cube = Cube_algorithm()
    solve_data = cube.solve_cube("BBRUURBBFDDDRRLUFFUULUFBULLRFFRDDBLDLFLULLUFFBDDDBRRBR")
    final_data = cube.solution_to_array(solve_data, final_data_cube)
    print(solve_data)
    print(final_data)
    print(len(final_data))
    if go_no_go:
        cube = Cube_algorithm()
        solve_data = cube.solve_cube(value)
        final_data = cube.solution_to_array(solve_data, final_data_cube)
        print(solve_data)
        print(final_data)
        print(len(final_data))
    else:
        print("some issue found you need to debug the issue")

    return True


if __name__ == '__main__':
    main()
