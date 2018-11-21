import sys
import VACSParser
import time

if len(sys.argv) != 3:
    print("Usage: python SerialReadTest.py serial-port-path message-definition-path")
    sys.exit(1)

serial_port_path = sys.argv[1]
message_definition_path = sys.argv[2]
file = open(str(serial_port_path), 'br')

#serial_port = serial.Serial(serial_port_path, 57600)

parser = VACSParser.Parser(message_definition_path)

while True:

    #serial_byte = serial_port.read(1)
    file_byte = file.read(1)

    if file_byte:#serial_byte:

        parser.parse(file_byte)

        new_packet = parser.get_packet()

        if new_packet:
            for i in new_packet.message:
                if i == 'position/longitude':
                    print(len(i))
                    print("Longitube: "+str(new_packet.message[i]))
                elif i == 'position/latitude':
                    print(len(i))
                    print("Latitude: "+str(new_packet.message[i]))
                elif i == 'position/altitude':
                    print(len(i))
                    print("Altitude: "+str(new_packet.message[i]))
                else:
                    print(len(i))




