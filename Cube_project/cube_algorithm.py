from itertools import repeat
from re import split

import kociemba


class Cube_algorithm:

    def solve_cube(self, cube_current_colors):
        data = kociemba.solve(cube_current_colors)
        return data

    def solution_to_array(self, data1, final_array):
        final_array_value = ""
        array_data = data1.split(" ")
        for idx, value in enumerate(array_data):
            if len(array_data) == idx+1:
                final_array_value += value + ""
            else:
                final_array_value += value + ","
        return final_array_value
