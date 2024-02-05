from turtle import Turtle

FONT = ("Courier", 20, "bold")
INITIAL_GAME_SPEED = 0.1
SPEED_DECREMENT = 0.9


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(x=-270, y=250)
        self.pencolor("black")
        self.game_speed = INITIAL_GAME_SPEED
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def write_game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=("Courier", 24, "bold"))

    def advance_level(self):
        self.level += 1
        self.game_speed = self.game_speed * SPEED_DECREMENT
        print(self.game_speed)
        self.write_level()

