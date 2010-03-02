#!/usr/bin/python

import time, pickle

import rfid, tagActions

file = open("tags.dat", "rb")
tags = pickle.load(file)

while 1:
	tag = rfid.readTag()
	if len(tag) == 10:
		if tags.has_key(tag):
			try:
				tagActions.__getattribute__(tags[tag])()
			except AttributeError:
				print "Function for action", tags[tag], \
				       "not declared"
		else:
			print tag, "was not found tags.dat"
		time.sleep(1)
	elif len(tag) != 0:
		print "hmm.. was:", len(tag)
