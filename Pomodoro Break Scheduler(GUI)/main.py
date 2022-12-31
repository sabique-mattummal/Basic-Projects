# imports

from tkinter import *
import math

# Constants
CANVAS_BACKGROUND = '#FF884B'
RED = "#e7305b"
GREEN = "#9bdeac"
FONT_NAME = "Arial Black"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# Timing Functions
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# Start timer (a) commence the reps count, (b) manage timing as per the breaks and works
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Extended Break Time", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break Time", fg='pink')
    else:
        count_down(work_sec)
        title_label.config(text="Work Time", fg='white')


# Commence countdown using window after function

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps / 2)
        for i in range(work_sessions):
            marks += '🕺🏼'
        check_marks.config(text=marks)


# Screen Layout
window = Tk()
window.title("Pmodoro Break Scheduler")
window.config(padx=100, pady=50, bg=CANVAS_BACKGROUND)

title_label = Label(text="Timer", fg=GREEN, bg=CANVAS_BACKGROUND, font=(FONT_NAME, 24))
canvas = Canvas(width=200, height=224, bg=CANVAS_BACKGROUND, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 22, 'bold'))
start_button = Button(text='Start', highlightthickness=0, command=start_timer, bg='#FF884B', height=2, width=20)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer, bg='#FF884B', height=2, width=20)
check_marks = Label(fg=GREEN, bg=CANVAS_BACKGROUND)

# Screen grid arrangement
title_label.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)
check_marks.grid(column=1, row=3)

window.mainloop()
