from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=40,pady=40)
        self.font_config = ("Arial", 20, "italic")
        self.canvas = Canvas(width=300,height=250,bg="white")
        self.canvas_label = self.canvas.create_text(150,125,font=self.font_config, text="Welcome to Quizzler")
        self.canvas.grid(row=1,column=0, columnspan=2, pady=20)

        self.score_label = Label(text="Score: 0",font=("arial",12,"bold"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0,column=1, pady=10)

        self.true_button = Button(text="✔", font=("arial", 30), bg="#4CAF50", fg="white", width=3, height=1,
                                  relief="flat", bd=0)
        self.true_button.grid(row=2,column=0)

        self.false_button = Button(text="✘", font=("arial", 30), bg="#F44336", fg="white", width=3, height=1,
                                bd=0)
        self.false_button.grid(row=2,column=1)


        self.window.mainloop()

