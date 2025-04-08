from turtle import Turtle, Screen
from snake import Snake
import time
my_screen = Screen()
snake = Snake()

my_screen.setup(width=600, height=600)
my_screen.bgcolor("gray")
my_screen.title("Snake Game")
my_screen.tracer(0)
my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")





is_game_on = True
while is_game_on:
    my_screen.update()
    time.sleep(0.2)
    snake.move()


my_screen.exitonclick()
