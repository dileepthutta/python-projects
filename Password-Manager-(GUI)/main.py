from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')

#Adding the Padding to the window.
window.config(padx=20,pady=20)

#Creating a window using Canvas.
canvas = Canvas(width=200,height=200)

#Adding an image in the window.
logo = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo)
canvas.pack()







window.mainloop()