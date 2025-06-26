import turtle
from turtle import Turtle

import pandas as pd
from pandas import read_csv

screen = turtle.Screen()
screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


data = read_csv('50_states.csv')
all_states = data.state.to_list()

guessed_state = []

while len(guessed_state) < 50:
    # To Create a pop-up box and User ask user-input.
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",
                                    prompt="What's another state's name? ").title()

    #If the user type exit then the game terminates and the missing data is saved into a file.
    if answer_state == "Exit":
        missing_data = [state for state in all_states if state not in guessed_state]
        final_data = pd.DataFrame(missing_data)
        final_data.to_csv('missing_data.csv')
        break


    #Check's if the user-state is correct || not.
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)
screen.exitonclick()


#Function to get the co-ordinate of x,y values of  the image onclick.
# def get_mouse_click_coor(x , y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()