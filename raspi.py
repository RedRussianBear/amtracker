import serial
import json
import urllib3
from time import sleep

data = json.load(urllib3.urlopen('http://someurl/path/to/json'))
ser = serial.Serial('/dev/tty.usbserial', 9600)

while True:
    data = json.load(urllib3.urlopen('http://someurl/path/to/json'))
    ser.write(b'1:%d' % int(data['motor0']))
    sleep(.01)
    ser.write(b'2:%d' % int(data['motor1']))
    sleep(.25)


