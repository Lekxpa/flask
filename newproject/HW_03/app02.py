from flask import Flask, request, render_template, redirect, url_for
from flask-wtf import CSRFProtect
import secrets
from werkzeug.security import generate_password_hash

from forms02 import FormRegistration
from models02 import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex()
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_reg.db'
db.init_app(app)


@app.route('/')
@app.route('/index/')
def index():
    return 'Hi'


@app.route('/new_reg/', methods=['GET', 'POST'])
def new_reg():
    form = FormRegistration()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data
        hashed_password = generate_password_hash(password)
        user = User(username=name, userlastname=last_name, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('success-reg', name=name))
    return render_template('new_reg.html', form=form)


@app.route('/success_reg/<name>')
def success_reg(name):
    return render_template('okreg.html', name=name)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('Ok new-reg')


if __name__ == '__main__':
    app.run(debug=True)