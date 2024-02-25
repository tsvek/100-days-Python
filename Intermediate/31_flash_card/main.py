import csv
import os
import shutil
import tkinter

from random import randint

BG_COLOR = '#B1DDC6'
FROM_LANGUAGE = 'Polish'
TO_LANGUAGE = 'Ukrainian'


current_word = {}
to_learn = []

def get_to_learn():
    """Get words data. Copy data if 'to_learn.csv' isn't exist."""
    global to_learn
    if not os.path.isfile('to_learn.csv'):
        data = os.path.dirname('data.csv')
        learn = os.path.join(data, 'to_learn.csv')
        shutil.copy('data.csv', learn)

    with open('to_learn.csv', 'r', encoding='utf-8') as file:
        to_learn = [row for row in csv.reader(file)]
        print(len(to_learn))

def get_word():
    """Get word and translate from data file"""
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = to_learn[randint(0, len(to_learn))]
    canvas.itemconfig(language, text=FROM_LANGUAGE, fill='black')
    canvas.itemconfig(word, text=current_word[0], fill='black')
    canvas.itemconfig(card_image, image=front_image) 
    flip_timer = window.after(3000, flip_card)

def flip_card():
    """Flip the card""" 
    canvas.itemconfig(language, text=TO_LANGUAGE, fill='white')
    canvas.itemconfig(word, text=current_word[1], fill='white')
    canvas.itemconfig(card_image, image=back_image)

def known_button():
    """Update 'to_learn' list."""
    global to_learn, known
    to_learn.remove(current_word)
    known.append(current_word)
    get_word()

known = []
get_to_learn()

window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BG_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = tkinter.Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
front_image = tkinter.PhotoImage(file="images/card_front.png")
back_image = tkinter.PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=front_image)
language = canvas.create_text(400, 143, text='', fill='black', font=("Arial", 40, 'normal italic'))
word = canvas.create_text(400, 263, text='', fill='black', font=("Arial", 45, 'bold'))
canvas.grid(column=0, row=0, sticky='we',columnspan=2)

unknown_image = tkinter.PhotoImage(file='images/wrong.png')
unknown_button = tkinter.Button(image=unknown_image, highlightthickness=0, command=get_word)
unknown_button.grid(column=0, row=1)
known_image = tkinter.PhotoImage(file='images/right.png')
known_button = tkinter.Button(image=known_image, highlightthickness=0, command=known_button)
known_button.grid(column=1, row=1)

get_word()

window.mainloop()
# Save updated list to file for next time.
with open('to_learn.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(to_learn)