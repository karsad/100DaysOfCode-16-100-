from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        try:
            with open("highscore.txt", "r") as file:
                self.highscore = int(file.read())
                print("Readed from file:", self.highscore)
        except FileNotFoundError:
            self.highscore = 0
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
        self.write(arg=f"Score: {self.score}, high score: {self.highscore}", align="center", font=("Arial", 20, "bold"))

    def reset(self):

        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", "w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align="center", font=("Arial", 20, "bold"))
