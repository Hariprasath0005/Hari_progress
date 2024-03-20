import turtle as t
from turtle import Screen
import random
tim = t.Turtle()
tim.shape("turtle")
#tim.color("#32CD32", "#FFD700"	)

colors = ["light steel blue","forest green","firebrick","blanched almond","medium slate blue","magenta"]
def shape(size):
    for i in range(size):
        tim.right(360/size)
        tim.forward(100)
for i in range(3,10):
    tim.color(random.choice(colors))
    shape(i)

screen = Screen()
screen.exitonclick()