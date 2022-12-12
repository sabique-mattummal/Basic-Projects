from turtle import Turtle
from random import randint

#Inherittence from super class

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=.75, stretch_len=.75)
        self.color("lightgreen")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = randint(-260, 260)
        rand_y = randint(-270, 270)
        self.goto(rand_x, rand_y)
