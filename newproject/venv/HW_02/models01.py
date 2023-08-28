# Задание №3 Доработаем задача про студентов
# Создать базу данных для хранения информации о студентах и их оценках в учебном заведении.
# База данных должна содержать две таблицы: "Студенты" и "Оценки".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа и email.
# В таблице "Оценки" должны быть следующие поля: id, id студента, название предмета и оценка.
# Необходимо создать связь между таблицами "Студенты" и "Оценки".
# Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их оценок


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)


class Marks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    name_of_subject = db.Column(db.String(30), nullable=False)
    mark = db.Column(db.Integer, nullable=False)
    student = db.relationship('Student', backref=db.backref('marks', lazy=True))