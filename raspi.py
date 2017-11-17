import serial
import json
from urllib.request import urlopen
from time import sleep

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    r = urlopen('http://demo.mkhrenov.com/state')
    data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
    ser.write(bytes('1:%d\n' % int(data['motor1']), 'ascii'))
    print(bytes('1:%d' % int(data['motor1']), 'ascii'))
    sleep(.01)
    ser.write(bytes('2:%d\n' % int(data['motor2']), 'ascii'))
    print(bytes('2:%d' % int(data['motor2']), 'ascii'))
    sleep(1)


