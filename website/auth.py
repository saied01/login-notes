from flask import Blueprint, render_template, request, flash, redirect, url_for
#from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
#from . import db   # para la database desde __init__.py
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route("/login")
def login():

    return render_template("login.html")


@auth.route("/logout")
def logout():
    return render_template("home.html")



@auth.route("/sign-up")
def sign_up():
    return render_template("signup.html")