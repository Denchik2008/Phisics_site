from beckend import app
from flask import request, redirect, make_response, render_template
from flask_cors import cross_origin
from ..data_base.database import get_item_by_id, update_item_data




@app.route("/make_cource", methods=['GET', 'POST'])
def make_cource():
    if request.method == 'POST':
        try:
            cource_name = request.form['name']
            cource_theory = request.form['theory']
        except Exception:
            return redirect('/?error_message=Некорректные данные')

        item = get_item_by_id(1)
        cources = item.data
        cources.append([cource_name, cource_theory, ['hhh.png'], []])
        update_item_data(1, cources)

    return redirect('/')
