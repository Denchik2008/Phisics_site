from beckend import app
from flask import render_template, request
from flask_cors import cross_origin
from ..data_base.database import get_item_by_id
TEMPLATE = 'task.html'

@app.route("/<cource_id>/<id>/task")
@cross_origin()
def task(cource_id, id):
    task = {}

    cources = get_item_by_id(1)
    cources = cources.data
    cource = cources[int(cource_id)-1]       
    lessons =  cource[3]
    
    task_discription = lessons[int(id)-1] #второе здание

    task[1] = task_discription[1]
    task[2] = task_discription[2]
    right_answer = task_discription[3]

    is_admin = False

    return render_template(TEMPLATE, task = task, right_answer = right_answer, is_admin = is_admin)

def return_task(cource_id, id):
    task = {}

    cources = get_item_by_id(1)
    cources = cources.data
    cource = cources[int(cource_id)-1] 
    print(cource)      
    lessons =  cource[3]
    print(lessons)
    task_discription = lessons[int(id)-1] #второе здание

    task[1] = task_discription[1]
    task[2] = task_discription[2]
    right_answer = task_discription[3]

    return task, right_answer