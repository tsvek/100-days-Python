import csv
import os
import tkinter

from random import choice
from tkinter import messagebox

# Password generator
def pass_gen():
    password_entry.delete(0, 'end')
    all_in_one = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
                  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
                  '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

    password = ''.join([choice(all_in_one) for _ in range(20)])
    password_entry.insert(0, string=password)

# Save password
def pass_save():
    for_save = {
        'Website': website_entry.get(),
        'Login': login_entry.get(), 
        'Password': password_entry.get()
    }
    
    if '' not in for_save.values():
        message = '\n'.join([f'{key}:{value}' for key, value in for_save.items()])
        checking = messagebox.askyesno(title='Is everything correct?', message=message)
        
        if checking:
            mode = 'a+' if os.path.isfile('pass_manager.csv') else 'w'
            with open('pass_manager.csv', mode=mode, encoding="utf-8", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=for_save.keys(), delimiter=';')
                if mode == 'w':
                    writer.writeheader()
                writer.writerow(for_save)
            messagebox.showinfo(title="Success!", message="Your password has been saved.")
    else:
        messagebox.showinfo(title="Opps", message='Please fill in all fields!')
    website_entry.delete(0, 'end')
    login_entry.delete(0, 'end')
    password_entry.delete(0, 'end')

# UI setup
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
image = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website = tkinter.Label(text='Website:')
website.grid(column=0, row=1)

website_entry = tkinter.Entry()
website_entry.grid(column=1, row=1, sticky='we',columnspan=2)

login = tkinter.Label(text='Email/Username:')
login.grid(column=0, row=2)
login_entry = tkinter.Entry()
login_entry.grid(column=1, row=2, sticky='we',columnspan=2)

password = tkinter.Label(text='Password:')
password.grid(column=0, row=3)
password_entry = tkinter.Entry()
password_entry.grid(column=1, row=3, sticky='we',)

generate = tkinter.Button(text="Generate Password", command=pass_gen)
generate.grid(column=2, row=3)

add = tkinter.Button(text="Add", command=pass_save)
add.grid(column=1, row=4, sticky='we', columnspan=2)

window.mainloop()