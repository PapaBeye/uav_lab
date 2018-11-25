import serial

ser = serial.Serial('COM5', 57600)


while 1:
    byte = ser.read(1)
    print(byte)
