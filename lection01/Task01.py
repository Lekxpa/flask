# Напишите простое веб-приложение на Flask, которое будет выводить
# на экран текст "Hello, World!".

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/greeting/')
def greeting():
    return 'Hello world!'


if __name__ == '__main__':
    app.run(debug=True)