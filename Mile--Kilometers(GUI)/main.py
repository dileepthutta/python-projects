from tkinter import *

window = Tk()

window.title('Mile to Km converter')
#Adding padding to the content inside the window.
window.config(padx=20,pady=20)

entry_input = Entry()
entry_input.grid(column=1,row=0)

miles_label = Label(text="Miles",)
miles_label.grid(column=2,row=0)


is_eql_label = Label(text='is equal to',font='10')
is_eql_label.grid(column=0,row=1)

kilo_label = Label(text="0",font='10')
kilo_label.grid(column=1,row=1)

km = Label(text='Km',font='10')
km.grid(column=2,row=1)

button = Button(text="Calculate",font='10')
button.grid(column=1,row=2)
window.mainloop()