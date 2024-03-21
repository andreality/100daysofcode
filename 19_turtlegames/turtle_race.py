from turtle import Turtle, Screen
import random

screen = Screen()
screen_height = 400
screen_width = 500
screen.setup(width=500, height=400)


colors = ["red", "orange", "green", "blue", "purple", "pink"]
num_turtles = 6


def create_turtles():
    turtle_list = []
    for i in range(0, num_turtles):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[i])
        new_turtle.pencolor(colors[i])
        new_turtle.speed("fastest")
        turtle_list.append(new_turtle)
    return turtle_list


def reset_race():
    turtle_list = create_turtles()
    y = -80
    turtle_spacing = screen_height / (2 * num_turtles)
    t = Turtle()
    t.penup()
    t.setposition(x=210, y=200)
    t.pendown()
    t.setposition(x=210, y=-200)
    for tt in turtle_list:
        tt.penup()
        tt.setposition(x=-240, y=y)
        y += turtle_spacing
    return turtle_list


def get_user_bet():
    user_bet = screen.textinput(title="Make your bet!",
                                prompt="Pick the colour of the turtle you think will win the race:")
    while user_bet not in colors:
        user_bet = screen.textinput(title="Make your bet!",
                                    prompt="Please enter a valid colour: red, orange,  green, blue, purple, pink.")
    return user_bet

def get_user_chaos():
    alcohol_level = screen.textinput(title="Have your turtles been drinking?",
                                           prompt="Enter a drunkenness level between 1 and 100.")
    haywire_probability = float(alcohol_level) / 100
    return haywire_probability


def run_race(turtle_list, haywire_probability):
    game_on = True
    penup = True
    while game_on:
        for t in turtle_list:
            if penup:
                t.penup()
            else:
                t.pendown()
            step = random.random() * 10
            # with some probability, turtle veers off course
            haywire_draw = random.random()
            if haywire_draw < haywire_probability:
                angle_delta = random.choice([5, 10, 15, -5, -10, -15])
                current_heading = t.heading()
                t.setheading(to_angle=current_heading + angle_delta)
            t.forward(step)
            turtle_position = t.position()
            # print(turtle_position)
            if turtle_position[0] >= 210:
                game_on = False
                winning_color = t.color()[0]
        penup = not penup
    return winning_color

keep_playing = True
while keep_playing:
    turtle_list = reset_race()
    user_bet = get_user_bet()
    haywire_prob = get_user_chaos()
    winning_color = run_race(turtle_list, haywire_prob)

    if winning_color == user_bet:
        screen.title(f"Your turtle won! Way to go {user_bet}y!")
    else:
        screen.title(f"Your turtle lost! You suck {user_bet}y!")

    play_again = screen.textinput(title="Play Again?", prompt="Do you want to play again Y/N?").lower()
    if play_again == "n":
        keep_playing = False
    screen.clear()

screen.exitonclick()