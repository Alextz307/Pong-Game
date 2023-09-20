from turtle import Turtle
import time


FLIP = -1
NO_FLIP = 1


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.delta_x = -0.8
        self.delta_y = -0.8

    def move(self):
        new_x = self.xcor() + self.delta_x
        new_y = self.ycor() + self.delta_y
        self.setposition(new_x, new_y)

    def bounce(self, change_x, change_y):
        self.delta_x *= change_x
        self.delta_y *= change_y

    def get_sgn(self):
        sgn_x = -1 if self.delta_x < 0 else 1
        sgn_y = -1 if self.delta_y < 0 else 1

        return sgn_x, sgn_y

    def increase_speed(self):
        sgn_x, sgn_y = self.get_sgn()

        self.delta_x = sgn_x * (abs(self.delta_x) + 0.2)
        self.delta_y = sgn_y * (abs(self.delta_y) + 0.2)

    def reset_ball(self):
        self.setposition(0, 0)

        self.bounce(FLIP, NO_FLIP)

        sgn_x, sgn_y = self.get_sgn()

        self.delta_x = 0.8 * sgn_x
        self.delta_y = 0.8 * sgn_y

        time.sleep(0.1)
