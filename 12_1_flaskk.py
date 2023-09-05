from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def form_page():
    return render_template('post_form.html')
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

app.run()