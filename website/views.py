from flask import Blueprint, render_template, request, flash, redirect, session, url_for, request
from website.db import db
from sqlalchemy.sql import text


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




@views.route('/delete-entry/<int:entry_id>', methods=['POST'])
def delete_entry(entry_id):

    db.session.execute(text("DELETE FROM entry_notes WHERE id =:entry_id"), {"entry_id": entry_id})
    db.session.execute(text("DELETE FROM entry WHERE id = :entry_id"), {"entry_id": entry_id})
    db.session.commit()

    flash('Entry deleted', category='success')
    return redirect(url_for('views.home'))


@views.route('/entry/<int:entry_id>')
def entry(entry_id):
    entry = db.session.execute(text("SELECT * FROM entry WHERE id = :entry_id"), {"entry_id": entry_id}).fetchone()
    entry_notes = db.session.execute(text("SELECT * FROM entry_notes WHERE entry_id = :entry_id"), {"entry_id": entry_id}).fetchall()
    
    return render_template("entry.html", entry=entry, entry_notes=entry_notes, entry_id=entry_id)


@views.route('/add-note/<int:entry_id>', methods=['POST'])
def add_note(entry_id):
    note_text = request.form.get('note_text')
    current_user = session.get("user_id")


    file = request.files.get('file')
    filename = file.filename if file else None

    if file and filename:
        file_data = file.read()
        db.session.execute(text("INSERT INTO pictures_files (filename, file_data, user_id) VALUES (:filename, :file_data, :user_id)"),
                           {"filename":filename, "file_data":file_data, "user_id":current_user})
        db.session.commit()



    db.session.execute(text("INSERT INTO entry_notes (content, entry_id, user_id) VALUES (:content, :entry_id, :user_id)"), 
                            {"content": note_text, "entry_id": entry_id, "user_id": current_user})
    db.session.commit()
    flash('Note added!', category='success')

        
    return redirect(url_for('views.entry', entry_id=entry_id))


@views.route('/delete-note/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    db.session.execute(text("DELETE FROM entry_notes WHERE id = :note_id"), {"note_id": note_id})
    db.session.commit()

    flash('Note deleted', category='success')
    
    return redirect(request.referrer)
