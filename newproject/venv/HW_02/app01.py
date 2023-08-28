from flask import Flask, render_template, jsonify
from models01 import db, Student, Marks

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///univer.db'
db.init_app(app)


@app.route('/')
@app.route('/index/')
def index():
    return "univer"
    # return render_template('index.html')


@app.route('/univer/')
def get_mark_list():
    univer = Marks.query.all()
    context = {'univer': univer}
    return render_template('univer.html', **context)

@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK univer')


@app.cli.command("add-student")
def add_student():
    student = Student(first_name='Olga', last_name="Petrova", group='22', email= "olgaP@mail.ru")
    student1 = Student(first_name='Helga', last_name="Prom", group='25', email="helgaP@mail.ru")
    db.session.add(student)
    db.session.add(student1)
    db.session.commit()
    print('Student added')


@app.cli.command('add-mark')
def add_mark():
    mark = Marks(name_of_subject='History', mark=4, student_id=1)
    mark1 = Marks(name_of_subject='Geograghy', mark=5, student_id=2)
    db.session.add(mark)
    db.session.add(mark1)
    db.session.commit()
    print('mark added')


if __name__ == '__main__':
    app.run(debug=True)