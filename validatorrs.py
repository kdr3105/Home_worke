code_rus = ("а", "б", "в", "г", 'д', 'е', 'ё', "ж", "з", "и", "й", "к", "л", "м", "н", "о", 'п', "р",
            "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", ' ')
chifri_cod = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
def chek_pin(pin):
    otvet=''
    if len(pin)==4:
        if pin == '1234':
            otvet = "пароль не может быть равен 1234"
        elif pin.count(pin[0])==4:
            otvet = 'пароль не может содежрать 4 одинаковых символа'
        else:
            otvet = 'пароль верный'
    else:
        otvet = 'пароль должен состоять из 4 символов!'
    return otvet

def chek_pass(pass_):
    otvet = ''
    chofri = False
    bukvi = False
    if len(pass_)>=8:
        for i in pass_:
            if i in  code_rus:
                bukvi = True
            if i in  chifri_cod:
                chofri = True
        if chofri and bukvi:
            otvet = 'пароль верный'
        elif chofri:
            otvet = 'пароль должен содержать хотя бы одну букву'
        else:
            otvet = 'пароль должен содержать хотя бы одну цифру'
    else:
        otvet = 'длинна паролья минимум 8 символов'
    return otvet

def chek_mail(mail_):
    if ("." in mail_) and ('@' in mail_):
        otvet = "почта верная"
    else:
        otvet = "почта должна содержать точку и собаку"
    return otvet

def chek_name(name):
    otvet = 'имя верное'
    for i in name:
        if i not in code_rus:
            otvet = 'Имя должно состоять только из русских букв'

    return otvet
