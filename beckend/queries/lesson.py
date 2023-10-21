from beckend import app
from flask import render_template, request
from flask_cors import cross_origin
from ..data_base.database import get_item_by_id

TEMPLATE = 'lesson.html'

@app.route("/lesson")
# @cross_origin()
def page_lesson():
    lessons = {}

    id = 3
    cources = get_item_by_id(1)
    cources = cources.data
    cource = cources[int(id)-1]       

    lessons[1] = cource[1]  
    lessons[2] = cource[2]
    lesson = cource[3]
    lessons_name = []
    for i in range(len(lesson)):
        lessons_name.append(lesson[i][0])
    lessons[3] = lessons_name

    is_admin = True

    return render_template(TEMPLATE, lessons = lessons, is_admin = is_admin)
