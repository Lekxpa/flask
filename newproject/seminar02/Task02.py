# создать страницу, на которой будет изображение и ссылка
# на другую страницу, на которой будет отображаться форма
# для загрузки изображений


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

@app.route('/form_page/')
def form_page():
    return render_template('form_page.html')


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False)



# ошибка сервера