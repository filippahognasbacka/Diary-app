import sqlite3
from flask import Flask
import os

DB_NAME = "database.db"

def get_db():
    db = getattr(Flask, '_database', None)
    if db is None:
        db = Flask._database = sqlite3.connect(DB_NAME)
    return db

def close_db(e=None):
    db = getattr(Flask, '_database', None)
    if db is not None:
        db.close()

def init_db(app):
    with app.app_context():
        db = get_db(app)
        schema_path = "website/schema.sql"
        with open(schema_path, mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
