from beckend import app
from flask import request, redirect, make_response, render_template
from flask_cors import cross_origin
from ..data_base.database import get_item_by_id, update_item_data

@app.route("/<cource_id>/<id>/fix_task", methods=['GET', 'POST'])
def fix_task(cource_id, id):
    if request.method == 'POST':
        try:
            fix_task_name = request.form['name']
            fix_task_theory = request.form['theory']
            fix_task_right_answer = request.form['right_answer']

            print(cource_id, id)

            item = get_item_by_id(1)
            cources = item.data
            cource_id = int(cource_id)-1 #курс на котором я сейчас нахожусь
            task_id = int(id)-1 #задание на котором я сейчас нахожусь
            

            cources[cource_id][3][task_id][0] = fix_task_name
            cources[cource_id][3][task_id][1] = fix_task_theory
            cources[cource_id][3][task_id][3] = fix_task_right_answer

            update_item_data(1, cources)

        except Exception:
            return redirect('/?error_message=Некорректные данные')

        data = {'name': fix_task_name, 'theory': fix_task_theory, 'right_answer': fix_task_right_answer}
        print(data)


    return redirect(f'/{cource_id+1}/{id}/task')


TEMPLATE = 'fix_task.html'

@app.route("/<cource_id>/<id>/fix_tasks")
@cross_origin()
def update_task(cource_id, id):
    item = get_item_by_id(1)
    cources = item.data
    cource_id = int(cource_id) - 1 #курс на котором ты сейчас находишься
    cource = cources[cource_id]
    task_id = int(id) - 1 #задание на котором ты сейчас находишься
    tasks = cource[3]
    task = tasks[task_id]

    task_name = task[0]
    task_text = task[1]
    task_right_answer = task[3]
    return render_template(TEMPLATE, task_name = task_name, task_text = task_text, task_right_answer = task_right_answer, cource_id = cource_id+1, id = id)


