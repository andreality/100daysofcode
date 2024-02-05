from colour import Color


def get_colour_list(first_colour, second_colour, num_colours=10):
    first = Color(first_colour)
    second = Color(second_colour)
    return list(first.range_to(second, num_colours))