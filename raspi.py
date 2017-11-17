import serial
import json
from urllib2 import urlopen
from time import sleep

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    data = json.load(urlopen('http://demo.mkhrenov.com/state'))
    ser.write('1:%d' % int(data['motor1']))
    print(ser.readline())
    sleep(3)
    ser.write('2:%d' % int(data['motor2']))
    print(ser.readline())
    sleep(3)

