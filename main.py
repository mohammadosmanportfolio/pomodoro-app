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
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    window.after_cancel(timer)
    reps = 0
    above_tomato_text.config(text='Timer', fg=PINK)
    check_marks.config(text="")
    canvas.itemconfig(timer_text, text='00:00')
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    if reps == 8:
        above_tomato_text.config(text='Break', fg=RED)
        check_marks.config(text=check_marks.cget('text') + "✔")
        reps = 0
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 1:
        above_tomato_text.config(text='Work', fg=GREEN)
        count_down(WORK_MIN * 60)
    else:
        above_tomato_text.config(text='Break', fg=PINK)
        check_marks.config(text=check_marks.cget('text') + "✔")
        count_down(SHORT_BREAK_MIN * 60)


def count_down(count):
    count_minutes = math.floor(count/60)
    count_seconds = count % 60
    if count_seconds >= 0 and count_seconds <= 9:
        count_seconds = "0" + str(count_seconds)
    if count >= 0:
        canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
        global timer       
        timer = window.after(1000, count_down, count - 1)
    if count < 0 and reps <= 7:
        start_timer()
    else:
        return

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title(string='Pomodoro')
window.config(background=YELLOW, padx=100, pady=100)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 28, 'bold'), fill='white')
canvas.grid(column=2, row=1)

above_tomato_text = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 26, 'bold'), bg=YELLOW)
above_tomato_text.grid(column=2, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row=2)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=3, row=2)

check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(column=2, row=3)


window.mainloop()