# создать страницу, на которой будет форма для ввода двух чисел
# и выбор операции (сложение, вычитание, умножение или деление)
# и кнопка Вычислить
# При нажатии на кнопку будет произведено вычисление результата выбранной
# операции и переход на страницу с результатом


from flask import Flask, request, make_response, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/')
def hello_page(name=None):
    context = {
        'name': name or 'hel'
    }
    return render_template('hello.html', **context)

@app.route('/form/', methods=['GET', 'POST'])
def form_page():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        if name == "Helen" and password == 'pass':
            return redirect(url_for('hello_page', name=name))
        return render_template('task03.html', error=True)
    return render_template('task03.html', error=None)

@app.route('/inputtext/', methods=['GET', 'POST'])
def input_text():
    form = ''
    if request.method == 'POST':
        text_input = request.form.get('text')
        len_text = str(len(text_input.split()))
        print(len_text, text_input)
        return redirect(url_for('result_len', res_text=text_input, text_len=len_text))
        # return 'redirect'
        # return render_template('task04.html', error=True)
    return render_template('task04.html')

# @app.route('/resultlen/<res_text>-<text_len>')
# def result_len(res_text, text_len):
#     # html = lens
#     return f'{res_text}, {text_len}'

@app.route('/resultlen/')
def result_len():
    res_text = request.args.get('res_text')
    text_len = request.args.get('text_len')
    # html = lens
    return f'{res_text}, {text_len}'


@app.route('/inputnumb/', methods=['GET', 'POST'])
def input_numb():
    form = """
        <form method=post enctype=multipart/form-data>
        <input type="text" placeholder="Введите число 1" name="numb1"><br>
        <p><input list="math" name="option"></p>
            <datalist id="math">
            <option value='+'>+</option>
            <option value='-'>-</option>
            <option value='/'>/</option>
            <option value='*'>*</option>
            </datalist>
        <input type="text" placeholder="Введите число 2" name="numb2"><br>
        <input type="submit" value="Отправить">
        </form>
    """
    res = None

    if request.method == 'POST':
        numb_1 = int(request.form.get('numb1'))
        numb_2 = int(request.form.get('numb2'))
        if request.form.get('option') == '+':
            res = numb_1 + numb_2
        elif request.form.get('option') == '-':
            res = numb_1 - numb_2
        elif request.form.get('option') == '/':
            res = numb_1 / numb_2
        else:
            res = numb_1 * numb_2
        return redirect(url_for('res_math', res=res))
    return form
@app.route('/result/<res>/')
def res_math(res):
    return res


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False)
