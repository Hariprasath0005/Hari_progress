import turtle as t
from turtle import Screen
tim = t.Turtle()
tim.shape("turtle")
tim.color("#32CD32", "#FFD700"	)
def rectangle():
    for i in range(4):
        tim.forward(100)
        tim.left(90)
rectangle()
screen = Screen()
screen.exitonclick()