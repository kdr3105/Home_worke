from flask import Flask

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


app.run()