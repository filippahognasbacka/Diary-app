from flask import Flask
from flask_login import LoginManager
from dotenv import load_dotenv
import os
import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from website.db import get_db


load_dotenv()



app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    
from .views import views
from .auth import auth

app.register_blueprint(views, url_prefix='/') 
app.register_blueprint(auth, url_prefix='/') 

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    if user:
        return user 




