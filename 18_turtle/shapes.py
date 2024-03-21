from turtle import Turtle, Screen
from colour import Color
from turtleart.common import draw_shape, get_colour_list

timmy = Turtle()
timmy.speed("fastest")

colors = get_colour_list(first_colour="pink", second_colour="firebrick", num_colours=25)

timmy.width(2)
timmy.penup()
timmy.goto(-100, -375)
timmy.pendown()
size = 100

for i in reversed(range(2, 25)):
    rgb = colors[i].rgb
    timmy.pencolor(*rgb)
    timmy.fillcolor(*rgb)
    draw_shape(timmy, num_sides=i, side_length=size)

screen = Screen()
screen.colormode(1.0)
screen.bgcolor("black")
screen.exitonclick()
