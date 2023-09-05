import logging
from flask import Flask, request, render_template
logging.basicConfig(filename="basic.log", level=logging.INFO)
app = Flask(__name__)
@app.route('/',)
def page_index():
    logging.info("Главная страница запрошена")
    return "Главная страница"
@app.route('/store')
def page_store():
    logging.info("Страница магазина запрошена")
    return "Страница магазина "
@app.route('/store/<cat>')
def pagecat(cat):
    logging.info(f"Страница категории {cat} запрошена")
    return f"Страница категории {cat} "

app.run()