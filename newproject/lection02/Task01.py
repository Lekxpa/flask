from flask import Flask, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi-ffi!'


@app.route('/test_url_for/<int:num>/')
def test_url(num):
    text = f'В num лежит {num}<br>'
    text += f'Функция {url_for("test_url", num=42) = }<br>'
    text += f'Функция {url_for("test_url", num=42, data="new_data") = }<br>'
    text += f'Функция {url_for("test_url", num=42, data="new_data", pi=3.14515) = }<br>'
    return text

@app.route('/sum/<int:num1>-<int:num2>/')
def sum_num(num1, num2):
    res = num1 + num2
    return f"{num1} + {num2} = {res}"

@app.route('/about/')
def about():
    context = {
        'title': "Обо мне",
        'name': "Helen",
    }
    return render_template('about.html', **context)

if __name__ == '__main__':
    app.run(debug=True)