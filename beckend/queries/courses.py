from beckend import app
from flask import render_template, request
from flask_cors import cross_origin
from ..data_base.database import get_item_by_id

TEMPLATE = 'index.html'


@app.route("/")
@app.route("/courses")
@cross_origin()
def courses():
    courses = {}

    cources = get_item_by_id(1)
    cources = cources.data
    for i in range(len(cources)):
        courses[i+1] = {'name' : cources[i][0]}
    return render_template(TEMPLATE, cources = courses, is_admin = True)
