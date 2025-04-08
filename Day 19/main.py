from turtle import Turtle, Screen
import random

is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = {}

my_screen = Screen()
my_screen.setup(width=1200, height=400)
user_bet = my_screen.textinput(title="Make a bet!", prompt="Bet which color turlte will win?")
print(user_bet)
if user_bet: is_race_on = True

for color in colors:
    turtle = Turtle(shape='turtle')
    turtle.shapesize(outline=1)
    turtle.color("black", color)
    turtle.penup()
    turtle.goto(x=-550, y=(155-(len(turtles) * 60)))
    turtles[color] = turtle

while is_race_on:
    for color in turtles:
        turtles[color].forward(random.randint(5,30))
        if turtles[color].xcor() >= 550:
            is_race_on = False
            if color.lower() == user_bet.lower(): print(f"You won - {color} turtle won!")
            else: print(f"You lost - {color} turtle won!")

my_screen.exitonclick()