import os
from flask_app import app
from flask import Flask, redirect, request, session, flash, url_for
from werkzeug.utils import secure_filename
from flask_app.models.part_model import Part
from flask_app.models.project_model import Project
from flask_app.models.user_model import User
from flask_app.models.profile_model import Profile

app.config['UPLOAD_FOLDER'] = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static/uploads/'))

@app.route('/Upload_part/<int:project_id>', methods=['POST'])
def upload_part(project_id):
    print('### this is the one thats important ###',project_id)
    if 'id' not in session:
        return redirect('/')
    else:
        file = request.files['part']
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        data = {
            'part': f'uploads/{filename}',
            'part_name': request.form['part_name'],
            'project_id': project_id
        }
        Part.create_part(data)
        flash('Part uploaded successfully!', 'success')
        return redirect(f'/edit_project/{project_id}')

@app.route('/delete_part/<int:part_id>')
def delete_part(part_id):
    if 'id' not in session:
        return redirect('/')
    part = Part.get_one_part({'id': part_id})
    Project.get_project_by_id({'id': part.project_id})
    Part.delete_part(part_id)
    flash("Part deleted successfully.","part")
    return redirect(f'/edit_project/{part.project_id}')
