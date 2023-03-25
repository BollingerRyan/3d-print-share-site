from flask_app import app
from flask import Flask, redirect, request, session, flash
from flask_app.models.project_model import Project

@app.route('/create_project', methods=["POST"])
def create_project():
    if not Project.validations:
        return redirect('/create_project')
    else:
        data = {
            'project_name' : request.form['project_name'],
            'description' : request.form['description'],
            'users_id' : session['id']
        }
        Project.create_project(data)
        return redirect('/edit_project')
