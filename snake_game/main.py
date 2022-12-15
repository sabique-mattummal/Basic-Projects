from turtle import Turtle, Screen
from snake import Snake
from score_board import Scoreboard
from food import Food
import time

#Screen setting

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("#65647C")
screen.title("Snake Game")
screen.tracer(0)

#import objects
snake = Snake()
food = Food()
score_board = Scoreboard()

#Controls

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#Game initialisation
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    #Collision
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            


screen.exitonclick()
