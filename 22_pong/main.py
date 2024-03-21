from turtle import Screen
from helpers import draw_line
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


PADDLE_LENGTH = 4

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)  # turn off animation
draw_line(x_from=0, y_from= 300, x_to=0, y_to=-300)

# initialize objects
left_paddle = Paddle(x_coord=-350, up_key="w", down_key="s")
right_paddle = Paddle(x_coord=350, up_key="Up", down_key="Down")
scoreboard = ScoreBoard()
ball = Ball()

screen.listen()
screen.onkey(key=right_paddle.down_key, fun=right_paddle.move_down)
screen.onkey(key=right_paddle.up_key, fun=right_paddle.move_up)
screen.onkey(key=left_paddle.down_key, fun=left_paddle.move_down)
screen.onkey(key=left_paddle.up_key, fun=left_paddle.move_up)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.08)
    ball.move()
    ball.detect_wall_collision()
    scoring_side = ball.detect_score(left_paddle=left_paddle, right_paddle=right_paddle)
    if scoring_side == "none":
        continue
    else:
        scoreboard.update_score(side=scoring_side)
        ball.reset()
        ball.move()

screen.exitonclick()
