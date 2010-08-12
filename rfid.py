import serial
ser = serial.Serial(port="/dev/rfid", baudrate=2400, timeout=10)

def readTag():
	#change the value of port to the serial port the reader is connected to
	ser.open()
	ser.flushInput()
	ser.setDTR(1) #activate RFID Reader
	value = ser.read(11) #read tag
	value = value.lstrip() #remove whitespace
	ser.setDTR(0) #deactivate RFID Reader
	ser.close()
	return value
