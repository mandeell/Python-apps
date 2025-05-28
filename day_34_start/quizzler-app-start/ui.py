from tkinter import *
from quiz_brain import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.window.minsize(300,250)
        self.window.resizable(width=False, height=False)
        self.font_config = ("Arial", 20, "italic")

        self.score_label = Label(text="Score: 0",font=("arial",12,"bold"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width = 280,
            font=self.font_config,
            text="Welcome to Quizler",
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1,column=0, columnspan=2, pady=50)
        try:
            self.true_image = PhotoImage(file="images/true.png")
            self.false_image = PhotoImage(file="images/false.png")
        except Exception as e:
            print(f"Error loading image: {e}")
            self.window.destroy()
            return

        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=self.false_image,highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2,column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self) -> None:
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.config(bg="white")
        else:
            self.end_quiz()

    def true_pressed(self) -> None:
        is_right = self.quiz.check_answer("True")
        self.update_score()
        self.give_feedback(is_right)


    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.update_score()
        self.give_feedback(is_right)


    def give_feedback(self,is_right: bool) -> None:
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



    def update_score(self) -> None:
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def end_quiz(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(
            self.question_text,
            text=f"Quiz completed!\nFinal score: {self.quiz.score}/{self.quiz.question_number}")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
