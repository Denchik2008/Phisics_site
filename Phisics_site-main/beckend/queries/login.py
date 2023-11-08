from beckend import app
from flask import request, redirect, make_response, render_template
from flask_cors import cross_origin
import re

from ..data_base.database import get_item_by_id
from ..queries.courses import return_cources
from ..queries.lesson import return_lesson
from..queries.task import return_task

import smtplib
import os
from email.mime.text import MIMEText

@app.route("/<path:path>", methods=['GET', 'POST'])
def login(path):
    path = path.split('/')
    
    if path[-1] == "login" and request.method == 'POST':
        try:
            admin_nickname = request.form['nickname']
            admin_email = request.form['email']
            admin_password = request.form['psw']
        except Exception:
            return redirect('/?error_login=Некорректные_данные')

        admin = {}
        admin['admin_name'] = '1'
        admin['email'] = 'example@mail.ru'
        admin['password'] = 'example_password'
        if admin_nickname == admin['admin_name'] and admin_email == admin['email'] and admin_password == admin['password']:
            is_admin = True
        else:
            is_admin = False
    
    if path[-1] == 'letter' and request.method == 'POST':
        try:
            name = request.form['name']
            surname = request.form['surname']
            text = request.form['text']
        except:
            return redirect("/?error__reg=Некорректные_данные")
        
        sender = "d.chenchenko@student.univers.su"
        password = "Distant12357"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        try:
            server.login(sender, password)
            msg = MIMEText(text)
            msg["Subject"] = f"{name} {surname}"
            server.sendmail(sender, sender, msg.as_string())

            print("The message was sent successfully!")
        except Exception as _ex:
            print(f"{_ex}\nCheck your login or password please!")

        is_admin = False

    if len(path) == 1:
        cources = return_cources()

        return render_template('index.html', cources = cources, is_admin = is_admin)
    
    if len(path) == 2:
        lessons = return_lesson(int(path[0]))

        return render_template('lesson.html', lessons = lessons, is_admin = is_admin)

    if len(path) == 3:
        task, right_answer = return_task(int(path[0]), int(path[1]))
        
        return render_template('task.html', task = task, right_answer = right_answer, is_admin = is_admin)
    

# @app.route("/<path:path>", methods=['GET', 'POST'])
# def registration():
#     path = path.split('/')

#     if path[-1] == 'letter' and request.method == 'POST':
#         try:
#             name = request.form['name']
#             surname = request.form['surname']
#             text = request.form['text']
#         except:
#             return redirect("/?error__reg=Некорректные_данные")
        
#         sender = "d.chenchenko@student.univers.su"
#         password = "Distant12357"

#         server = smtplib.SMTP("smtp.gmail.com", 587)
#         server.starttls()

#         try:
#             server.login(sender, password)
#             msg = MIMEText(text)
#             msg["Subject"] = f"{name} {surname}"
#             server.sendmail(sender, sender, msg.as_string())

#             print("The message was sent successfully!")
#         except Exception as _ex:
#             print(f"{_ex}\nCheck your login or password please!")

    
#     if len(path) == 1:
#         return redirect(f'/')
#     if len(path) == 2:
#         return redirect(f'/{path[0]}/lesson')
#     if len(path) == 3:
#         return redirect(f'/{path[0]}/{path[1]}/task')