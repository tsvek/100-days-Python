import csv
import tkinter

from random import choice
from time import sleep

BG_COLOR = '#B1DDC6'
FROM_LANGUAGE = 'Polish'
TO_LANGUAGE = 'Ukrainian'

def get_word():
    # Get word and translate from data file
    with open('data.csv', 'r', encoding='utf-8') as file:
        data = [row for row in csv.reader(file)]
        return choice(data[1:])

def flip(word_translate):
    # TODO: Flip the card
    image = tkinter.PhotoImage(file="images/card_back.png")
    canvas.itemconfig(card_image, image=image)
    canvas.itemconfig(language, text=TO_LANGUAGE)
    canvas.itemconfig(word, text=word_translate)

# TODO: Action buttons

window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BG_COLOR)

word, translate = get_word()
known = []
unknown = []

canvas = tkinter.Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
image = tkinter.PhotoImage(file="images/card_front.png")
card_image = canvas.create_image(400, 263, image=image)
language = canvas.create_text(400, 143, text=FROM_LANGUAGE, fill='black', font=("Arial", 40, 'normal italic'))
word = canvas.create_text(400, 263, text=word, fill='black', font=("Arial", 45, 'bold'))
canvas.grid(column=0, row=0, sticky='we',columnspan=2)

#print(word, translate)
wrong_image = tkinter.PhotoImage(file='images/wrong.png')
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)
right_image = tkinter.PhotoImage(file='images/right.png')
right_button = tkinter.Button(image=right_image, highlightthickness=0)
right_button.grid(column=1, row=1)


flip(translate)

window.mainloop()