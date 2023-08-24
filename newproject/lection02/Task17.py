from flask import Flask, session, redirect, url_for, request, make_response, render_template

app = Flask(__name__)
app.secret_key = 'ed7bdd5b880859b03fd36eaed4ea21025607a324229288684332f37b1d4f2fac'

@app.route('/')
def index():
    if 'username' in session:
        return f'Привет, {session["username"]}'
    else:
        return redirect(url_for('login'))

@app.route('/login/', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
       session['username'] = request.form.get('username') or 'NoName'
       return redirect(url_for('index'))
   return render_template('username_form.html')

@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False)
