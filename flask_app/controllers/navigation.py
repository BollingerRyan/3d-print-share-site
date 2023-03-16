from flask import render_template,redirect,request,session,flash
from flask_app.models.user_model import User
from flask_app import app


@app.route('/')
def show_home_page():
    return render_template('home_page.html')

@app.route('/login')
def show_login_page():
    return render_template ('/login.html')

@app.route('/register')
def show_register_page():
    return render_template('/register.html')

@app.route('/profile_page')
def show_profile_page():
    if User.id in session == True:
        return render_template('/profile_pgae.html')
    
@app.route('/create_project')
def show_create_project_page():
    if User.id in session == True:
        return render_template('/create_project.html')