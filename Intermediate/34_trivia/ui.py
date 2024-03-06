import tkinter

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class TriviaInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        #self.text = self.quiz.current[0]
        self.window = tkinter.Tk()
        self.window.title("It's time for Trivia !!!")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = tkinter.Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            120, 
            text='question', 
            width=200, 
            font=('Arial', 15, 'italic')
        )
        self.canvas.grid(column=0, row=1,  sticky='we', columnspan=2, pady=20)

        self.score_text = tkinter.Label(text="Score: 0/0", bg=THEME_COLOR)
        self.score_text.grid(column=1, row=0)

        self.true_image = tkinter.PhotoImage(file='images/true.png')
        self.true_button = tkinter.Button(
            image=self.true_image, 
            command=lambda: self.answer_buttons('True')
        )
        self.true_button.grid(column=0, row=2)

        self.false_image = tkinter.PhotoImage(file='images/false.png')
        self.false_button = tkinter.Button(
            image=self.false_image, 
            command=lambda: self.answer_buttons('False')
        )
        self.false_button.grid(column=1, row=2, pady=20)

        self.translate_button = tkinter.Button(
            text='Дуже цікаво але ніхера не зрозуміло',
            command=self.translate)
        self.translate_button.grid(column=0, row=3, sticky='we', columnspan=2)
        
        self.get_question()

        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg='white')
        self.quiz.get_new_question()
        self.canvas.itemconfig(self.question_text, text=self.quiz.current[0])
    
    def answer_buttons(self, user):
        is_right = self.quiz.check_answer(user)
        self.feedback(is_right)
        self.score_text.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")


    def translate(self):
        self.quiz.get_translate()
        self.canvas.itemconfig(self.question_text, text=self.quiz.current[2])

    def feedback(self, correct):
        color = 'green' if correct else 'red'
        self.canvas.config(bg=color)
        self.window.after(1000, self.get_question)