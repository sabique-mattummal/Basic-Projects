from turtle import Turtle, Screen
from ball import Ball
from score import Score
from paddle import Paddle
import time

#Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.title("THE PONG GAME")
screen.bgcolor("black")
screen.tracer(0)

#Creation of objects
ball= Ball()
score = Score()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

#On-Screen Functions
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

#Game initialisation
game_on = True
while game_on:
    #Slow Down
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #Bounce from Top and Bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    #Collision with Paddles 
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or \
            ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #If Paddle miss the ball, point to oppositte player
    if ball.xcor() > 380:
        ball.reset()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset()
        score.r_point()


screen.exitonclick()
