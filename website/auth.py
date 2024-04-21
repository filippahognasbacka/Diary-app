from flask import Blueprint, render_template, request, flash, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from website.db import db
from sqlalchemy.sql import text

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        query = db.session.execute(text("SELECT * FROM users WHERE email = :email"), {"email": email})
        user = query.fetchone()

        if user:
            if check_password_hash(user.password, password):
                session["user_id"] = user.id
                print(user.id)
                flash('Logged in successfully!', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist, create an account.', category='error')

    return render_template("login.html")

@auth.route("/logout")
def logout():
    del session["user_id"]
    return redirect("/")


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        query = db.session.execute(text("SELECT * FROM users WHERE email = :email"), {"email": email})
        user = query.fetchone()

        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be grater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be grater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords must match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            hashed_password = generate_password_hash(password1)
            db.session.execute(text("INSERT INTO users (email, first_name, password) VALUES (:email, :first_name, :hashed_password)"), 
                               {"email": email, "first_name": first_name, "hashed_password": hashed_password})
            db.session.commit()
            flash('Account created! ', category='success')
            return redirect(url_for('auth.login'))
        
    return render_template("sign_up.html")
