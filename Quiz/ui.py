from tkinter import *

from pandas.io.formats.info import frame_see_also_sub

THEME_COLOR = "#375362"


class QuizzInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        # Creating a Score Label.
        self.score_label = Label(text="Score",fg='White',bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        # Creating a white Background with height and width.
        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(150,
            125,
            text="Some Question text",
            fill=THEME_COLOR,
            font=('Arial',20,'italic')
            )
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        # True_image
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image,highlightthickness=0)
        self.true_button.grid(row=2,column=0)

        #False_image.
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image)
        self.false_button.grid(row=2,column=1)


        self.window.mainloop()