from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #
after_id = None
session_count = 0
def reset_timer():
    global after_id, session_count
    if after_id is not None:
        window.after_cancel(after_id)
        after_id = None
    canvas.itemconfig(timer_label, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    session_count = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Start the timer with 25 minutes."""
    global session_count
    session_count += 1
    if session_count % 8 == 0:
        countdown_timer(LONG_BREAK_MIN * 60)
        title_label.config(text="Long Break", fg=RED)
    elif session_count % 2 == 0:
        countdown_timer(SHORT_BREAK_MIN * 60)
        title_label.config(text="Short Break", fg=PINK)
    else:
        countdown_timer(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def format_time(seconds):
    """Convert seconds to MM:SS format."""
    minutes, secs = divmod(seconds, 60)
    return f"{minutes:02d}:{secs:02d}"

def countdown_timer(count):
    """Run a countdown timer using after for non-blocking updates."""
    global after_id
    canvas.itemconfig(timer_label, text=format_time(count))
    if count > 0:
        after_id = window.after(1000, countdown_timer, count - 1)
    else:
        after_id = None
        work_session_completed = (session_count + 1) // 2
        check_label.config(text="✓" * work_session_completed)  # Add checkmark for each work session
        if session_count < 8:
            start_timer()  # Auto-start next session

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.minsize(width=500, height=400)

canvas = Canvas(width=400, height=448, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file = "tomato_resized_400x448.png")
canvas.create_image(200,224, image=tomato_img)
timer_label = canvas.create_text(200,280, text="00:00",fill="white", font=(FONT_NAME,30,"bold"))
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", font=(FONT_NAME,30,"bold"), fg=GREEN,bg=YELLOW)
title_label.grid(row=0, column=1)

start_button = Button(text="Start", font=(FONT_NAME,10,"bold"),highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME,10,"bold"), highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = Label(text="", font=(FONT_NAME,30,"bold"), bg=YELLOW, fg=GREEN)
check_label.grid(row=3, column=1)





window.mainloop()
