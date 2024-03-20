from turtle import Screen, Turtle
from player import Player
from car_manager import Car
from score import Score
import time


screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("white")
screen.title("Crossing Turtle")
screen.tracer(0)


player = Player()
car_manager = Car()
score = Score()

screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on=True 
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    for i in car_manager.cars:
        if i.distance(player)<20:
            game_is_on = False
            score.game_over()

    if player.finish():
        player.goto_start()
        car_manager.level_up()
        score.increase_level()


screen.exitonclick()