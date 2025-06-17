from turtle import Turtle,Screen
import time 

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game ")
screen.tracer(0) # Untill we use (update) we screen will be blank.

#Creating a Snake body.
starting_position = [(0,0),(-20,0),(-40,0)]

segments = []
for position in starting_position:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup()    #Avoid to draw on Screen.
    new_segment.goto(position)
    segments.append(new_segment)

#Move the snake.
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1) #Adds a 0.1 sec delay for each pieace.
    
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x,new_y)
    segments[0].forward(20)
    segments[0].left(90)


screen.exitonclick()