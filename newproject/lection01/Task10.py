from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'

@app.route('/users/')
def users():
    _users = [{'name': 'Helen',
               'mail': 'hel@com.com',
               'phone': '+7-989-678-78-89',
               },
              {'name': 'Foma',
               'mail': 'fom@com.com',
               'phone': '+7-989-678-78-90',
               },
              {'name': 'Max',
               'mail': 'max@com.com',
               'phone': '+7-989-678-78-87',
               }, ]

    context = {'users': _users,
               'title': 'Точечная нотация'}
    return render_template('users.html', **context)


if __name__ == '__main__':
    app.run(debug=True)