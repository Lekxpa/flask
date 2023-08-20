# Написать функцию, которая будет выводить на экран HTML страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через контекст.


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


@app.route('/get_sheet/')
def get_sheet():
    sheet = [
        {'first_name': 'Andrey', 'last_name': 'Ivanov', 'age': 20, 'avg_grade': 4.5},
        {'first_name': 'Alex', 'last_name': 'Petrov', 'age': 21, 'avg_grade': 4.7},
        {'first_name': 'Anne', 'last_name': 'Frau', 'age': 19, 'avg_grade': 4.8}
    ]
    # sheet_head = list(sheet[0].keys())
    # sheet_content = [list(i.values()) for i in sheet]
    # return render_template('get_sheet.html', sheet_head=sheet_head, sheet_content=sheet_content)
    return render_template('get_sheet.html', students=sheet)
# @app.route('/students/')
# def students():
# context = {
# "students": [{"first_name": "Иван",
# "last_name": "Иванов",
# "age": 30,
# "grade": 5, },
# {
# "first_name": "Максим",
# "last_name": "Максимов",
# "age": 35,
# "grade": 2,
# },
# {
# "first_name": "Андрей",
# "last_name": "Андреев",
# "age": 25,
# "grade": 7,
# }]
# }
# return render_template("students.html", **context)

# <table>
# {% for student in students %}
#
# <tr>
# <td>{{ student.first_name }}</td>
# <td>{{ student.last_name }}</td>
# <td>{{ student.age }}</td>
# <td>{{ student.grade }}</td>
# </tr>
# {% endfor %}
# </table>

if __name__ == '__main__':
    app.run(debug=True)