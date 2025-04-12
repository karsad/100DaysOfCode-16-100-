import turtle
from turtle import Screen, Turtle
import pandas

states_guessed = 0
guessed_states = []

my_screen = Screen()
my_screen.title("US States Quiz Game")
image = "blank_states_img.gif"
my_screen.addshape(image)

turtle.shape(image)
my_turtle = Turtle()
my_turtle.penup()
my_turtle.hideturtle()

data = pandas.read_csv("50_states.csv")

while states_guessed < 50:
    user_input = my_screen.textinput(f"{states_guessed}/50 States Correct", "What's another state name?").title()
    if user_input == "Exit":
        output_data = []
        states = data.state.to_list()
        for state in states:
            if state in guessed_states: states.remove(state)
        pandas.DataFrame(states).to_csv("states_to_learn.csv")
        break


    result = data.state[data.state == user_input]
    if result.to_list():
        states_guessed += 1
        guessed_states.append(user_input)
        x_cor = data.x[data.state == user_input].item()
        y_cor = data.y[data.state == user_input].item()
        print("Jo znalaz", user_input, x_cor, y_cor)
        my_turtle.goto(x_cor, y_cor)
        my_turtle.write(user_input)

my_screen.exitonclick()
