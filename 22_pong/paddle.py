from turtle import Turtle


def create_new_turtle(start_x, start_y):
    new_turtle = Turtle(shape="square")
    new_turtle.speed("fastest")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(x=start_x, y=start_y)
    return new_turtle


class Paddle(Turtle):
    def __init__(self, x_coord, up_key, down_key):
        super().__init__(shape="square")
        self.setheading(90)
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(x=x_coord, y=0)
        self.turtlesize(stretch_len=5)

        self.up_key = up_key
        self.down_key = down_key

    def move_up(self):
        self.setheading(90)
        self.forward(20)

    def move_down(self):
        self.setheading(270)
        self.forward(20)
