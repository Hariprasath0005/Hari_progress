import turtle as t
from turtle import Screen
import random
tim = t.Turtle()
tim.shape("turtle")

t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

direction = [0,90,180,270]
tim.pensize(10)
tim.speed(0)
for i in range(200):
    
    tim.color(random_color())
    tim.forward(20)
    tim.setheading(random.choice(direction))


screen = Screen()
screen.exitonclick()


