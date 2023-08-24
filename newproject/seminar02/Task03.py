# создать страницу, на которой будет форма для ввода логина и пароля
# при нажатии на кнопку Отправить будет произведена проверка соответствия
# логина и пароля и переход на страницу приветствия пользователя или страницу
# с ошибкой


from flask import Flask, request, make_response, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/')
def hello_page(name=None):
    context = {
        'name': name or 'hel'
    }
    return render_template('hello.html', **context)

@app.route('/form/', methods=['GET', 'POST'])
def form_page():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        if name == "Helen" and password == 'pass':
            return redirect(url_for('hello_page', name=name))
        return render_template('task03.html', error=True)
    return render_template('task03.html', error=None)


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False)
