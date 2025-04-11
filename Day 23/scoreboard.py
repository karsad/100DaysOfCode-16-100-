from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-290, y=270)
        self.color("gray")
        self.display_level()

    def display_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def display_game_over(self):
        self.goto(0, -280)
        self.write("GAME OVER", align="center", font=FONT)