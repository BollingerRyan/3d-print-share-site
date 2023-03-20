import os
from flask_app import app
from flask import Flask, render_template, redirect, request, session, flash
from flask import send_from_directory
from werkzeug.utils import secure_filename
from flask_app.models.user_model import User
from flask_app.models.profile_model import Profile

app.config['UPLOAD_FOLDER'] = 'static/uploads/profile_pics'

@app.route('/create_profile', methods=["POST"])
def create_users_profile():
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    print("create_users_profile called!")
    data = {
        'users_id': session['id'],
        'Full_name': request.form['Full_name'],
        'description': request.form['description']
    }
    if 'Pic' in request.files:
        image_file = request.files['Pic']
        if image_file.filename != '':
            filename = secure_filename(image_file.filename)
            image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            data['Pic'] = os.path.join('uploads/profile_pics', filename)
        else:
            data['Pic'] = None
    else:
        data['Pic'] = None
    Profile.create_profile(data)
    print("create_users_profile finished!")
    return redirect('/profile_page')

@app.route('/profile_pics/<filename>')
def serve_profile_pic(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)






