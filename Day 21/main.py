from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
my_screen = Screen()
snake = Snake()
my_food = Food()
my_scoreboard = Scoreboard()

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
    time.sleep(0.15)
    snake.move()

    if snake.head.distance(my_food) < 20:
        my_food.refresh()
        my_scoreboard.add_point()
        snake.extend()

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        is_game_on = False
        my_scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            my_scoreboard.game_over()

my_screen.exitonclick()
