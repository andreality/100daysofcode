from turtle import Turtle
from helpers import create_move_function

RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270

WALL_BOUNDARY = 280


def create_new_turtle():
    new_turtle = Turtle(shape="square")
    new_turtle.speed("fastest")
    new_turtle.color("white")
    new_turtle.penup()
    return new_turtle


class Snake:
    def __init__(self, screen, num_segments=3):
        self.segment_list = [create_new_turtle()]
        self.head.setheading(0)

        for i in range(0, num_segments - 1):
            self.grow()

        # keybindings
        self.down_key = "j"
        self.up_key = "k"
        self.left_key = "h"
        self.right_key = "l"

        screen.listen()
        screen.onkey(key=self.down_key, fun=self.down)
        screen.onkey(key=self.up_key, fun=self.up)
        screen.onkey(key=self.left_key, fun=self.left)
        screen.onkey(key=self.right_key, fun=self.right)

    @property
    def length(self):
        return len(self.segment_list)

    @property
    def head(self):
        return self.segment_list[0]

    @property
    def head_position(self):
        return self.head.position()

    @property
    def heading(self):
        return self.head.heading()

    def up(self):
        if self.heading != DOWN:
            self.head.setheading(to_angle=UP)

    def down(self):
        if self.heading != UP:
            self.head.setheading(to_angle=DOWN)

    def right(self):
        if self.heading != LEFT:
            self.head.setheading(to_angle=RIGHT)

    def left(self):
        if self.heading != RIGHT:
            self.head.setheading(to_angle=LEFT)

    def move(self):
        previous_position = self.head_position
        self.head.forward(20)
        for i in range(1, self.length):
            segment = self.segment_list[i]
            current_position = segment.position()
            segment.goto(*previous_position)
            previous_position = current_position

    def grow(self):
        last_segment = self.segment_list[-1]
        last_position = last_segment.position()
        new_turtle = create_new_turtle()
        if self.heading == RIGHT:
            new_turtle.goto(last_position[0] - 20, last_position[1])
        if self.heading == LEFT:
            new_turtle.goto(last_position[0] + 20, last_position[1])
        if self.heading == UP:
            new_turtle.goto(last_position[0], last_position[1] - 20)
        if self.heading == DOWN:
            new_turtle.goto(last_position[0], last_position[1] + 20)
        self.segment_list.append(new_turtle)

    def detect_collision_with_wall(self):
        if abs(self.head.xcor()) > WALL_BOUNDARY or abs(self.head.ycor()) > WALL_BOUNDARY:
            return True
        else:
            return False

    def detect_collision_with_tail(self):
        positions = [seg.position() for seg in self.segment_list]
        if self.head_position in positions[1:]:
            return True
        else:
            return False


