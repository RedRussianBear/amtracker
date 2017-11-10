from flask import render_template
from amtracker import amtracker


@amtracker.route('/')
@amtracker.route('/index')
def index():
    alumni = [{'name': 'Kalin', 'city': 'College Park', 'class': 2016},
              {'name': 'Ethan', 'city': 'New York', 'class': 2017}]
    return render_template('index.html', alumni=alumni)
