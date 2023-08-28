from flask import Flask
from models05 import db, User, Post, Comment


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'

@app.cli.command("init-db")
#при появлении в командной строке flask или db - запусть эту функцию
def init_db():
    # показать ошибку с неверным wsgi.py
    db.create_all()
    print('OK')


if __name__ == '__main__':
    app.run(debug=True)


# подружили Flask  с БД. Теперь нужно создать модель