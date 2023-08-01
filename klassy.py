import json
import requests
import random




class Question():
    def __init__ (self, text, level, ansver):
        self.text = text
        self.level = level
        self.ansver = ansver
        self.asked = False
        self.user_answer = ''
        self.score = 0


    def get_point(self):
        self.score = int(self.level) * 10

    def is_correct(self):
        return self.ansver == self.user_answer

    def bild_question(self):
        return (f"Вопрос: {self.text}" , f"Сложность {self.level}")

    def bild_feedback(self):
        if self.is_correct():
            self.get_point()
            return f'Ответ верный, получено баллов {self.score}'
        else:
            return f'Ответ неверный, верный ответ {self.ansver}'

"""https://jsonkeeper.com/b/ZTYT азмещение json опросов
https://jsonkeeper.com/b/2LY0
"""
class quests(list):

    def calculate(self):
        vopros = 0
        verno = 0
        total_score = 0
        for i in self:
            vopros += 1
            if i.score!=0:
                verno += 1
            total_score += i.score
        return(vopros, verno, total_score)


def main():
    q = quests()
    json_qustions = requests.get("https://jsonkeeper.com/b/2LY0", verify=False).text
    data = json.loads(json_qustions)
    for i in data.values():
        q.append(Question(i['q'],i['d'],i['a']))
    random.shuffle(q)
    for i in range(len(q)):
        print(f"Вопрос {q[i].text}")
        print(f"Сложность {q[i].level}/5")
        q[i].user_answer = input()
        q[i].asked = True
        print(q[i].bild_feedback())
        # print(q[i].text, q[i].level, q[i].asked, q[i].user_answer, q[i].score, q[i].ansver)

    print('Вот и все!')
    i, y, z = q.calculate()
    print(f'Отвечено на {y} вопроса  из {i}')
    print(f'Набранно балов {z}')
main()