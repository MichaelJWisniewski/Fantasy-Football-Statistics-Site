from app import app, db
from flask import render_template, redirect, flash

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html', **context)















