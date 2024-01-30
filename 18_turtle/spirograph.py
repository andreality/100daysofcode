from turtle import Turtle, Screen
from turtleart.common import get_colour_list


timmy = Turtle()
timmy.speed("fastest")
radius = 100
num_circles = 75
angle = 360 / num_circles
num_colours = int(num_circles / 2) + 1
color1 = "orchid"
color2 = "turquoise"
colors1 = get_colour_list(first_colour=color1, second_colour=color2, num_colours=num_colours)
colors2 = get_colour_list(first_colour=color2, second_colour=color1, num_colours=num_colours)
colors = colors1 + colors2

for i in range(0, num_circles):
    timmy.pencolor(*colors[i].rgb)
    timmy.circle(radius=radius)
    timmy.left(angle=angle) # can also use setheading

screen = Screen()
screen.colormode(1.0)
screen.bgcolor("black")
screen.exitonclick()