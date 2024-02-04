from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
step_length = 10

def move_forward():
    tim.forward(step_length)


def move_backward():
    tim.backward(step_length)


def move_ccw():
    tim.circle(radius=50, extent=50)


def move_cw():
    turn()
    tim.circle(radius=50, extent=50)


def turn():
    current_heading = tim.heading()
    # print(current_heading)
    tim.setheading(current_heading + 180)


def create_move_function(angle, step_length=10):
    def move_func(angle=angle, step_length=step_length):
        tim.setheading(to_angle=angle)
        tim.forward(step_length)
    return move_func


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


if True:
    screen.listen()
    screen.onkey(key="j", fun=create_move_function(angle=270))
    screen.onkey(key="k", fun=create_move_function(angle=90))
    screen.onkey(key="h", fun=create_move_function(angle=180))
    screen.onkey(key="l", fun=create_move_function(angle=0))
    screen.onkey(key="a", fun=move_ccw)
    screen.onkey(key="d", fun=move_cw)
    screen.onkey(key="f", fun=move_forward)
    screen.onkey(key="b", fun=move_backward)
    screen.onkey(key="c", fun=clear_screen)
    screen.exitonclick()

# w = forwards
# s = backwards
# a = counter clockwise
# d = clockwise
# c = clear drawings