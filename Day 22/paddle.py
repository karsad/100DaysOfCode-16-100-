from turtle import Turtle, Screen
from board import Board

class Paddle(Turtle):
    def __init__(self, player, board):

        super().__init__("square")
        self.board = board
        self.speed("fastest")
        self.color("white")
        self.shapesize(stretch_len=5)
        self.penup()
        self.left(90)
        if player: self.goto(x= ((board.my_screen.window_width()/2)-16) * (-1), y=0)
        else: self.goto(x= ((board.my_screen.window_width()/2)-24), y=0)

    def up(self):
        if self.position()[1] < 240:
            self.goto(x=self.position()[0], y=self.position()[1] + 10)
            self.board.my_screen.update()

    def down(self):
        if self.position()[1] > -230:
            self.goto(x=self.position()[0], y=self.position()[1] - 10)
            self.board.my_screen.update()
