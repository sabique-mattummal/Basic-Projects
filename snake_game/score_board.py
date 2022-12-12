from turtle import Turtle

FONT = ("Arial", 22, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(220, 250)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score : {self.score}", align="center"
                   , font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER\nFinal Score : {self.score}",
                   align="center", font=("Arial", 36, "italic"))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
