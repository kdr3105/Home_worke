from flask import Flask
import json

app = Flask(__name__)
with open('candidate.json', 'r', ) as f:
    my_candidats = json.load(f)
for i in my_candidats:
    print(i)
@app.route("/")
def page_index():
    print_data = ''
    print_data += '<pre>\n'
    for i in my_candidats:
        print_data += f"Имя кандидата - {i['name']}\n"
        print_data += f"Позиция кандидата {i['position']}\n"
        print_data += f"Навыки через запятую {i['skills']}\n"
        print_data += f"=========================================================\n"
    print_data += '</pre>'
    return print_data
@app.route("/candidate/<int:xid>")
def pagemessages():
    print_candidat = ''
    for i in my_candidats:
        if i['id']==xid:
            print_candidat = f'< img src = "({i["picture"]})">\n'
            print_candidat += f"<рге>"
            print_candidat += f"Имя кандидата - {i['name']}\n"
            print_candidat += f"Позиция кандидата {i['position']}\n"
            print_candidat += f"Навыки через запятую {i['skills']}\n"
            print_candidat += f"</рге>"
            break
        else:
            print_candidat += f"<рге>"
            print_candidat += f"Нет такого кандидата"
            print_candidat += f"</рге>"
    return "Сообщения пользователя"

@app.route('/users/<uid>')
def profile(uid):
    return f'<h1>Профиль {uid}</h1>'
@app.route('/catalog/items/<itemid>')
def profile_1(itemid):
    return f'<h1>Страничка товара {itemid}</hl>'

app.run()