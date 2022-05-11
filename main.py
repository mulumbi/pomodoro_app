import math
from tkinter import *
import time
import pandas as pd

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
LONG_WORK_MIN = 30
TOTAL_LAPS = 5
my_timer = None
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
# Initializing the data_structure


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if start["text"] == "Start":
        start.config(text="Pause")
        if reps % 8 == 0:
            # 8th rep is long break
            countdown(long_break_sec)
            timer['text'] = "Long Break"
            timer['fg'] = RED

        elif reps % 2 == 0:
            # even reps are short breaks
            countdown(short_break_sec)
            timer['text'] = "Short Break"
            timer['fg'] = PINK

        else:
            # odd reps are pomodoro 25 min bursts
            countdown(work_sec)
            timer['text'] = "Work Minute"
            timer['fg'] = GREEN



    else:
        start.config(text="Start")
        mark = ''
        work_sessions = math.floor(reps / 2)
        for i in range(work_sessions):
            mark += check_mark
        check["text"] = mark


def reset_timer():
    global my_timer
    global reps
    reps = 0
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer["text"] = "Timer"
    check['text'] = ''




    # create cvs to store last value plus how many laps we've done so far
    # write curr to cvs
    # if button name is "Start" Retrieve current value from csv
    # otherwise, it should keep running, once we finish our time loop: update laps and curr time to either 25, 5 or 30
    # reset button should set value back to whatever starting value we had based off num laps


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(num):
    minute = int(num / 60)
    sec = int(num % 60)
    if sec < 10:
        sec = f'0{sec}'

    canvas.itemconfig(timer_text, text=f"{minute}:{sec}")
    if num > 0:
        global my_timer
        my_timer = window.after(1000, countdown, num - 1)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

img = PhotoImage(file='tomato.png')
timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, 'bold'))
start = Button(text="Start", font=(FONT_NAME, 10), command=start_timer)
reset = Button(text='Reset', font=(FONT_NAME, 10), command=reset_timer)
check_mark = '✔'
break_mark = '🚫'
check = Label(text=' ', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10, 'bold'))
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
timer.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start.grid(column=0, row=2)
reset.grid(column=2, row=2)
check.grid(column=1, row=3)

window.mainloop()
