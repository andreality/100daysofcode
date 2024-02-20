from tkinter import *

reps = 0
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
FONT_TUPLE = (FONT_NAME, 35, "bold")

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        count_down(work_sec)
        title_label.config(text="Work!")
    elif reps % 4 == 0:
        title_label.config(text="Break!")
        count_down(long_break_sec)
    else:
        title_label.config(text="Break!")
        count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def format_time(count):
    minutes = count // 60
    if minutes < 10:
        minutes = "0" + str(minutes)
    seconds = count % 60
    if seconds < 10:
        seconds = "0" + str(seconds)
    return f"{minutes}:{seconds}"


def count_down(count):
    if count == 0:
        start_timer()
    canvas.itemconfig(timer_text, text=format_time(count))
    window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=00, pady=50, bg=YELLOW)


title_label = Label(text="Timer", fg=GREEN, font=FONT_TUPLE, background=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=FONT_TUPLE)
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = Label(text="✔", fg=GREEN, bg=YELLOW, font=FONT_TUPLE)
check_marks.grid(column=1, row=3)

window.mainloop()
