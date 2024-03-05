import requests
import tkinter

import key as k

KEY = k.key
DEEPL = k.deepl
new = "Click the button and get fun =)"

def get_fact():
    """Get random fact."""
    global new
    url = "https://api.api-ninjas.com/v1/facts"
    headers = {
        "X-Api-Key": KEY,
    }

    response = requests.get(url=url, headers=headers)
    if response.status_code == requests.codes.ok:
        new = response.json()[0]['fact']
        canvas.itemconfig(fact_text, text=new)
    else:
        print(f"Something went wrong: {response.status_code, response.text}")

def get_translate() -> str:
    """Translates fact into Ukrainian(special for my wife=))."""
    global new
    url = "http://api-free.deepl.com/v2/translate"
    headers = {
        'Authorization': f'DeepL-Auth-Key {DEEPL}', 
        'Content-Type': 'application/json'
    }
    params = {
        'text': new,
        'target_lang': "UK"
    }
    response = requests.get(url=url, headers=headers, params=params)
    new = response.json()['translations'][0]['text']
    canvas.itemconfig(fact_text, text=new)

window = tkinter.Tk()
window.title("Interesting fact =)")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=300, height=150)
fact_text = canvas.create_text(150, 57, text=new, width=200, font=('Arial', 10, 'bold'))
canvas.grid(column=0, row=0)

new_fact_button = tkinter.Button(text="New fact", command=get_fact)
new_fact_button.grid(column=0, row=1)

translate_button = tkinter.Button(text='Дуже цікаво але ніхера не зрозуміло', command=get_translate)
translate_button.grid(column=0, row=2)

window.mainloop()