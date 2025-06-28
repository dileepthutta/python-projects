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
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=205,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
#It adds an image into the window.
canvas.create_image(103,112,image=tomato_img)
# Adds a text into the tomato
canvas.create_text(103,130,text="00:00",fill='White',font=(FONT_NAME,35,"bold"))
canvas.pack()




window.mainloop()