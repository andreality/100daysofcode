from turtle import Turtle, Screen
import random
from colour import Color

step_length = 25

pink = Color("pink")
red = Color("firebrick")
colors = list(pink.range_to(red, 25))


def move(turtle):
    color = random.choice(colors)
    turtle.pencolor(*color.rgb)
    rotation_times = random.randint(0, 3)
    turtle.left(90 * rotation_times)
    turtle.forward(step_length)


timmy = Turtle()
timmy.width(10)
timmy.speed("fastest")
while True:
    move(timmy)

screen = Screen()
screen.colormode(1.0)
screen.exitonclick()
