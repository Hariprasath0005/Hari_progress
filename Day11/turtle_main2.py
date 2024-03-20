import turtle as t
from turtle import Screen

tim = t.Turtle()
tim.shape("turtle")
#tim.color("#32CD32", "#FFD700"	)

for i in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


screen = Screen()
screen.exitonclick()