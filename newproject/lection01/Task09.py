from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'

@app.route('/for/')
def show_for():
    context = {'title': 'цикл',
               'poem': ['Helen',
                        'fjklj lj',
                        'fklj jklkj flkj',
                        ]}
    # txt = """<h1>Стихотворение</h1>\n<p>""" + '<br/>.join(poem) + '</p>'
    return render_template('show_for.html', ** context)


if __name__ == '__main__':
    app.run(debug=True)