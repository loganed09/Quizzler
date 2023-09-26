from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)


        self.score_text = Label(text= f"Score: 0")
        self.score_text.config(bg=THEME_COLOR, fg="white", pady=15)
        self.score_text.grid(row=0, column=1)

        self.canvas = Canvas(self.window, width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            width=280, 
            text="Some Text", 
            fill=THEME_COLOR, 
            font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, bg=THEME_COLOR, command=self.true_button)
        self.true_button.grid(column=0, row=2, pady=20)
        self.false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, bg=THEME_COLOR, command=self.false_button)
        self.false_button.grid(column=1, row=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=question_text)

    def update_score(self):
        self.get_next_question()
        self.score_text.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number-1}")

    def true_button(self):
        is_right = self.quiz.check_answer("True")
        self.update_score()
    
    def false_button(self):
        is_wrong = self.quiz.check_answer("False")
        self.update_score()