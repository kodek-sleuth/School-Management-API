import jwt
import json
from flask_cors import CORS
from flask.views import MethodView
from Settings.config import app_config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, make_response, Blueprint, request

db=SQLAlchemy()

def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(app_config[config_name])
    db.init_app(app)
    CORS(app)


    from app.auth.views import admin 
    from app.pupils.views import pupil 
    from app.Bot.views import subject_bot
    from app.Bot_Results.views import results_bot

    app.register_blueprint(admin)
    app.register_blueprint(pupil)
    app.register_blueprint(subject_bot)
    app.register_blueprint(results_bot)
   
    return app



