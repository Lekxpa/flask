from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, noname"

@app.route('/Николай/')
def nike():
    return "Привет, Николай!"

@app.route('/Иван/')
def ivan():
    return "Привет, Ваня!"


if __name__ == '__main__':
    app.run(debug=True)