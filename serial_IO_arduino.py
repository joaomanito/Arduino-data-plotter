# import time
import serial  # Import PySerial package
import serial.tools
import serial.tools.list_ports

print(list(serial.tools.list_ports.comports()))

device_port = 'COM1'

ser = serial.Serial(device_port)
