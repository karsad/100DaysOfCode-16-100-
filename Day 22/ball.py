from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.x_motion = True
        self.y_motion = True
        super().__init__("circle")
        self.penup()
        self.color("white")
        self.speed = 2
        self.org_speed = self.speed

    def reset_ball(self):
        self.speed = self.org_speed
        self.x_pos = 0
        self.y_pos = 0

    def move(self, paddle1, paddle2):
        if self.x_motion:
            self.x_pos += self.speed
        else: self.x_pos -= self.speed

        if self.y_motion:
            self.y_pos += self.speed
        else: self.y_pos -= self.speed

        if self.y_pos > 290: self.y_motion = False
        elif self.y_pos < -285: self.y_motion = True

        if self.distance(paddle2) < 52:
            if self.x_pos > 360:
                self.x_motion = False
                self.speed *= 1.1
        elif self.distance(paddle1) < 52:
            if self.x_pos < -360:
                self.x_motion = True
                self.speed *= 1.1

        self.goto(x=self.x_pos, y=self.y_pos)
