from flask_app import app
from flask_app.controllers import navigation
from flask_app.models.user_model import User
from flask import render_template,redirect,request,session,flash

db = '3d_prints_db'

@app.route('/edit_profile')
def edit_users_profile():
    data = {

        'picture': request.form['picture'],
        'full name' : request.form['full name'],
        'description' : request.form['description']
    }


