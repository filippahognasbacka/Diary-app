from flask import Blueprint, render_template, request, flash, jsonify, session
from website.db import db
from sqlalchemy.sql import text

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    current_user = session.get("user_id")
    if request.method == 'POST':
        review = request.form.get('review')
        if len(review) < 1:
            flash('Review is too short!', category='error')
        else:
            db.session.execute(text("INSERT INTO review (data, user_id) VALUES (:review, :user_id)"), 
                               {"review": review, "user_id": current_user})
            db.session.commit()
            flash('Review added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-review', methods=['POST'])
def delete_review():
    current_user = session["user_id"]
    review_data = request.get_json()
    review_id = review_data['reviewId']
    

    cursor = db.cursor()
    cursor.execute("SELECT * FROM review WHERE id = %s AND user_id = %s", (review_id, current_user))
    review = cursor.fetchone()
    
    if review:
        cursor.execute("DELETE FROM review WHERE id = %s", (review_id,))
        db.commit()
    
    return jsonify({})

