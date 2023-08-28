# Создать базу данных для хранения информации
# о студентах университета. База данных должна содержать
# две таблицы: "Студенты" и "Факультеты".
# В таблице "Студенты" должны быть следующие поля:
# id, имя, фамилия, возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля:
# id и название факультета. Необходимо создать связь
# между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить
# список всех студентов с указанием их факультета.
#
# from flask_sqlalchemy import SQLAlchemy
#
# db = SQLAlchemy()
#
# class Faculty(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), unique=True, nullable=False)
#     # faculty = db.relationship('Students', backref='faculty', lazy=True)
#
#
# class Student(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(30), nullable=False)
#     last_name = db.Column(db.String(30), nullable=False)
#     age = db.Column(db.Integer, nullable=False)
#     gender = db.Column(db.String(10), nullable=False)
#     group = db.Column(db.Integer, nullable=False)
#     faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)
#     faculty = db.relationship('Faculty', backref=db.backref('students', lazy=True))
#


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    # faculty = db.relationship('Students', backref='faculty', lazy=True)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)
    faculty = db.relationship('Faculty', backref=db.backref('students', lazy=True))
