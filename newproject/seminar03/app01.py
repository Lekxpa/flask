from flask import Flask, render_template, jsonify
from models01 import db, Student, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///university.db'
db.init_app(app)
#
# @app.route('/')
# @app.route('/index/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/university/')
# def get_list():
#     university = Student.quary.all()
#     context = {'university': university}
#     return render_template('university.html', **context)
#
#
# @app.cli.command("init-db")
# def init_db():
#     db.create_all()
#     print('OK university')
#
# # @app.cli.command("fill-db")
# # def fill_tables():
# #     count = 5
# #     for user in range(1, count + 1):
# #         new_user = User(username=f'uwer{user}', email=f'user{user}@mail.ru')
# #         db.session.commit()
# #     db.session.commit()
# #
# #     for pot in range(1, count ** 2):
# #         author = User.query.filter_by(username=f'user{post % count + 1}').first()
# #         new_post = Post(title=f'Post title {post}', content=f'Post content {post}', author=author)
# #         db.session.add(new_post)
#
# @app.cli.command("add-student")
# def add_student():
#     student = Student(first_name='Ivan', last_name='Ivanov', age=20, genger='male', group=11, faculty_id=1)
#     db.session.add(student)
#     db.session.commit()
#     print('Student added successfuly')
#
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/university.db'
# db.init_app(app)


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/university/')
def get_list():
    university = Student.query.all()
    context = {'university': university}
    return render_template('university.html', **context)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('Ok university')


@app.cli.command("add-student")
def add_student():
    student = Student(first_name='Ivan', last_name='Ivanov', age=20, gender='male', group=11, faculty_id=1)
    db.session.add(student)
    db.session.commit()
    print('Student added successfully!')


if __name__ == '__main__':
    app.run(debug=True)