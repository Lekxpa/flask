# Написать функцию, которая будет принимать
# на вход два числа и выводить на экран их сумму.

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


if __name__ == '__main__':
    app.run(debug=True)