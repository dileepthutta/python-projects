from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
# Add Padding to the image.
window.config(padx=100,pady=50,bg=YELLOW,)

#Label for the Timer.
head_label = Label(text='Timer',fg=GREEN,highlightthickness=0,bg=YELLOW,font=(FONT_NAME,50,'bold'))
head_label.grid(column=1,row=0)

canvas = Canvas(width=205,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
#It adds an image into the window.
canvas.create_image(103,112,image=tomato_img)
# Adds a text into the tomato
canvas.create_text(103,130,text="00:00",fill='White',font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)
#Adding buttons on the image.
start_button = Button(text='Start',fg='black',bg='White',highlightthickness=0)
start_button.grid(column=0,row=2)

#Reset Buttton.
reset_btn = Button(text='Reset',fg='black',bg='White',highlightthickness=0)
reset_btn.grid(column=2,row=2)

#Tick Symbol.
tick_label = Label(text="✔",bg=YELLOW,fg=GREEN,font=(10,))
tick_label.grid(column=1,row=3)


window.mainloop()