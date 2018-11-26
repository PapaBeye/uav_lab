import serial
gscomtopi = serial.Serial('COM7', 57600)

while True:
    if gscomtopi.inWaiting() > 0:
        data = gscomtopi.readline()
        data = data.decode()
        data = data.replace('-', '\n')
        print(data)
    



