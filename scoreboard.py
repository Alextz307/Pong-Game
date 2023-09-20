from turtle import Turtle


ALIGN = 'center'
FONT = ('Courier', 80, 'normal')
LEFT_COORDINATES = (-100, 200)
RIGHT_COORDINATES = (100, 200)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor('white')
        self.speed('fastest')
        self.left_score = 0
        self.right_score = 0
        self.write_score()

    def write_score(self):
        self.clear()

        self.goto(LEFT_COORDINATES)
        self.write(arg=self.left_score, align=ALIGN, font=FONT)

        self.goto(RIGHT_COORDINATES)
        self.write(arg=self.right_score, align=ALIGN, font=FONT)

    def update_score(self, delta_left, delta_right):
        self.left_score += delta_left
        self.right_score += delta_right
        self.write_score()
