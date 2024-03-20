import turtle as t
from turtle import Turtle, Screen
import random
tim = Turtle()

t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

tim.pensize(1)
tim.speed(100)

def spirograpth(size):
    for i in range(int(360/size)):
        tim.color(random_color())
        tim.circle(80)
        tim.setheading(tim.heading()+size)
spirograpth(5)
screen = Screen()
screen.exitonclick()