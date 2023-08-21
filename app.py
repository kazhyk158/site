from flask import Flask, render_template, request
import db
from random import shuffle

db.clear_db()
db.create()
db.insert_db()

# Создаем объект нашего приложения
app = Flask(__name__)

@app.route('/')
def index():
    '''Функция возвращает html документ
    когда мы обращаемся на главную страницу ('/') '''
    return render_template('index.html')

@app.route('/test')
def test():
    result = db.get_random_question()
    question = result[1]
    id = result[0]
    answers = [result[2], result[3], result[4] ,result[5]]
    shuffle(answers)
    return render_template(
        'test.html',
        question = question,
        answers=answers,
        id=id
    )

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        result = request.form.get('quest')
        result = result.split()
        id = result[-1]
        result.remove(result[-1])
        result = ' '.join(result)
    return render_template('result.html', correct=db.is_correct_answer(id, result))

# Если это главный файл - запусти приложение
if __name__ == "__main__":
    app.run()