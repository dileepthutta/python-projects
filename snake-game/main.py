from turtle import Turtle,Screen
from snake import Snake
import time 

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game ")
screen.tracer(0) # Untill we use (update) we screen will be blank.

snake = Snake()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1) #Adds a 0.1 sec delay for each pieace.
    
    snake.move()
screen.exitonclick()