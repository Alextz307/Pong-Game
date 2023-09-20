from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.update()

screen.listen()

screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')

game_is_on = True

FLIP = -1
NO_FLIP = 1


def refresh():
    ball.move()
    screen.update()


while game_is_on:
    refresh()

    # Detect collisions with top and bottom walls
    if abs(ball.ycor()) >= 285:
        ball.bounce(NO_FLIP, FLIP)

    # Detect a collision with the right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 325:
        ball.bounce(FLIP, NO_FLIP)
        ball.increase_speed()

    # Detect collision with the left paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -325:
        ball.bounce(FLIP, NO_FLIP)
        ball.increase_speed()

    # Left scores
    if ball.xcor() > 385:
        ball.reset_ball()
        scoreboard.update_score(1, 0)

    # Right scores
    if ball.xcor() < -385:
        ball.reset_ball()
        scoreboard.update_score(0, 1)

screen.exitonclick()
