from flask import render_template, request, jsonify
from amtracker import amtracker

motor_states = {'motor1': 0, 'motor2': 0}


@amtracker.route('/', methods=['POST', 'GET'])
@amtracker.route('/index')
def index():
    return render_template('index.html')


@amtracker.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        motor_states['motor1'] = int(request.form['motor1'])
        motor_states['motor2'] = int(request.form['motor2'])
        print(request.form)
    return 'Good!'


@amtracker.route('/state')
def state():
    return jsonify(motor_states)
