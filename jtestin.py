import serial

ser = serial.Serial('COM4', 57600)

file = open('plane_10.dat', 'rb')
while 1: 
    byte = file.read(1)
    ser.write(byte)



