from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("green")
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.spawn()

    def spawn(self):
        xloc = random.randint(-13, 13) * 20
        yloc = random.randint(-13, 13) * 20
        self.penup()
        self.goto(x=xloc, y=yloc)


