THEME_COLOR = "#375362"
from tkinter import*
from quiz_brain import QuizBrain


class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, height=50, width=50, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white")

        self.question_text = self.canvas.create_text(150, 125,width=280, text="Default text", fill=THEME_COLOR, font=("Arial", 16, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)



        right = PhotoImage(file="images/true.png")
        wrong = PhotoImage(file="images/false.png")

        self.true_b = Button(image=right, highlightthickness=0, command=self.true_b_press)
        self.true_b.grid(column=1, row=2)
        self.false_b = Button(image=wrong, highlightthickness=0, command=self.false_b_press)
        self.false_b.grid(column=0, row=2)

        self.get_next_question()


        self.window.mainloop()

    def true_b_press(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_b_press(self):
        self.give_feedback(self.quiz.check_answer("False"))



    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've Reached the end of questions...")
            self.true_b.config(state="disabled")
            self.false_b.config(state="disabled")

    def give_feedback(self, is_right:bool):
        if is_right==True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.get_next_question)






