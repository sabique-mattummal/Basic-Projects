from turtle import Turtle
import random

#Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
INIT_SPEED = 5
MOVE_UP = 5


class Carmanager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = INIT_SPEED

    def create_cars(self):
        random_chance = random.randint(1, 5)
        if random_chance == 5:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(280, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            
    def level_up(self):
        self.car_speed += MOVE_UP
