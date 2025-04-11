import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

my_scoreboard = Scoreboard()

my_player = Player()
screen.onkey(my_player.move, "space")

car_manager = CarManager()

game_is_on = True
while game_is_on:

    # Check if lvl finished
    if my_player.is_at_finishline():
        my_player.reset_position()
        my_scoreboard.level += 1
        my_scoreboard.display_level()
        car_manager.change_speed()
        car_manager.reset_cars()
    car_manager.move()
    car_manager.generate_traffic()
    if car_manager.is_target_hit(my_player): break
    time.sleep(0.1)
    screen.update()

my_scoreboard.display_game_over()
screen.update()
screen.exitonclick()
