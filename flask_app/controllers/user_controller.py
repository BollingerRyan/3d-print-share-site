from flask_bcrypt import Bcrypt
from flask_app.controllers import navigation
from flask_app.models.user_model import User
from flask_app import app
bcrypt = Bcrypt(app)
from flask import render_template,redirect,request,session,flash

db = '3d_prints_db'

@app.route('/login', methods=["post"])
def log_user_in():
    data = {'email' : request.form['email']}
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Email or Password is incorrect","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Email or Password is incorrect","login")
        return redirect('/')
    session['id'] = user_in_db.id
    return redirect('/profile_page')

@app.route('/register', methods=["post"])
def Reg_new_user():
    if not User.validations(request.form):
        return redirect ('/')
    data = {
        "username" : request.form['username'],
        'email' : request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password']),
    }
    user_id = User.Reg_user(data)
    session['id'] = user_id
    return redirect('/profile_page')

@app.route('/profile_page')
def show_profile_page():
    if User.id in session == True:
        return render_template('/profile_pgae.html')