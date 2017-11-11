from flask import render_template
from amtracker import amtracker


@amtracker.route('/')
@amtracker.route('/index')
def index():
    return render_template('index.html')
