from tkinter import *
import csv
import random
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
# ----------------------- Functionality Setup -----------------------
def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="French")
    canvas.itemconfig(card_word,text=current_card["French"])



# ----------------------- Data Setup -----------------------
data = pd.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

# ----------------------- UI Setup -----------------------
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50,background=BACKGROUND_COLOR)


canvas = Canvas(width=800,height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=card_front_img)
card_title = canvas.create_text(400,153,text="",font=('Arial',40,"italic"))
card_word = canvas.create_text(400,263,text="",font=('Arial',40,'bold'))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)



# Buttons

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img,highlightthickness=0,command=next_card)
right_button.grid(row=1,column=1)


# To call the function because to refresh the page with the random word.
next_card()
window.mainloop()