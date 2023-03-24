import os
from flask_app import app
from flask import Flask, redirect, request, session, flash
from flask import send_from_directory
from werkzeug.utils import secure_filename
from flask_app.models.project_model import Project
from flask_app.models.user_model import User
from flask_app.models.profile_model import Profile

app.config['UPLOAD_FOLDER'] = 'flask_app/static/uploads/parts/'

@app.route('/create_project', methods=["POST"])
def create_project():
    data = {
        'project_name' : request.form['project_name'],
        'description' : request.form['description'],
        'users_id' : session['id']
    }
    Project.create_project(data)
    return redirect('/edit_project')

