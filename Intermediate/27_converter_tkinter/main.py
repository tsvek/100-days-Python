import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(pady=50, padx=50)

is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

miles_entry = tkinter.Entry(width=10)
miles_entry.grid(column=1, row=0)

miles = tkinter.Label(text='Miles')
miles.grid(column=2, row=0)

km = tkinter.Label(text="Km")
km.grid(column=2, row=1)

answer = tkinter.Label(text="0")
answer.grid(column=1, row=1)

def convert():
    miles = miles_entry.get()
    try:
        km = round(float(miles) * 1.609344, 2)
        answer.config(text=km)
    except:
        print("Wrong enter format")

convert_button = tkinter.Button(text="Calculate", command=convert)
convert_button.grid(column=1, row=2)

window.mainloop()