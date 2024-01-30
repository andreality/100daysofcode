from quiz.data import question_data
from quiz.question_model import Question
from quiz.quiz_brain import QuizBrain


question_bank = []
for item in question_data:
    new_question = Question(text=item["text"], answer=item["answer"])
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_list=question_bank)
quiz_brain.run()

