from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
#Initial attributes
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quiz API GUI')
        self.window.config(background='#375362')
        self.score_label = Label(text='Score', background='#375362', foreground='white', font=('Arial', 18, 'normal'))
        self.score_label.grid(row=0, column=1, pady=10)
        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="test", fill='#375362',font=('Arial', 20, 'normal'))
        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image, height=50, width=60, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(row=2, column=0, pady=30)
        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, height=50, width=60, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1, pady=30)
        self.next_question()
        self.window.mainloop()
        
    #Functions        
    def next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_question():
            self.score_label.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Quiz Completed")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
            
        self.window.after(1000, self.next_question)


