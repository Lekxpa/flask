# Задание №6
# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.

from flask import Flask, flash, request, make_response, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<name>/')
def hello(name):
    return f'Привет, {name}. Проверка прошла успешно! Можешь получить паспорт!'


@app.route('/check_age/', methods=['GET', 'POST'])
def check_age():
    if request.method == 'POST':
        min_age: int = 14
        name = request.form.get('name')
        age = int(request.form.get('age'))
        if age >= min_age:
            return redirect(url_for('hello', name=name))
        return render_template('checkage.html', error=True)
    return render_template('checkage.html', error=None)
    

# Задание №7
# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.

@app.route('/count_square/', methods=['GET', 'POST'])
def count_square():
    res = None
    if request.method == 'POST':
        numb = int(request.form.get('numb'))
        res = numb ** 2
        return redirect(url_for('square', numb=numb, res=res))
    return render_template('square.html')

@app.route('/square/<numb>-<res>/')
def square(numb, res):
    return f'{numb}^2 = {res}'


# Задание №8
# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".

app.secret_key = 'a5b516ff2ac25d3cba20fbe3207d56f18551c850e8fa5bbc593b59570b199a2c'
"""
Генерация надежного секретного ключа
>>>import secrets
>>>secrets.token_hex()
"""


@app.route('/hello_fl/', methods=['GET', 'POST'])
def hello_fl():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'ПРивет, {name}', 'success')
        return redirect(url_for('hello_fl'))
    return render_template('fl_form.html')




# Задание №9
# Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# При отправке которой будет создан cookie файл с данными
# пользователя
# Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.


@app.route('/cook/', methods=['GET', 'POST'])
def cook():
    if request.method == 'POST':
        name = request.form.get('name')
        mail = request.form.get('mail')
        response = make_response("Cookie установлен")
        # response.headers['new_head'] = 'New-value'
        # response = make_response(render_template('cook.html'))
        response.set_cookie("name", name)
        response.set_cookie("mail", mail)
        return redirect(url_for('hello_cook', name=name, mail=mail))
    return render_template('cook.html')


@app.route('/hello_cook/<name>-<mail>', methods=['GET', 'POST'])
def hello_cook(name, mail):
    if request.method == 'POST':
        response = make_response('Cookie')
        response.delete_cookie('name')
        response.delete_cookie('mail')
        return redirect(url_for('cook'))
    # return render_template('hello_cook.html')
    return f'Привет, {name}' + render_template('hello_cook.html')


if __name__ == '__main__':
    app.run(debug=True)