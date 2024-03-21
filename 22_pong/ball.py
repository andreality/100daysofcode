from turtle import Turtle
import random

VERTICAL_WALL_BOUNDARY = 280
HORIZONTAL_WALL_BOUNDARY = 330
STARTING_ANGLES = [0, 180, 15, 345, 195, 165, 30, 330, 220, 150, 45, 315, 225, 135]


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.reset()

    def reset(self):
        self.goto(x=0, y=0)
        random_heading = random.choice(STARTING_ANGLES)
        self.setheading(random_heading)

    def move(self):
        self.forward(20)

    def detect_wall_collision(self):
        if abs(self.ycor()) > VERTICAL_WALL_BOUNDARY:
            self.setheading(360 - self.heading())
        else:
            return

    def detect_paddle_contact(self, paddle):
        if abs(self.ycor() - paddle.ycor()) < 50:
            self.setheading(self.heading() - 180)
            return True
        else:
            return False

    def detect_score(self, left_paddle, right_paddle):
        if self.xcor() > HORIZONTAL_WALL_BOUNDARY:
            paddle_hit = self.detect_paddle_contact(paddle=right_paddle)
            scoring_side = "left" if not paddle_hit else "none"
        elif self.xcor() < -HORIZONTAL_WALL_BOUNDARY:
            paddle_hit = self.detect_paddle_contact(paddle=left_paddle)
            scoring_side = "right" if not paddle_hit else "none"
        else:
            scoring_side = "none"
        return scoring_side



