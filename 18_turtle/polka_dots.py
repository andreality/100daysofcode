import colorgram
import turtle as t
import random
from turtleart.common import get_colour_list

t.colormode(1.0)
# colors = colorgram.extract("images/rave1.jpg", number_of_colors=10)
# rgb_colors = []
# for col in colors:
#     new_item = tuple(col.rgb)
#     rgb_colors.append(new_item)
# print(rgb_colors)

color_list = get_colour_list(first_colour="deeppink", second_colour="aquamarine", num_colours=10)

radius = 20
space = 75
timmy = t.Turtle()

timmy.speed("fastest")
num_dots = 10


def fill_line():
    for i in range(0, num_dots):
        color = random.choice(color_list).rgb
        timmy.pendown()
        timmy.pencolor(*color)
        timmy.fillcolor(*color)
        timmy.begin_fill()
        timmy.circle(radius=radius)
        timmy.end_fill()
        timmy.penup()
        timmy.forward(space)

y = -350
for i in range(0, 10):
    timmy.penup()
    timmy.goto(-350, y)
    fill_line()
    y += space

screen = t.Screen()
screen.colormode(255)
# screen.bgcolor("beige")
screen.exitonclick()