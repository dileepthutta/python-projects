from random import choice,randint,shuffle
import random
from tkinter import *
from tkinter import messagebox
from webbrowser import open_new

import pyperclip
import json
# ---------------------------- Generate PASSWORD ------------------------------- #
#Password Generator
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    letter_list = [choice(letters) for _ in range(random.randint(8,10))]
    symbol_list = [choice(symbols) for _ in range(random.randint(2,4))]
    number_list = [choice(numbers)for _ in  range(random.randint(2,4))]

    password_list = letter_list + number_list + symbol_list
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    #Retrive the Data from Entry Field.
    website_data = website_entry.get()
    email_data   = email_entry.get()
    password_data = password_entry.get()

    new_data = {
        website_data:{
            "Email":email_data,
            "Password":password_data
        }
    }

    #Check and return a popup button if any of the fields are Empty while saving the data.
    if len(website_data)==0 or len(email_data)==0 or len(password_data)==0:
        valid_or_not = messagebox.showinfo(title='Something went wrong!',message='Please don`t leave any fields empty!')

    #Asks the user to save the data or not in the datafile.
    else:
        is_ok = messagebox.askokcancel(title=website_data,message=f"These are the details entered: \nEmail: {email_data}"
                                       f"\nPassword: {password_data} \nIs it ok to save?")
        if is_ok:
            try:
                with open('data.json','r')as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                #If the file doesn't exist.
                with open('data.json','w') as data_file:
                    json.dump(new_data,data_file,indent=4)
            else:
                #updaing old data with new data
                data.update(new_data)

                with open('data.json','w') as data_file:
                    #Saving the updated data
                    json.dump(data,data_file,indent=4)

# Deletes the password in the window when you added into the File.
            website_entry.delete(0,'end')
            password_entry.delete(0,'end')


def search():
    website_data = website_entry.get()
    try:
        with open('data.json','r') as file_data:
            data = json.load(file_data)
            display = messagebox.showinfo(title=website_data,message=f'Email : {data[website_data]['Email']}\nPassword : {data[website_data]['Password']}')
    # If file doesn't Exist or if user enters  invalid details to search.
    except FileNotFoundError and KeyError:
        error = messagebox.showerror(title='Error',message='No Data File Found.')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20,background="black")

# Canvas for logo
canvas = Canvas(width=200, height=200, highlightthickness=0,background="black")
logo = PhotoImage(file="logo.png")  # Make sure logo.png is in the same folder
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Website Label and Entry, Search Button
website_label = Label(text="Website:",fg="white",bg="black")
website_label.grid(column=0, row=1)
website_entry = Entry(width=29)
website_entry.grid(column=1, row=1)
website_entry.focus()
search_button = Button(text='Search',width=14,background="blue",command=search)
search_button.grid(column=2,row=1)

# Email/Username Label and Entry
email_label = Label(text="Email/Username:",fg="white",bg="black")
email_label.grid(column=0, row=2)
email_entry = Entry(width=29)
email_entry.grid(column=1, row=2)

#To Set the default entry on the Email Entry Field.
# email_entry.insert(0,"Your Email field to set a default email.")

# Password Label, Entry and Generate Button
password_label = Label(text="Password:",fg="white",bg="black")
password_label.grid(column=0, row=3)
password_entry = Entry(width=29)
password_entry.grid(column=1, row=3)
gen_pass_btn = Button(text="Generate Password",command=generate_password,bg="#4CAF50")
gen_pass_btn.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add Data", width=10,command=add,fg="white",bg="red")
add_button.grid(column=1, row=4)

window.mainloop()