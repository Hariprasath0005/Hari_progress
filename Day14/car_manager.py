from turtle import Turtle
import random
COLORS = ["red","blue","green","yellow","purple","orange"]
STARTING_MOVE_DISTANCE =5
MOVE_INCREMENT = 2

class Car:

    def __init__(self):
        #super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-150,200)
            new_car.goto(350,random_y)
            self.cars.append(new_car)

    def move_car(self):
        for i in self.cars:
            i.backward(self.car_speed)

    def level_up(self):
        self.car_speed +=MOVE_INCREMENT

