from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(bg=THEME_COLOR,padx=40,pady=40)
        self.window.minsize(800,800)
        self.window.resizable(width=False, height=False)
        self.font_config = ("Arial", 20, "italic")
        self.canvas = Canvas(width=800,height=700,bg="white")
        self.canvas_label = self.canvas.create_text(400,350,font=self.font_config, text="Welcome to Quizler")
        self.canvas.grid(row=1,column=0, columnspan=2, pady=20)

        self.score_label = Label(text="Score: 0",font=("arial",12,"bold"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0,column=1, pady=10)

        self.true_button = Button(text="✔", font=("arial", 50), bg="#4CAF50", fg="white")
        self.true_button.grid(row=2,column=0, padx=20)

        self.false_button = Button(text="✘", font=("arial", 50), bg="#F44336", fg="white")
        self.false_button.grid(row=2,column=1, padx=20)


        self.window.mainloop()

