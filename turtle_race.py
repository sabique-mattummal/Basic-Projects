from turtle import Turtle, Screen
import random

#Pre setting of screen and data list
screen = Screen()
screen.setup(height=400,width=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which color will win the race ?")
colors = ["red", "orange", "yellow", "green", "blue"]
y_positions = [-100, -40, 0, 40, 100]
all_turtles = []

#Turtles creation

for turtle in range(5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle])
    new_turtle.goto(x = -230, y = y_positions[turtle])
    all_turtles.append(new_turtle)

is_race_on = True

#Race initialization

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                screen.title(titlestring=f"Your {winning_color} turtle won.")
            else:
                screen.title(titlestring=f"You lost.\n{winning_color} turtle won")
        turtle.forward(random.randint(3, 20))

screen.exitonclick()
