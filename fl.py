from flask import Flask
app = Flask(__name__)
@app.route("/")
def page_index():
    return "Главная страничка"
@app.route("/messages/")
def pagemessages():
    return "Сообщения пользователя"

@app.route('/users/<uid>')
def profile(uid):
    return f'<h1>Профиль {uid}</h1>'
@app.route('/catalog/items/<itemid>')
def profile_1(itemid):
    return f'<h1>Страничка товара {itemid}</hl>'

app.run()