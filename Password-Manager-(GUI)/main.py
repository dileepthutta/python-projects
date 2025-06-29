from tkinter import *
# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    #Retrive the Data from Entry Field.
    website_data = website_entry.get()
    email_data   = email_entry.get()
    password_data = password_entry.get()

    #Creates and add the data into the File.
    with open("data.txt",'a') as file:
        file.write(f"{website_data}\t|{email_data}\t|{password_data}")
        file.write('\n')
    # Deletes the password in the window when you added into the File.
    website_entry.delete(0,'end')
    # email_entry.delete(0,'end')
    password_entry.delete(0,'end')
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas for logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")  # Make sure logo.png is in the same folder
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Website Label and Entry
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# Email/Username Label and Entry
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)

#To Set the default entry on the Email Entry Field.
email_entry.insert(0,"dileep@gmail.com")

# Password Label, Entry and Generate Button
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21,show='*')
password_entry.grid(column=1, row=3)
gen_pass_btn = Button(text="Generate Password")
gen_pass_btn.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", width=36,command=add)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()