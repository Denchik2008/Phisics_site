from beckend import app
from flask import request, redirect, make_response, render_template
from flask_cors import cross_origin
import re

# from .__help__ import send_simple_query, login_user, logout_user, get_user

'''
    /login          login()             Вход пользователя.
    /logout         logout()            Выход пользователя.
'''


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            user_login = request.form['login']
            user_password = request.form['psw']
        except Exception:
            return redirect('/?error_login=Некорректные данные')

        data = {'password': user_password, 'login': user_login}
        print(data)


    return redirect('/')


@app.route("/logout")
@cross_origin()
def logout():
    resp = make_response(redirect('/'))
    # logout_user(resp)
    return resp


@app.route('/registration', methods=['POST'])
def registration():
    if request.method == 'POST':
        try:
            login = request.form['login']
            email = request.form['email']
            name = request.form['name']
            psw1 = request.form['psw1']
            psw2 = request.form['psw2']
        except:
            return "/?error__reg=Некорректные данные"

        if psw1!=psw2:
            return "/?error__reg=Пароли не совпадают"
        
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if not re.fullmatch(regex, email):
            return "/?error__reg=Некоректная почта"
        
        return redirect('/')

