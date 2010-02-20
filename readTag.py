import pickle
import rfid

file = open("tags.dat", "rb")
tags = pickle.load(file)
print "Reading tag.."
tag = rfid.readTag()
if tags.has_key(tag):
	print tag, tags[tag]
else:
	print tag, "noname"
