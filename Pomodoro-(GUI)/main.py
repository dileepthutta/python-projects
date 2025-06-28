import math
from tkinter import *

from matplotlib.pyplot import title

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text,text="00:00")
    head_label.config(text="Timer")
    tick_label.config(text="")
    global reps
    reps =0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global  reps
    reps+=1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8==0:
        count_down(long_break_sec)
        head_label.config(text="Break",fg=RED)
    elif reps % 2 ==0:
        count_down(short_break_sec)
        head_label.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        head_label.config(text="Work",fg=PINK)

    # count_down(1 * 60) # It represents the Number of Seconds.
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

        count_min = math.floor(count / 60) # To calculate minutes.
        count_sec = count % 60             # To calculate second.
        if count_sec < 10:
            count_sec = f"0{count_sec}"

        canvas.itemconfig(canvas_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            # .after() Schedule a function to run after a specified time delay in millisecond
            global timer
            timer = window.after(1000,count_down , count-1)
        else:
            start_timer()
            marks = ""
            work_sessions = math.floor(reps/2)
            for _ in range(work_sessions):
                marks += "✔"
            tick_label.config(text=marks)

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
canvas_text = canvas.create_text(103,130,text="00:00",fill='White',font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

#Adding buttons on the image.
start_button = Button(text='Start',fg='black',bg='White',highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

#Reset Button.
reset_btn = Button(text='Reset',fg='black',bg='White',highlightthickness=0,command=reset_timer)
reset_btn.grid(column=2,row=2)

#check Symbol.
tick_label = Label(text="",bg=YELLOW,fg=GREEN,font=(10,))
tick_label.grid(column=1,row=3)


window.mainloop()