# importing the module
import json
import datetime



with open('questions.json', 'r', ) as f:
    my_questions = json.load(f)

def load_questions(my_questions=my_questions):

    urovni = []
    for keys_ ,values_ in my_questions.items():
        for keyq, valueq in values_.items():
            if valueq['asked']==False:
                urovni.append(keyq)
            else:
                urovni.append(" ")
        print(keys_, ', '.join(urovni))
        urovni = []


def parse_input():
    return

def show_question(category, lavel ,schet, correct, false_):
    if category in  my_questions.keys():
        if lavel in my_questions[category].keys():
            if my_questions[category][str(lavel)]['asked']==False:
                print(f'Слово {my_questions[category][str(lavel)]["question"]} в переводе означает:')
                otvet = input()
                if otvet==my_questions[category][str(lavel)]["answer"]:
                    schet += int(lavel)
                    print(f'Верно, +{lavel}. Ваш счет = {schet}')
                    correct += 1
                else:
                    false_ += 1
                    print(f'Неверно, правильный ответ {my_questions[category][str(lavel)]["answer"]}. Ваш счет = {schet}')
                my_questions[category][str(lavel)]["asked"] = True
            else:
                print('Такой вопрос уже был сигран, попробуйте еще раз')
        else:
            print('Такого вопроса нет, попробуйте еще раз')
    else:
        print("Такой категории нет, попробуйте еще раз")
    return (schet, correct, false_)

def show_stats():
    return

def save_results_to_file(score):
    with open("score.json", "w") as write_file:
        json.dump(score, write_file)
    return


def game_followe(my_q):
    result = False
    for values_ in my_q.values():
        for keyq, valueq in values_.items():
            if valueq['asked']==False:
                result = True
    return result


def main():
    user_score_ = 0
    user_correct = 0
    user_false = 0
    x = True
    while x:
        load_questions()
        game_ansver = input('Выберете категорию и уровень ')
        try:
            category, lavel = game_ansver.split()
            user_score_, user_correct, user_false = show_question(category, lavel, user_score_, user_correct, user_false)
            x = game_followe(my_questions)
        except ValueError:
            print('Введено недостаточное количество значений')

    print('У вас закончились вопросы')
    print(f'Ваш счет: {user_score_}')
    print(f'Верных ответов: {user_correct}')
    print(f'Неверных ответов: {user_false}')
    curr_date = datetime.datetime.now().strftime("%Y.%m.%d")
    score_json = {curr_date: {"points": user_score_,"correct": user_correct,'incorrect': user_false}}
    save_results_to_file(score_json)


main()