# Дорабатываем задачу 1.
# Добавьте две дополнительные страницы в ваше веб-приложение:
# страницу "about"
# страницу "contact".

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

if __name__ == '__main__':
    app.run(debug=True)