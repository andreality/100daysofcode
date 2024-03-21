import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
states = pd.read_csv("50_states.csv")
states["state"] = states["state"].str.lower()
states["state"] = states["state"].str.strip()
if "florida" in states["state"]:
    print("yes")

image_path = "blank_states_img.gif"
screen.addshape(image_path)

map_turtle = turtle.Turtle()
map_turtle.shape(image_path)

marker_turtle = turtle.Turtle()


game_on = True
while game_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state name?")
    print(answer_state)
    if answer_state is None:
        continue
    if answer_state in states["state"]:
        state_row = states.loc[states["state"] == answer_state]
        print(state_row)
        marker_turtle.goto(x=state_row["x"], y=state_row["y"])
# def get_mouse_click_coords(x, y):
#     print(x, y)
# turtle.onclick(get_mouse_click_coords)


screen.exitonclick()