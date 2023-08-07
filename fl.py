# Сперва импортируем Flask
from flask import Flask
# Затем создадим экземпляр этого Flask, назовем его арр -
# это будет наше приложение
арр = Flask(__name__)
# Что такое name ?
# При запуске сценария значение переменной name равно main
# Эта переменная помогает Flask разбрираться, где он находится
# и без нее он просто не заработает
# Теперь создадим функцию, которая будет что-то делать
# Например, pageindex - это функция, которая будет возвращать 'Hello Wor
def page_index():
    return "Я страничка"
# Теперь используем метод у приложения, который зарегистрирует маршрут
# Например, для главной страницы будет вызвана функция pageindex
app.add_url_rule('/',view_func=page_index)