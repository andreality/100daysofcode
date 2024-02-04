from turtle import Turtle


def draw_line(x_from, x_to, y_from, y_to):
    line_turtle = Turtle()
    line_turtle.pencolor("white")
    line_turtle.goto(x=x_from, y=y_from)
    line_turtle.goto(x=x_to, y=y_to)
