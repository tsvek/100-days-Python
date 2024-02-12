import tkinter


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=220, height=220)
image = tkinter.PhotoImage(file=r'Intermediate\29_password_manager\logo.png')
canvas.create_image(110, 110, image=image)
canvas.grid(column=0, row=0)

window.mainloop()