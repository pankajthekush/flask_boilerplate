from posixpath import abspath
import flask_login
from flask_login import login_user, login_required, LoginManager
from app import app
from flask import Blueprint, render_template
import os
from .models import Users



login_manager = LoginManager()
login_manager.init_app(app=app)

@login_manager.user_loader
def user_loader(user_id):
    return Users.get(user_id)

api_login = Blueprint('login',__name__)


@api_login.route('/login',methods=['GET'])
def login():
    return render_template('login.html')
