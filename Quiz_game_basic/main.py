from data import question_data
from question_model import Question
from quiz_engine import Quizengine

question_bank = []
for i in question_data:
    question = i["question"]
    answer = i["correct_answer"]
    new_question = Question(question, answer)
    question_bank.append(new_question)

quiz = Quizengine(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Finished\nFinal Score {quiz.score}/{quiz.question_number}")