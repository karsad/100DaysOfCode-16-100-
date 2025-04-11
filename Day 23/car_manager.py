from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2
MAX_CARS = 15

class CarManager():
    def __init__(self):
        self.current_speed = STARTING_MOVE_DISTANCE
        self.cars = []

        for car in range(MAX_CARS):
            self.add_car()

    def add_car(self):
        new_car = Turtle("square")
        new_car.left(180)
        new_car.shapesize(stretch_len=2)
        new_car.color("black", random.choice(COLORS))
        new_car.penup()
        x_pos = random.randint(-280, 300)
        # x_pos = 0
        y_pos = self.find_random_y_pos(x_pos)
        new_car.goto(x_pos, y_pos)
        self.cars.append(new_car)


    def move(self):
        for car in self.cars:
            car.forward(self.current_speed)

    def generate_traffic(self):
        for car in self.cars:
            if car.xcor() < -320:
                car.color("black", random.choice(COLORS))
                x_pos = 320
                y_pos = self.find_random_y_pos(x_pos)
                car.goto(x_pos,y_pos)

    def is_target_hit(self, target):
        is_hit = False
        for car in self.cars:
            car_x = car.xcor()
            car_y = car.ycor()
            if car.distance(target) < 28:
                if car_y-20  <= target.ycor() <= car_y + 20:
                    is_hit = True
                    break
        return is_hit

    def find_random_y_pos(self, x_pos):
        position_not_found = True
        while position_not_found:
            y_pos = random.randint(-12, 12) * 20
            if not self.cars: break
            for car in self.cars:
                print(car.ycor(), y_pos)
                if car.ycor() == y_pos:
                    if -50 < car.xcor() - x_pos < 50:
                        position_not_found = True
                        break
                else: position_not_found = False
        return y_pos

    def reset_cars(self):
        for car in self.cars:
            car.color(random.choice(COLORS))
            x_pos = random.randint(-280, 300)
            y_pos = self.find_random_y_pos(x_pos)
            car.goto(x_pos, y_pos)

    def change_speed(self):
        self.current_speed += MOVE_INCREMENT

