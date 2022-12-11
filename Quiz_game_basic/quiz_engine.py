class Quizengine:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}"
                            f"/{len(self.question_list)}. {current_question.text}"
                            f"(True/False):  ")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("Right Answer")
        else:
            print(f"Wrong Answer\nThe correct answer is :{correct_answer}.\n"
                  f"Your score is {self.score}/{len(self.question_list)}")




