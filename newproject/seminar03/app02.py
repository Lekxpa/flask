from flask import Flask, render_template, jsonify
from models02 import db, Author, Books

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db.init_app(app)

@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/books/')
def books():
    authors = Author.query.all()
    books = Books.query.all()
    # books = [Books.query.filter(Books.authon == author_pk) for author_pk in authors]
    # books = [Books.query.filter(author_id=author_id) for author_id in Author.query.all()]
    # books = [Books.query.filter(Author.pk == author_pk.pk) for author_pk in authors]
    # print(authors, books)
    context = {
        'title': "Список ",
        'books': books,
        # 'authors': authors,
    }
    return render_template('all_books.html', **context)



@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('Ok books')


# @app.cli.command("add-books")
# def add_student():
#     student = Student(first_name='Ivan', last_name='Ivanov', age=20, gender='male', group=11, faculty_id=1)
#     db.session.add(student)
#     db.session.commit()
#     print('Student added successfully!')

BOOKS = [
    ['Kniga 1', 2000, 2, 1],
    ['Kniga 2', 2001, 21, 2],
    ['Kniga 3', 2002, 6, 1],
    ['Kniga 4', 2003, 1, 2],
    ['Kniga 5', 2004, 5, 1],

]

AUTHORS = [
    ['Ivan', 'Ivanov'],
    ['Maria', 'Andreeva'],
]

@app.cli.command("fill-db")
def fill_tables():
    for author in AUTHORS:
        new_author = Author(first_name=author[0], last_name=author[1])
        db.session.add(new_author)
    db.session.commit()

    for book in BOOKS:
        new_book = Books(title=book[0], year=book[1], count=book[2], author_pk=book[3])
        db.session.add(new_book)
    db.session.commit()



if __name__ == '__main__':
    app.run(debug=True)