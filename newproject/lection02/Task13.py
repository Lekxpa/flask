from flask import Flask, flash, redirect, request, url_for, render_template

app = Flask(__name__)
app.secret_key = b'264595d7dc61201607945cfaec8b69b9bcfe235011839e9c74a954e2815e2fd5'
"""
Генерация надежного секретного ключа
>>>import secrets
>>>secrets.token_hex()
"""

@app.route('/')
def index():
    return 'Добро пожаловать на главную страницу'

@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # обработка данных формы
        flash('ФОрма успешно отправлена', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')



if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False)



# ошибка сервера