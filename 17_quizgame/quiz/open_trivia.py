import requests
from quiz.question_model import Question


CATEGORIES = {
    "Science and Nature": 17,
    "Computers": 18,
    "Mathematics": 19,
    "History": 23,
    "Politics": 24,
    "Animals": 27
}


def get_question_data(num_questions, category_num: int = None):
    if category_num is not None:
        url = f"https://opentdb.com/api.php?amount={num_questions}&category={category_num}&type=boolean"
    else:
        url = f"https://opentdb.com/api.php?amount={num_questions}&type=boolean"
    r = requests.get(url=url)
    data = r.json()

    question_bank = []
    for item in data["results"]:
        new_question = Question(text=item["question"], answer=item["correct_answer"])
        question_bank.append(new_question)
    return question_bank


