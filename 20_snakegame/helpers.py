

def create_move_function(turtle_object, angle, step_length=10):
    def move_func(angle=angle, step_length=step_length):
        turtle_object.setheading(to_angle=angle)
        turtle_object.forward(step_length)
    return move_func
