from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def form_page():
    return render_template('zagruzka.html')
@app.route('/search')
def search_page():
    s = request.args.get('s')
    if s:
        return f'Вы ввели слово {s}'
    else:
        return 'Вы не ввели ничего'

@app.route('/filter')
def filter_page():
    fromvalue = request.args['from']
    tovalue = request.args['to']
    return f"Ищем в диапазоне от {fromvalue} до {tovalue}"

@app.route('/add', methods = ["POST"])
def add_page():
    task = request.form['task_name']
    return f"Вы добавили задачу {task}"
@app.route('/upload', methods = ["POST"])
def page_upload():
    # Получаем объект картинки из формы
    picture = request.files.get("picture")
    # Получаем имя файла у загруженного фала
    filename = picture.filename
    # Сохраняем картинку под родным именем в папку uploads
    picture.save(f"./{filename}")
    return f"Загружен файл {picture.filename}"

app.run()