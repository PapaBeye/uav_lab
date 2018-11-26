import serial

#import time
gscomtopi = serial.Serial('COM5', 57600)

file = open('plane_10.dat','rb')
while True:
    data = file.read(1)
    gscomtopi.write(data)

