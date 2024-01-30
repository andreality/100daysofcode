class QuizBrain:
    def __init__(self, question_list):
        self.current_question_number = 0
        self.question_list = question_list
        self.max_question_number = len(self.question_list) - 1
        self.has_more_questions = True
        self.score = {"right": 0, "wrong": 0}

    @property
    def current_question(self):
        return self.question_list[self.current_question_number]

    @property
    def still_has_questions(self):
        return self.current_question_number < self.max_question_number

    def next_question(self):
        msg = f"Q.{self.current_question_number + 1}: {self.current_question.text} (True/False)?:"
        self.current_question_number += 1
        return input(msg)

    def check_if_answer_correct(self, answer):
        is_correct = answer == self.current_question.answer
        if is_correct:
            self.score["right"] += 1
            print("You are correct!")
        else:
            self.score["wrong"] += 1
            print("You are wrong!")
        return is_correct

    def print_score(self):
        print(f"You have {self.score['right']} correct, and {self.score['wrong']} incorrect.")

    def end_game(self):
        print(f"Game is over!")
        self.print_score()

    def run(self):
        while self.still_has_questions:
            user_response = self.next_question()
            self.check_if_answer_correct(user_response)
            self.print_score()
        self.end_game()



