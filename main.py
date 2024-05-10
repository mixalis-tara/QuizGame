
from Services.services import *

create_questions(questions_list)

questions = [question.quest for question in questions_list]
options = [option.option for option in questions_list]
answers = [answer.answer for answer in questions_list]


guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter(A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score+=1
        print("Correct")
    else:
        print("INCORRECT :(")
        print(f"{answers[question_num]}!! Is the correct answer")

    question_num+=1

print("--------------------")
print("      Results       ")
print("--------------------")

print("Answers: ", end="")

for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score/len(questions)*100)
print(f"Your score is: {score}%")