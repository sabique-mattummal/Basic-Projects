from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

#Functions

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

#Key assign

screen.listen()
screen.onkey(move_forward, "Right")
screen.onkey(move_backward, "Left")
screen.onkey(turn_left, "Up")
screen.onkey(turn_right, "Down")
screen.onkey(clear, "c")

screen.exitonclick()






