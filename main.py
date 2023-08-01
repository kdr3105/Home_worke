# Сегодня мы потренируемсярасшифровывать азбуку Морзе
# Нажмите Enter и начнем
# Слово 1 - ... -. .- -.- .
# Snayke
# Верно, Snayke!
#
# Список английских слов
#
# morze_encoder(sentence) ереводит англ слова в код морзе
#
# get_word() олучает случайное слово из списка
# answer[] писок ответов булевое
# print_statistics() выводит статистику игрока
#
#
import random
list_of_word = ['code', 'bit', 'list', 'soul', 'next']
"""
Самая главная программа. примитивная 
до ужаса
"""
def morze_encoder(sentence):
    """
    Функция переводит анлийские слова в код Морзе
    :param sentence: слово на английском str
    :return: трока из точек и тере в коде Морзе str
    """
    morze_code = {'A': '.-', 'B': '-...', 'C': '-.-.',
                'D': '-..', 'E': '.', 'F': '..-.',
                'G': '--.', 'H': '....', 'I': '..',
                'J': '.---', 'K': '-.-', 'L': '.-..',
                'M': '--', 'N': '-.', 'O': '---',
                'P': '.--.', 'Q': '--.-', 'R': '.-.',
                'S': '...', 'T': '-', 'U': '..-',
                'V': '...-', 'W': '.--', 'X': '-..-',
                'Y': '-.--', 'Z': '--..',
                '0': '-----', '1': '.----', '2': '..---',
                '3': '...--', '4': '....-', '5': '.....',
                '6': '-....', '7': '--...', '8': '---..',
                '9': '----.'
                }
    otvet = ''
    if type(sentence)==str:
        for i in sentence:
            otvet += morze_code[i.title()]+' '
    else:
        otvet = 'введен некоректный ответ'
    return(otvet)
# print(morze_encoder('little'))


def get_word():
    """
    Возвращает случайное слово из списка list_of_word
    :return: слово в формате str
    """
    return list_of_word[random.randrange(0, len(list_of_word))]
# print(get_word())


def print_statistics(result_list):
    """
    подсчитывает статистику ответов
    :return: нечего
    """
    print(f'Всего задачек {len(result_list)}')
    print(f'Отвечено верно: {result_list.count(True)}')
    print(f'Отвечено неверно: {result_list.count(False)}')
    return


def main():
    """
    основная прогамма
    :return: нечего
    """
    answers = []
    print('Сегодня мы потренируемся расшифровывать морзянку')
    input('Нажмите Enter и начинаем')
    for i in range(4):
        wopros = get_word()
        wopros_mz = morze_encoder(wopros)
        print(f'Слово {i+1} - {wopros_mz}')
        otvet = input()
        if wopros==otvet:
            print(f"Верно, {otvet}")
            answers.append(True)
        else:
            print(f'Неверно, {wopros}')
            answers.append(False)
    print_statistics(answers)
    return

main()