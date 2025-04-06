from question_model import Question
from data import question_data
from quiz_brain import Quiz
question_bank = []

for question in question_data:
    question_bank.append(Question(question['text'], question['answer']))

quiz_game = Quiz(question_bank)

while quiz_game.still_has_questions():
    quiz_game.next_question()
quiz_game.quiz_end()