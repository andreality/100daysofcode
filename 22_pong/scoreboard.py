from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = {"left": 0, "right": 0}
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(x=-50, y=250)
        self.write(self.score["left"], align=ALIGNMENT, font=FONT)
        self.goto(x=50, y=250)
        self.write(self.score["right"], align=ALIGNMENT, font=FONT)

    def update_score(self, side):
        self.score[side] += 1
        self.write_score()

    def write_game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over!", align=ALIGNMENT, font=FONT)
