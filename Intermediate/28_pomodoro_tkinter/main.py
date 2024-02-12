import tkinter

PINK = '#e2979c'
RED = '#e7005b'
GREEN = '#9bdeac'
YELLOW = '#f7f5dd'
FONT_NAME = 'Courier'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# Timer reset
def reset_timer():
    window.after_cancel(timer)
    status.config(text='Timer', fg=GREEN)
    check_marks.config(text='')
    canvas.itemconfig(timer_text, text="00:00")

# Timer mechanism
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    if reps == 7:
        seconds = long_sec
        status.config(text='Long Break', fg=RED)
        reps = 1
        reset_timer()
    elif reps % 2 == 0:
        seconds = work_sec
        status.config(text='Work', fg=GREEN)
    else:
        check_marks.config(text='✔'*(int(reps/2)))
        seconds = short_sec
        status.config(text='Break', fg=PINK)
    count_down(seconds)
    reps += 1

# Countdown mechanism
def count_down(count):
    minute = count // 60
    second = count % 60
    canvas.itemconfig(timer_text, text=f"{minute:02d}:{second:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()

# UI setup
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=50, pady=25, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = tkinter.PhotoImage(file=r"Intermediate\28_pomodoro_tkinter\tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

status = tkinter.Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, 'bold'))
status.grid(column=1, row=0)

check_marks = tkinter.Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

start = tkinter.Button(text='Start', command=start_timer)
start.grid(column=0, row=2)

reset = tkinter.Button(text='Reset', command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()