from turtle import Turtle
from helpers import get_colour_list
import random


STARTING_MOVE_DISTANCE = 5
HIT_DISTANCE = 22
MOVE_INCREMENT = 10
COLORS = get_colour_list(first_colour="pink", second_colour="aquamarine", num_colours=10)


class Car(Turtle):
    def __init__(self):
        super().__init__()
        colour_int = random.randint(0, len(COLORS) - 1)
        starting_y = random.randint(-250, 250)
        self.color(*COLORS[colour_int].rgb)
        self.shape("square")
        self.turtlesize(stretch_len=2)
        self.penup()
        self.setheading(180)
        self.goto(x=280, y=starting_y)

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)

    def detect_collision(self, player):
        check_x = abs(self.xcor() - player.xcor())
        check_y = abs(self.ycor() - player.ycor())
        if check_x < HIT_DISTANCE and check_y < HIT_DISTANCE:
            return True
        else:
            return False

