from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/views')
def login():
    return render_template('index.html')