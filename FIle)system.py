errors_arrays = {
            "cut" : "Вы вышли из системы",
            "noaccess" : "У вас нет доступа в этот раздел",
            "unknown" : "Неизвестная ошибка",
            "timeout" : "Система долго не отвечает",
            "robot" : "Ваши действия похожи на робота"
            }
def get_errors(*error):
    vozvrat = []
    for i in error:
        vozvrat.append(errors_arrays[i])
    return vozvrat

print(get_errors('cut','noaccess'))

code_rus = ("а", "б", "в", "г", 'д', 'е', 'ё', "ж", "з", "и", "й", "к", "л", "м", "н", "о", 'п', "р",
            "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я")

def shift_encoding(stroka):
     otvet=''
     for i in stroka:
        if i in code_rus:
            if code_rus.index(i) == 32:
                otvet += code_rus[0]
            else:
                otvet += code_rus[code_rus.index(i) + 1]
        else:
            otvet += i
     return otvet

def shift_decoding(stroka):
     otvet=''
     for i in stroka:
        if i in code_rus:
            if code_rus.index(i) == 0:
                otvet += code_rus[32]
            else:
                otvet += code_rus[code_rus.index(i) - 1]
        else:
            otvet += i
     return otvet
p1 = shift_encoding('а привет !')
print(p1)
print(shift_decoding(p1))