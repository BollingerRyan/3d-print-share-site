import os
from flask_app import app
from flask import Flask, redirect, request, session
from flask import send_from_directory
from werkzeug.utils import secure_filename
from flask_app.models.user_model import User
from flask_app.models.profile_model import Profile


app.config['UPLOAD_FOLDER'] = 'flask_app/static/uploads/profile_pics/'


@app.route('/create_profile', methods=["POST"])
def create_users_profile():
    file = request.files['Pic']
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    print("file_path:", file_path)
    if not os.path.exists(file_path):
        print("File does not exist!")   
    file.save(file_path)
    data = {
        'users_id': session['id'],
        'Full_name': request.form['Full_name'],
        'Pic': f'uploads/profile_pics/{filename}',
        'description': request.form['description']
    }
    Profile.create_profile(data)
    print("create_users_profile finished!")
    return redirect('/profile_page')


@app.route('/update_profile', methods=["POST"])
def update_users_profile():
    file = request.files['Pic']
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    print("file_path:", file_path)
    if not os.path.exists(file_path):
        print("File does not exist!")
    file.save(file_path)
    data = {
        'users_id': session['id'],
        'Full_name': request.form['Full_name'],
        'Pic': f'uploads/profile_pics/{filename}',
        'description': request.form['description']
    }
    Profile.update_users_profile(data)
    return redirect('/profile_page')

@app.route('/uploads/profile_pics/<filename>')
def serve_profile_pic(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)





