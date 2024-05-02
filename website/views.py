from flask import Blueprint, render_template, request, flash, jsonify, session
from website.db import db
from sqlalchemy.sql import text
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    current_user = session.get("user_id")
    if request.method == 'POST':
        entry_text = request.form.get('entry')
        if len(entry_text) < 1:
            flash('Entry is too short!', category='error')
        else:
            db.session.execute(text("INSERT INTO entry (data, user_id) VALUES (:entry_text, :user_id)"), 
                                {"entry_text": entry_text, "user_id": current_user})
            db.session.commit()
            flash('Entry added!', category='success')

    entries_query = db.session.execute(text("SELECT * FROM entry"))
    entries = entries_query.fetchall()

    return render_template("home.html", user=current_user, entries=entries)




@views.route('/delete-entry', methods=['POST'])
def delete_entry():
    entry = json.loads(request.data) 
    if entry and entry.get('user_id') == session.get('user_id'):
        db.session.delete(entry)
        db.session.commit()

    return jsonify({})
