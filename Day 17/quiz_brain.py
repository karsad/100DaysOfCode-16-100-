class Quiz:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        answer = input(f"Q.{self.question_number+1} {self.question_list[self.question_number].question} (true/false): ")
        self.check_answer(answer, self.question_list[self.question_number].answer)
        self.question_number += 1


    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You're right!")
            self.score += 1
        else: print("You're wrong!")
        print(f"Correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number+1}\n")

    def quiz_end(self):
        print("You have completed the quiz!")
        print(f"Your final score was: {self.score}/{self.question_number}")