# - class Scoreboard
# - class Screenboard
# - class Ball
# - class player
#   - class enemy

from board import Board
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

is_game_on = True

my_screen = Board()
my_paddle = Paddle(player=True, board=my_screen)
pc_paddle = Paddle(player=False, board=my_screen)
my_ball = Ball()
my_scoreboard = Scoreboard()

my_screen.my_screen.listen()
my_screen.my_screen.onkey(my_paddle.up, "Up")
my_screen.my_screen.onkey(my_paddle.down, "Down")
my_screen.my_screen.onkey(pc_paddle.up, "w")
my_screen.my_screen.onkey(pc_paddle.down, "s")



while is_game_on:
    my_ball.move(my_paddle, pc_paddle)
    if my_ball.x_pos > 375:
        my_ball.x_motion = False
        my_ball.reset_ball()
        my_scoreboard.l_score += 1
        my_scoreboard.display_score()
    elif my_ball.x_pos < -375:
        my_ball.x_motion = True
        my_ball.reset_ball()
        my_scoreboard.r_score += 1
        my_scoreboard.display_score()
    my_screen.my_screen.update()
my_screen.exit_on_click()