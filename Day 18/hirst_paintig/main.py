import colorgram
import random
from turtle import Turtle, Screen

my_turtle = Turtle()
my_screen = Screen()
my_screen.colormode(255)

my_turtle.shape("arrow")
my_turtle.penup()

colors = colorgram.extract('image.jpg', 10)
dots_count = 15
screen_w = my_screen.window_width()
screen_h = my_screen.window_height()
spacing_w = screen_w * 2 / 3 / 2 / dots_count
spacing_h = screen_h * 2 / 3 / 2 / dots_count
# my_turtle.teleport(-(screen_w/2)+3*spacing_w, -(screen_h/2)+3*spacing_h)

for row in range(dots_count):
    my_turtle.teleport(-(screen_w / 2) + 3 * spacing_w, -(screen_h / 2) + (row+1) * 2.5 * spacing_h)
    for col in range(dots_count):
        color_rgb = random.choice(colors).rgb
        my_turtle.dot(spacing_w, (color_rgb.r, color_rgb.g, color_rgb.b))
        my_turtle.forward(spacing_w*2)


my_screen.exitonclick()