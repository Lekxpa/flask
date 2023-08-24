# создать страницу, на которой будет кнопка "Нажми меня",
# при нажатии на которую будет переход на другую страницу
# с приветствием пользователя по имени

from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/')
def hello_page():
    context = {
        'name': 'hel'
    }
    return render_template('hello.html', **context)

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False)



# ошибка сервера