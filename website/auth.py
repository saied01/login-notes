from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   # para la database desde __init__.py
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from .config import LoginForm


auth = Blueprint('auth', __name__)


@auth.route("/login", methods=["POST", "GET"])
def login():

    form = LoginForm() # WTForms to validate using flask

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            flash('successfully loggged in.', category='success')
            print('user logged')
            login_user(user, remember=True)
            return redirect(url_for('views.home'))

        else:
            flash('Incorrect Email or password, try again', category='error')

    return render_template("login.html", user=current_user, form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))



@auth.route("/sign-up", methods=['POST', 'GET'])
def sign_up():

    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        first_name = request.form.get('first_name')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 5:
            flash('Email must be at least 5 characters long.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(first_name) < 2:
            flash('Name must be at least 2 characters long.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 5 characters long.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()

            flash('Account created!', category='success')
            return redirect(url_for('views.home'))



    return render_template("signup.html", user=current_user)