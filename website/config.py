import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


class Config:
    #Security
    SECRET_KEY = b'F\x9e[\x8cRC\nA\x0f\xbaM\xe4,y{\x11'
    #Debug mode
    DEBUG = os.environ.get("FLASK_DEBUG", "True").lower() in ("true", "1", "t")
    #Permitted origins for CORS
    CORS_ORIGINS = os.environ.get("CORS_ORIGIN", "*")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.json.compact = False