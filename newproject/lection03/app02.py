from flask import Flask
from models02 import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'

if __name__ == '__main__':
    app.run(debug=True)


# подружили Flask  с БД. Теперь нужно создать модель