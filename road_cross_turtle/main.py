#Import class objects

from turtle import Turtle, Screen
from player import Player
from score_board import Scoreboard
from car_manager import Carmanager
import time

#Screen setup

screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

#Creation of objects

player = Player()
cars= Carmanager()
score_board = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

#Game initialisation

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    if player.is_it_finished():
        player.goto_start()
        cars.level_up()
        score_board.increase_level()

screen.exitonclick()
