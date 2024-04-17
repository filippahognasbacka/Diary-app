from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .db import get_db


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    db = get_db()
    if request.method == 'POST':
        review = request.form.get('review')

        if len(review) < 1:
            flash('Review is too short!', category='error')
        else:
            cursor = db.cursor()
            cursor.execute("INSERT INTO review (data, user_id) VALUES (?, ?)", (review, current_user.id))
            db.commit()
            flash('Review added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-review', methods=['POST'])

def delete_review():
    db = get_db()
    review_data = request.get_json()
    review_id = review_data['reviewId']
    cursor = db.cursor()
    cursor.execute("SELECT * FROM review WHERE id = ?", (review_id,))
    review = cursor.fetchone()
    
    if review and review[3] == current_user.id:  
        cursor.execute("DELETE FROM review WHERE id = ?", (review_id,))
        db.commit()
    return jsonify({})
