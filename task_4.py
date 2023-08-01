# from validatorrs import chek_pin, chek_pass, chek_mail, chek_name
import validatorrs as vvvv
import random as rd

user_name = input('Введите ваше имя ')
user_mony = 0
with open('words.txt') as fhile:
    for i in fhile:
        pereme = i
        a = pereme.strip()
        a = list(a)
        print(a)
        rd.shuffle(a)
        print(f'угадайте слово {"".join(a)}')
        otvet = input()
        if otvet.strip()==pereme.strip():
            print('Верно! Вы получаете 10 очков')
            user_mony += 10
        else:
            print(f'Не верно! Верный ответ {pereme}')

with open('hystory.txt', 'a') as f:
    f.writelines(f'{user_name} {user_mony}\n')
max_count = 0
top_user = ''
game_count = 0
with open('hystory.txt', 'r') as f:
    for i in f:
        game_count += 1
        name_u, count_u = i.split()
        if max_count < int(count_u):
            max_count = count_u
            top_user = name_u
print (f'сего сыграно игр: {game_count}')
print(f'Максимальный рекорд {max_count} принадлежит пользователю {top_user}')
