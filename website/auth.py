from flask import Blueprint, render_template, request, flash, redirect, url_for
#from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
#from . import db   # para la database desde __init__.py
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route("/login", methods=["POST", "GET"])
def login():

    login_form = LoginForm()
    if login_form.validate_on_submit():
        # Buscar usuario en database
        # Loggear y validar usuario
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')

        # url_has_allowed_host_and_scheme should check if the url is safe
        # for redirects, meaning it matches the request host.

        if not url_has_allowed_host_and_scheme(next, request.host):
            return flask.abort(400)
        
        return flask.redirect(next or url_for('home'))
 
    return render_template("login.html")


@auth.route("/logout")
def logout():
    return render_template("home.html")



@auth.route("/sign-up")
def sign_up():
    return render_template("signup.html")