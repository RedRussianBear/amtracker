import serial
import json
from urllib2 import urlopen
from time import sleep

ser = serial.Serial('/dev/ttyACM0', 9600)
sleep(3)
dest1 = -1
dest2 = -1

while True:
    data = json.load(urlopen('http://demo.mkhrenov.com/state'))
    if dest1 != int(data['motor1']):
        ser.write('1:%d' % int(data['motor1']))
    dest1 = int(data['motor1'])
    print('1:%d' % int(data['motor1']))
    sleep(.1)
    if dest2 != int(data['motor2']):
        ser.write('2:%d' % int(data['motor2']))
    dest2 = int(data['motor2'])
    print('2:%d' % int(data['motor2']))
    sleep(1)

