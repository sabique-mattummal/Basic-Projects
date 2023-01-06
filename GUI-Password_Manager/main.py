#Imports
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# Password Generator from data
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for i in range(randint(5, 10))]
    password_numbers = [choice(numbers) for i in range(randint(5, 10))]
    password_symbols = [choice(symbols) for i in range(randint(5, 10))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    #Conversion of list into string
    
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }
    #Exclusion if any field left blank
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Save Error', message='Incompleted Field')
    else:
      #Read data from existing file
        try:
            with open('data.json', "r") as data_file:
                data = json.load(data_file)
        #If the data.json not created, this will create the file.
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

#Search in the exixting directory

def find_password():
    website = website_entry.get()
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='No website details saved', message='No data for this website been saved')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=f'Transaction Found Successfully for{website}',message=f'Email : {email}\npassword : {password}')
        else:
            messagebox.showinfo(title='Invalid Transaction', message=f'No data found for {website}')
            
#GUI Setup

window = Tk()
window.title("GUI Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)

# Items as per the layout

website_label = Label(text='Website Name :')
website_entry = Entry(width=21)
website_entry.insert(0, 'https://')
website_entry.focus()
search_button = Button(text='Search', width=13,command=find_password)
email_label = Label(text='Email/Username : ')
email_entry = Entry(width=35)
email_entry.insert(0, 'ssmail@gmail.com')
password_label = Label(text='Your Password :')
password_entry = Entry(width=21)
password_generator_button = Button(text='Generate Password', command=generate_password)
add_button = Button(text='Add to Directory', width=36, command=save)

# Grid Arrangement

canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
website_entry.grid(row=1, column=1)
search_button.grid(row=1, column=2)
email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1, columnspan=2)
password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1)
password_generator_button.grid(row=3, column=2)
add_button.grid(row=4, column=0, columnspan=2)

window.mainloop()
