__author__ = 'reytsman'
import random


class Question():
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

    def copy(self):
        result = Question(self.question, self.answers)
        return result

    def __repr__(self):
        result = self.question + '\n'
        for index, answ in enumerate(self.answers):
            if answ[1]:
                result += str(index + 1) + ") " + answ[0] + "\n"
            else:
                result += str(index + 1) + ") " + answ[0] + "\n"
        return result


def load_questions(path):
    file = open(path, 'r')
    keys = {}
    for key in file:
        keys[key] = ""
    lines = list(keys.keys())
    questions = []
    for line in lines:
        splitted_line = line.split(';')
        temp_question = Question(splitted_line[0], [])
        for element in splitted_line[1:]:
            temp_question.answers.append(element.split('@'))
        questions.append(temp_question)
    return questions


path = 'c:\\temp\\questions2.csv'
questions = load_questions(path)

print("To exit print 0\n")

i = 0
right = 0
wrong = 0
numbers = random.sample(range(1, len(questions)), len(questions) - 1)
while i < len(questions) - 1:
    number = numbers[i]
    if right + wrong > 0:
        print('Right answers: ' + str(int((right / (right + wrong)) * 100)) + '%')
    print('Question: ' + str(i + 1) + ' from ' + str(len(questions)) + '\n')
    print(questions[number])
    user_answer = input("Answer number?\n")

    def check_answer(answer, answers_len):
        if not user_answer.isdigit():
            return False
        if int(answer) > answers_len:
            return False
        return True

    while not check_answer(user_answer, len(questions[number].answers)):
        print("Wrong number\n")
        user_answer = input("Answer number?\n")
    answer = int(user_answer)
    if answer == 0:
        break
    if questions[number].answers[answer - 1][1] == 'True' or questions[number].answers[answer - 1][1] == 'True\n':
        print("Right!\n")
        right += 1
    else:
        print("Wrong!")
        for ans in questions[number].answers:
            if ans[1] == 'True' or ans[1] == 'True\n':
                print("Right answer: " + ans[0] + "\n")
                break
        wrong += 1
    i += 1
