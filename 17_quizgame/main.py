# from quiz.data import question_data
from quiz.open_trivia import get_question_data, CATEGORIES
from quiz.question_model import Question
from quiz.quiz_brain import QuizBrain


pick_category = input("Would you like to select a category? Y/N \n")
if pick_category == "Y":
    print(CATEGORIES)
    category_num = input("Please enter category number.")
else:
    category_num = None
num_questions = int(input("How many questions would you like? \n"))
question_bank = get_question_data(num_questions=num_questions, category_num=category_num)
quiz_brain = QuizBrain(question_list=question_bank)
quiz_brain.run()

