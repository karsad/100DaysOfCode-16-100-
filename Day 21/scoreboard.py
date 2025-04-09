from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def add_point(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 20, "bold"))

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align="center", font=("Arial", 20, "bold"))
