from beckend import app
from flask import request, redirect, make_response, render_template
from flask_cors import cross_origin

from ..data_base.database import get_item_by_id, update_item_data
from ..queries.lesson import return_lesson


@app.route("/<id>/fix_lesson_theory", methods=['GET', 'POST'])
def fix_lesson_theory(id):
    if request.method == 'POST':
        try:
            fix_lesson_name = request.form['name']
            fix_lesson_theory = request.form['theory']

            item = get_item_by_id(1)
            cources = item.data
            cource_id = int(id)-1 #id курса на котором я нахожусь
            cources[cource_id][0] = fix_lesson_name
            cources[cource_id][1] = fix_lesson_theory

            update_item_data(1, cources)

        except Exception:
            return redirect('/?error_message=Некорректные данные')

        data = {'name': fix_lesson_name, 'theory': fix_lesson_theory}
        print(data)

        lessons = return_lesson(int(id))
        return render_template('lesson.html', lessons = lessons, is_admin = True)

TEMPLATE = 'fix_lesson_theory.html'

@app.route("/<id>/fix_lesson")
@cross_origin()
def fix_lesson(id):
    item = get_item_by_id(1)
    cources = item.data
    cource_id = int(id) - 1 #айди курса в котором ты находишься
    cource = cources[cource_id]
    cource_name = cource[0]
    lesson_theory = cource[1]

    return render_template(TEMPLATE, cource_name = cource_name, lesson_theory = lesson_theory, id = id)
