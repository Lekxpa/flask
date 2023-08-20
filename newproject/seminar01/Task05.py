# Написать функцию, которая будет выводить
# на экран HTML страницу с заголовком
# "Моя первая HTML страница" и абзацем "Привет, мир!".

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/about/')
def about():
    return 'about'
    # context = {'title': 'Эта страница посвящена...'}
    # return render_template('about.html', **context)


@app.route('/contact/')
def contact():
    return 'contact'
    # context = {'title': 'Контакты...'}
    # return render_template('contact.html', **context)

@app.route('/sum/<int:num1>-<int:num2>/')
def sum_num(num1, num2):
    res = num1 + num2
    return f"{num1} + {num2} = {res}"

@app.route('/str/<text>/')
def txt(text):
    res = len(text)
    return f'Длина строки {text} = {res}'

@app.route('/')
def print_html():
    # html = """<h1>Моя первая страница</h1><p>Привет, мир!</p>"""
    html = """<head>
    <p>Моя первая страница<p>Привет, мир!</p>
    </head>"""
    return html


if __name__ == '__main__':
    app.run(debug=True)