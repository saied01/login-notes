import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

DB_NAME = "database.db"

class Config:
    #Security
    SECRET_KEY = '1f21d71cf705fe60e192f45b6bf419b8efa0281b570db0d35f833f4551852cf6'
    #Debug mode
    DEBUG = os.environ.get("FLASK_DEBUG", "True").lower() in ("true", "1", "t")
    #Permitted origins for CORS
    CORS_ORIGINS = os.environ.get("CORS_ORIGIN", "*")
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False



class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Login")