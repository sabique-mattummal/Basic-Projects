from turtle import Turtle

FONT = ("Arial", 12, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        
        #storing the highest score into a txt file (Create a 'data.txt' in the same directory
        with open( "data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(220, 250)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score : {self.score}/nHigh Score : {self.highr_score}", align="center"
                   , font=FONT)
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open ("data.txt", mode ="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
        
    def increase_score(self):
        self.score += 1
        self.update_score()
