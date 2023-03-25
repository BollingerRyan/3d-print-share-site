import os
from flask_app import app
from flask import Flask, redirect, request, session, flash, url_for
from werkzeug.utils import secure_filename
from flask_app.models.part_model import Part
from flask_app.models.project_model import Project
from flask_app.models.user_model import User
from flask_app.models.profile_model import Profile

app.config['UPLOAD_FOLDER'] = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static/uploads/parts'))

@app.route('/Upload_part', methods=['POST'])
def upload_part():
    if 'id' not in session:
        return redirect('/')
    else:
        project = Project.get_project_by_users_id({'users_id':session['id']})
        file = request.files['part']
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        data = {
            'part': filename,
            'part_name': request.form['part_name'],
            'project_id': project.id
        }
        Part.create_part(data)
        flash('Part uploaded successfully!', 'success')
        return redirect('/edit_project')