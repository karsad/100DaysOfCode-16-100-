from turtle import Turtle

MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("lightgray")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for num in range(len(self.segments) - 1, 0, -1):
            self.segments[num].goto(self.segments[num - 1].xcor(), self.segments[num - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN: self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP: self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT: self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT: self.head.setheading(RIGHT)

    def reset(self):
        for piece in self.segments:
            piece.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

