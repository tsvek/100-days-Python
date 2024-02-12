import tkinter

from random import choice

# TODO: Password generator
def pass_gen():
    password_entry.delete(0, 'end')
    all_in_one = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
                  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
                  '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

    password = ''.join([choice(all_in_one) for _ in range(20)])
    password_entry.insert(0, string=password)

# TODO: Save password
def pass_save():
    pass
# TODO: UI setup
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
image = tkinter.PhotoImage(file=r'Intermediate\29_password_manager\logo.png')
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