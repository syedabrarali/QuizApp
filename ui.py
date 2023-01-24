from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some question goes in here",
            fill=THEME_COLOR,
            font=("Arial", 16, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true_image = PhotoImage(file='images/true.png')
        false_image = PhotoImage(file='images/false.png')
        self.true_button = Button(image=true_image, pady=5, padx=5, command=self.correct_answer)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_image, pady=5, padx=5, command=self.wrong_answer)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You've reached the end of the questions list")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def correct_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
