from colour import Color


def get_colour_list(first_colour, second_colour, num_colours=10):
    first = Color(first_colour)
    second = Color(second_colour)
    return list(first.range_to(second, num_colours))


def draw_shape(turtle, num_sides, side_length):
    angle = 360 / num_sides
    turtle.begin_fill()
    for _ in range(0, num_sides):
        turtle.forward(side_length)
        turtle.left(angle)
    turtle.end_fill()
