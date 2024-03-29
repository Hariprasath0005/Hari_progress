from turtle import Screen, Turtle
import time
from snake import Snake
from food import food
from Score import score
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)



snake = Snake()
food = food()
score = score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on=True 
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.add_score()

        
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score.reset()
        snake.reset()
    
    for i in snake.segment:
        if i == snake.head:
            pass
        elif snake.head.distance(i)<10:
            score.reset()
            snake.reset()
            


screen.exitonclick()
