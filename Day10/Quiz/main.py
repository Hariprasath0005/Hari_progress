from data import question_data
from question_model import question
from quiz_brain import QuizBrain
question_bank=[]
for i in question_data:
    question_text = i["text"]
    question_ans = i["answer"]
    new_qusetion = question(question_text,question_ans)
    question_bank.append(new_qusetion)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("Quiz completed")
print(f"Final score: {quiz.score}/{quiz.question_number}")