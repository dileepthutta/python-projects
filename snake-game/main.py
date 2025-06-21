from turtle import Turtle,Screen
from snake import Snake
import time 
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game ")
screen.tracer(0) # Untill we use (update) we screen will be blank.

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1) #Adds a 0.1 sec delay for each pieace.
    snake.move()

    #To Detect collisoin with food. 
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #To Detect colloison with wall
    if snake.head.xcor() >295 or snake.head.xcor() < -295 or snake.head.ycor() >295 or snake.head.ycor() < -295:
        game_on = False
        scoreboard.game_over()
    # Do To detect collision with Tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on =False
            scoreboard.game_over()
screen.exitonclick()
