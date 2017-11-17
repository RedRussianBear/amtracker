import serial
import json
from urllib.request import urlopen
from time import sleep

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    r = urlopen('http://demo.mkhrenov.com/state')
    data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
    ser.write(b'1:%d' % int(data['motor1']))
    sleep(.01)
    ser.write(b'2:%d' % int(data['motor2']))
    sleep(.25)


