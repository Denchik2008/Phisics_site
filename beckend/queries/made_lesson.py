from beckend import app
from flask import request, redirect, make_response, render_template
from flask_cors import cross_origin
from ..data_base.database import get_item_by_id, update_item_data


@app.route("/make_lesson", methods=['GET', 'POST'])
def make_lesson():
    if request.method == 'POST':
        try:
            lesson_name = request.form['name']
            lesson_theory = request.form['theory']
            right_answer = request.form['right_answer']
        except Exception:
            return redirect('/?error_message=Некорректные данные')

        item = get_item_by_id(1)
        cources = item.data
        cource_id = 2 #индекс курса на котором мы находимся
        cources[cource_id][3].append([lesson_name, lesson_theory, ['hhh.png'], right_answer])

        update_item_data(1, cources)


    return redirect('lesson')

