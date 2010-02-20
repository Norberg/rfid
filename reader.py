import time

import rfid

while 1:
	tag = rfid.readTag()
	if len(tag) == 10:
		print tag
		time.sleep(1)
	elif len(tag) != 0:
		print "hmm.. was:", len(tag)

