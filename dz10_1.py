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
def pagemessages(xid):
    print_candidat = ''
    exist_candidate = True
    for i in my_candidats:
        if i['id']==xid:
            print_candidat = f'<img src="({i["picture"]})">\n'
            print_candidat += f"</img>\n"
            print_candidat += f"<рге>\n"
            print_candidat += f"Имя кандидата - {i['name']}\n"
            print_candidat += f"Позиция кандидата {i['position']}\n"
            print_candidat += f"Навыки через запятую {i['skills']}\n"
            print_candidat += f"</рге>\n"
            exist_candidate = False
            break
    if exist_candidate:
        print_candidat += f"<рге>\n"
        print_candidat += f"Нет такого кандидата\n"
        print_candidat += f"</рге>\n"
    return print_candidat

@app.route('/skill/<string:scill_x>')
def skill_finde(scill_x):
    skill_data = ''
    skill_data += '<pre>\n'
    exist_skils = True
    for i in my_candidats:
        if str(scill_x).lower() in str(i["skills"]).lower().split(', '):
            skill_data += f"Имя кандидата - {i['name']}\n"
            skill_data += f"Позиция кандидата {i['position']}\n"
            skill_data += f"Навыки через запятую {i['skills']}\n"
            skill_data += f"=========================================================\n"
            exist_skils = False
    if exist_skils:
        skill_data += "Нет кандидатов с таким навыком\n"
    skill_data += '</pre>\n'
    return skill_data

app.run()