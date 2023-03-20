from flask import render_template,redirect,request,session,flash
from flask_app.models.user_model import User
from flask_app.models.profile_model import Profile
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
    if 'id' not in session:
        return redirect ('/')
    else:
        profile = Profile.get_users_profile({'user_id': session['id']})
        user = User.get_one_user({'id':session['id']})
        print(profile)
        return render_template('/profile_page.html', user=user, profile=profile)
    
@app.route('/create_project')
def show_create_project_page():
    if 'id' not in session:
        return redirect ('/')
    else:
        return render_template('/create_project.html')
    
@app.route('/create_profile')
def show_edit_profile_page():
    if 'id' not in session:
        return redirect ('/')
    else:
        return render_template('/create_profile.html')
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')