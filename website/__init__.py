from flask import Flask
from dotenv import load_dotenv
import os
import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from .db import db


load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

from .views import views
from .auth import auth

app.register_blueprint(views, url_prefix='/') 
app.register_blueprint(auth, url_prefix='/') 

db.init_app(app)




