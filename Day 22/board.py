from turtle import Turtle, Screen
LINE_PIECES = 15
class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.my_text = Turtle()
        self.my_screen = Screen()
        self.my_screen.setup(width=800, height=600)
        self.my_screen.title("PingPong Game")
        self.my_screen.bgcolor("black")
        self.my_screen.tracer(0)
        self.draw_middle_line()
        self.display_press_to_start()
        self.my_screen.update()


    def draw_middle_line(self):
        self.width(4)
        self.color("white")
        self.left(90)
        self.speed("fastest")
        spacing = self.my_screen.window_height() / 2 / (LINE_PIECES)
        offset = -10 - spacing + 4
        self.penup()
        self.goto(x=0, y=0-(LINE_PIECES*spacing)+offset)
        print("Draw middle", self.position())
        while self.position()[1] < 300:
            self.forward(spacing)
            self.penup()
            self.forward(spacing)
            self.pendown()
        print("END")

    def display_press_to_start(self):
        # self.my_screen.listen()
        # self.my_screen.onkey(key="spacebar", func=func)
        # my_text.hideturtle()
        print("trigger")
        self.my_text.color("gray")
        self.my_text.hideturtle()
        self.my_text.write(arg="Press [SPACE] to start", align="center", font=("arial", 50, "bold"))


    def exit_on_click(self):
        self.my_screen.exitonclick()
