import serial

def readTag():
	#change the value of port to the serial port the reader is connected to
	ser = serial.Serial(port="/dev/ttyUSB2", baudrate=2400, timeout=10)
	ser.open()
	ser.flushInput()
	ser.setRTS(1) #activate RFID Reader
	value = ser.read(11) #read tag
	value = value.lstrip() #remove whitespace
	ser.setRTS(0) #deactivate RFID Reader
	ser.close()
	return value
