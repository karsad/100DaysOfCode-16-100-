from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR, height=800)

        self.canvas = Canvas(height=250, width=300, bg="white",selectborderwidth=0, )
        self.canvas.grid(row=1, column=1, columnspan=2, pady=50)
        self.question = self.canvas.create_text(150, 125, text="Question", font=("Arial", 20, "italic"), fill=THEME_COLOR, width=270)

        true_btn_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_btn_img, borderwidth=0, command=self.check_if_true)
        self.true_btn.grid(row=2, column=1)

        false_btn_img = PhotoImage(file="images/false.png")
        self.true_btn = Button(image=false_btn_img, borderwidth=0, command=self.check_if_false)
        self.true_btn.grid(row=2, column=2)

        self.score = 0
        self.score_box = Label(text=f"Score: {self.score}", bg=THEME_COLOR)
        self.score_box.grid(row=0, column=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        question = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=question)

    def check_if_true(self):
        answer = self.quiz.check_answer("true")
        print(answer)
        if answer == "True":
            self.score += 1
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(ms=1500, func=self.get_next_question)
        self.score_box.config(text=f"Score: {self.score}")

    def check_if_false(self):
        answer = self.quiz.check_answer("false")
        print(answer)
        if answer == "False":
            self.score += 1
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(ms=1500, func=self.get_next_question)
        self.score_box.config(text=f"Score: {self.score}")