from turtle import Turtle, Screen
import random

colors = [
    "aqua", "aquamarine", "beige", "black", "blanchedalmond",
    "blue", "blueviolet", "brown", "burlywood", "cadetblue",
    "chartreuse", "chocolate", "coral", "cornflowerblue", "crimson",
    "cyan", "darkblue", "darkcyan", "darkgoldenrod", "darkgray",
    "darkgreen", "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange",
    "darkorchid", "darkred"
]



my_turtle = Turtle()
my_screen = Screen()
my_screen.colormode(255)

my_turtle.shape("turtle")
my_turtle.color("aquamarine")
my_turtle.shapesize(2, 2)
my_turtle.pen(pensize=10)
my_turtle.speed(20)
# for i in range(1,10):
#     my_turtle.forward(5)
#     my_turtle.penup()
#     my_turtle.forward(5)
#     my_turtle.pendown()


# for x in range(3, 9):
#     angle = 360 / x
#     my_turtle.pencolor(str(random.choice(colors)))
#     for i in range(1, (x+1) ):
#         my_turtle.forward(150)
#         my_turtle.right(angle)

# direction = [0, 90, 180, 270]
# for i in range(1, 550):
#     color = (random.randint(1,255), random.randint(1,255), random.randint(1,255))
#     my_turtle.left(random.choice(direction))
#     my_turtle.pencolor(color)
#     my_turtle.forward(30)

steps = 150
my_turtle.width(2)
for step in range(steps):
    angle = 360 / steps
    color = (random.randint(1,255), random.randint(1,255), random.randint(1,255))
    my_turtle.pencolor(color)
    my_turtle.circle(200)
    my_turtle.left(angle)



my_screen.exitonclick()