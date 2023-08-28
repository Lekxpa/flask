from flask import Flask, render_template
from models05 import db, User, Post, Comment


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'

@app.route('/data/')
def data():
    return 'Your data!'

@app.route('/users/')
def all_users():
    users = User.query.all()
    context = {'users': users}
    return render_template('users.html', **context)


if __name__ == '__main__':
    app.run(debug=True)


# подружили Flask  с БД. Теперь нужно создать модель