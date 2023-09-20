from turtle import Turtle


MOVE_DISTANCE = 25


class Paddle(Turtle):

    def __init__(self, starting_position):
        super().__init__()
        self.penup()
        self.speed('fastest')
        self.color('white')
        self.shape('square')
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.setposition(starting_position)

    def move_by(self, delta_y):
        new_y = self.ycor() + delta_y

        if abs(new_y) < 260:
            self.goto(self.xcor(), new_y)

    def up(self):
        self.move_by(MOVE_DISTANCE)

    def down(self):
        self.move_by(-MOVE_DISTANCE)
