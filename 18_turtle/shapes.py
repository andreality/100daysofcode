from turtle import Turtle, Screen
from colour import Color


timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("palegreen4")
# draw_square(turtle)

# def draw_dashed_line(turtle, num_steps=15, dash_length=10):
#     for _ in range(0, num_steps):
#         turtle.forward(dash_length)
#         turtle.penup()
#         turtle.forward(dash_length)
#         turtle.pendown()

blue = Color("aquamarine")
pink = Color("pink")
red = Color("firebrick")
colors1 = list(blue.range_to(pink, 13))
colors2 = list(pink.range_to(red, 12))
# colors = colors1 + colors2
colors = list(pink.range_to(red, 25))


def draw_shape(turtle, num_sides, side_length):
    angle = 360 / num_sides
    turtle.begin_fill()
    for _ in range(0, num_sides):
        turtle.forward(side_length)
        turtle.left(angle)
    turtle.end_fill()


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
