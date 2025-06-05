from flask import render_template, request
from app import app


@app.route('/', methods=['GET', 'POST'])
def questionnaire():
    if request.method == 'POST':
        name = request.form.get('name', '')
        city = request.form.get('city', '')
        hobby = request.form.get('hobby', '')
        age = request.form.get('age', '')

        return render_template('form.html',
                               name=name,
                               city=city,
                               hobby=hobby,
                               age=age,
                               submitted=True)

    return render_template('form.html', submitted=False)