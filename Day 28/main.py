from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
CHECK_MARK = "✔"
my_timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    my_window.after_cancel(my_timer)
    title.config(text="Timer", fg=GREEN)
    my_canvas.itemconfig(timer, text="00:00")
    check_mark['text'] = ""

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 2 == 0 and reps < 8:
        check_mark['text'] += (CHECK_MARK + " ")
        title.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN)
    elif reps % 2 == 1 and reps < 8:
        title.config(text="Work", fg=GREEN)
        count_down(WORK_MIN )
    elif reps == 8:
        check_mark['text'] += CHECK_MARK
        title.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN)
    else:
        check_mark['text'] = ""
        title.config(text="Timer", fg=GREEN)
        reps = 0
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    my_canvas.itemconfig(timer, text=f"{count_min:02d}:{count_sec:02d}")
    if count>0:
        global my_timer
        my_timer = my_window.after(100, count_down, count - 1)
    else: start_timer()

# ---------------------------- UI SETUP ------------------------------- #
my_window = Tk()
my_window.title("Pomodoro work balancer")
my_window.config(padx=100, pady=40, bg=YELLOW)

title = Label()
title.config(text="Timer", font=(FONT_NAME, 60, "bold"), bg=YELLOW, highlightthickness=0, fg=GREEN)
title.grid(column=2, row=1)

start_btn = Button()
start_btn.config(text="Start", font=(FONT_NAME, 16), highlightbackground=YELLOW, command=start_timer)
start_btn.grid(column=1, row=3)

reset_btn = Button()
reset_btn.config(text="Reset", font=(FONT_NAME, 16), highlightbackground=YELLOW, command=reset_timer)
reset_btn.grid(column=3, row=3)

check_mark = Label()
check_mark.config(text="", font=(FONT_NAME, 30, "bold"), bg=YELLOW, highlightthickness=0, fg=GREEN)
check_mark.grid(column=2, row=4)

my_canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
my_canvas.create_image(100, 112, image=tomato_img)
timer = my_canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
my_canvas.grid(column=2, row=2)

my_window.mainloop()