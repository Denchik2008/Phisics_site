from beckend import app
from flask import render_template, request
from flask_cors import cross_origin
from ..data_base.database import get_item_by_id
TEMPLATE = 'task.html'

@app.route("/task.html")
@cross_origin()
def task():
    task = {}

    cources = get_item_by_id(1)
    cources = cources.data
    cource = cources[0]       
    lessons =  cource[3]
    
    task_discription = lessons[0] #второе здание

    task[1] = task_discription[1]
    task[2] = task_discription[2]
    right_answer = task_discription[3]

    is_admin = True

    return render_template(TEMPLATE, task = task, right_answer = right_answer, is_admin = is_admin)
