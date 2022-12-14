from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-250, 220)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Level\n{self.level}",
                   align="center", font=("Arial", 24, "normal"))

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER",
                   align="center", font=("Arial", 34, "normal"))

