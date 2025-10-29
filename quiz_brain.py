class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    # TODO: 1. asking the questions
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(current_question.answer, user_input)

    # TODO: 2. checking if the answer was correct
    def check_answer(self, correct, answer):
        if answer.lower() == correct.lower():
            self.score += 1
            print(f"Your answer is correct!")
        else:
            print(f"Your answer was wrong.")
        print(f"The correct answer was: {correct}")
        print(f"your score is {self.score}/{self.question_number}")
        print("\n")

