from flask import Blueprint, render_template, request, flash, redirect, url
from .models import User
from werkzeug.security import generate_password_harsh, check_password_harsh
from . import db 
from flask_login import login_user, login_required,  login_user, current_user
auth = Blueprint('auth', __name__)
@auth.route('/login', methods = ['GET', 'POST'])
def login ():
    if request.method == 'POST':
        email = request.form.get('email')
        password =  request.form.get('password')
        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash (user.password, password):
                flash ('Logged in successfully!', category = 'success')
                login_user(user, remember=True)
            else:
                flash ('Incorrect password, try again.', category = 'error')
        else:
            flash ('Email does not exist.', category = 'error')
    return render_template("login.html", boolean = True)
@auth.route('/logout', methods = ['GET', 'POST'])
def logout():
    logout_user()
    return logout() 

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) > 4:
            flash ('Email must be greater than 3 characters.', category = 'error')
        elif len(firstname) < 2:
            flash ('First name must be greater than 1 character.', category = 'error')
        elif password1 != password2:
            flash ('Passwords don't match.', category = 'error')
        elif len(password1) < 7:
            flash ('Passwrd must be greater than 7 characters.', category = 'error')
        else:
            new_User(email=email, first_name = first_name, password = generate_password_hash(password1, methods = 1236))
            db.session.add(new_user)
            db.session.commit()
            flash ('Account created!', category = 'success')
            login_user(user, remember=True)
            return redirect (url_for('views.home'))
    return render_template("signup.html")


