from turtle import Turtle

#Constants

START_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE = 250

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.goto_start()
        self.setheading(90)

    def goto_start(self):
        self.goto(START_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def is_it_finished(self):
        return self.ycor() > FINISH_LINE
