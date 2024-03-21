from turtle import Turtle, Screen
import random
from turtleart.common import get_colour_list


step_length = 25
colors = get_colour_list(first_colour="pink", second_colour="aquamarine", num_colours=10)

def move_randomly(turtle):
    color = random.choice(colors)
    turtle.pencolor(*color.rgb)
    rotation_times = random.randint(0, 3)
    turtle.setheading(to_angle=90 * rotation_times)
    turtle.forward(step_length)


timmy = Turtle()
timmy.width(10)
timmy.speed("fastest")
while True:
    move_randomly(timmy)

screen = Screen()
screen.exitonclick()
