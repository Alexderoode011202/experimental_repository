import random
import math
from math import floor
from typing import Tuple

class DirectionTracker():
    def __init__(self):
        self.current = random.choice(range(0,361))

    def get_direction(self) -> int:
        return self.current

    def invert_horizontal(self) -> None:
        """
        inverts the horizontal direction.
        is supposed to be used after collision with vertical object (-> |).
        """
        angle: int
        midle: int

        if self.current < 90:
            midle = 360
            ...
            self.current = midle - self.current
        elif 90 < self.current <180:
            midle = 180
            angle = midle - self.current
            angle = math.sqrt(angle**2)
            self.current = midle + angle

        elif 180 < self.current < 270:
            midle = 180
            angle = midle - self.current
            angle = math.sqrt(angle**2)
            self.current = midle - angle

        elif self.current > 270:
            midle = 270
            angle = midle - self.current
            angle = math.sqrt(angle**2)
            self.current = midle - angle

    def invert_vertical(self) -> None:
        """
        inverts the vertical direction.
        is supposed to be used after collision with horizontal object, movement -> _.
        """
        midle: int
        angle: int
        if self.current <=90:
            middle = 90
            angle = middle - self.current
            angle = math.sqrt(angle**2)
            self.current = middle + angle

        elif 90< self.current <=180:
            middle = 90
            angle = middle - self.current
            angle = math.sqrt(angle**2)
            self.current = middle - angle

        elif 180 < self.current <=270:
            middle = 270
            angle = middle-self.current
            angle = math.sqrt(angle**2)
            self.current = middle + angle
        elif self.current > 270:
            middle = 270
            angle = middle = self.current
            angle = math.sqrt(angle**2)
            self.current = middle-angle

    def get_grid_movement(self) -> Tuple[int, int]:
        x_axis: int
        y_axis: int
        degrees_per_grid = 360/40
        grid_point: int = floor(self.current/ degrees_per_grid)
        # up -> y-axis +
        # down -> y-axis -
        # left -> x-axis -
        # right -> x-axis +

        # right
        if 5 < grid_point <=15:
            x_axis = 5
            y_axis = 10 - grid_point

        # left
        elif 25 < grid_point <= 35:
            x_axis = -5
            y_axis = grid_point - 30

        # bottom
        elif 15 < grid_point <= 25:
            y_axis = -5
            x_axis = 20 - grid_point
        
        # top
        elif grid_point >= 35 or grid_point <= 5:
            y_axis = 5
            if grid_point >= 35:
                x_axis = grid_point - 40
            else:
                x_axis = grid_point

        return (x_axis, y_axis)




