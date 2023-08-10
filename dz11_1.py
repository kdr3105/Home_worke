from flask import Flask, request, render_template
import utils
app = Flask(__name__)

@app.route("/")
def page_index():
    print_data = '<div><h1>Котофей Котофеевич</h1></div>\n'
    print_data += '<div><img src="https://avatars.mds.yandex.net/i?id=5c435ce2f5d829ca6bb9063ac5b719edcee93f70-9148863-images-thumbs&n=13" /></div>\n'
    print_data += '<div>\n'
    print_data += '<span><p>Ко́шка (лат. Felis catus) — <a href="https://ru.wikipedia.org/wiki/Кошка">домашнее животное</a>, одно из наиболее популярных (наряду с собакой) «животных-компаньонов».</p></span>\n'
    print_data += '<span><p>С точки <em>зрения научной систематики,</em> домашняя кошка — млекопитающее семейства кошачьих отряда хищных. <strong>Одни исследователи рассматривают домашнюю кошку как подвид дикой кошки</strong>, другие — как отдельный биологический вид[6].</p></span>\n'
    print_data += '<span><p>Являясь <ins>одиночным охотником на</ins> грызунов и других <del>мелких животных</del>, кошка — социальное животное[7],<mark> использующее для общения широкий диапазон звуковых сигналов</mark>, а также феромоны и движения тела[8].</p></span>\n'
    print_data += '</div>\n'
    return print_data

@app.route("/vtoraya/")
def hello():
    return render_template('list.html', items=utils.load_candidates_from_json())

@app.route("/candidate/<x>")
def print_candidat(x):
    return render_template('single.html', candidate=utils.get_candidate(x))

@app.route('/candidate/serch/', methods=['POST', 'GET']) # Доработать этот участок
def open_str():
    poisk = False
    if request.method=='POST':
        naidenoe = utils.get_candidates_by_name(request.form['name'])
        len_serch = len(naidenoe)
        poisk = True
        if naidenoe[0][0]=='id':
            len_serch = 0
            poisk = True
            naidenoe=[[1, "нет таких кандидатов"]]
    else:
        naidenoe = [[0,0]]
        len_serch = 0
    return render_template('search.html', items=naidenoe, lenthe=len_serch, find=poisk)

@app.route('/candidate/skill/', methods=['POST', 'GET'])
def serch_skill():
    poisk = False
    skill_obr = ''
    if request.method=='POST':
        skill_obr = request.form['navik']
        print(skill_obr)
        naidenoe = utils.get_candidates_by_skill(skill_obr)
        print(len(naidenoe))
        len_skill = len(naidenoe)
        poisk = True
        if naidenoe[0][0]=='id':
            len_skill = 0
            poisk = True
            naidenoe=[[1, "нет таких кандидатов"]]
    else:
        naidenoe = [[0,0]]
        len_skill = 0
    return render_template('skill.html', items=naidenoe, skill_name=len_skill, len_skill=skill_obr, find=poisk)


app.run()