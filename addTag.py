import sys, pickle, os.path
import rfid

if len(sys.argv) == 2:
	name = sys.argv[1]
else:
	name = raw_input("Name of tag:")
print "reading tag.."
tag = rfid.readTag()
if len(tag) != 10:
	print "No tag provided!"
	exit()

tags = {}
if os.path.isfile("tags.dat"):
	file = open("tags.dat", "rb")
	tags = pickle.load(file)
	file.close()

if tags.has_key(tag):
	answer = raw_input("Tag allready present, do you want to update i y/N?")
	if answer != "y" and answer != "Y":
		print "didnt update tag"
		exit()
#name allredy pressent
for key, value in tags.iteritems():
	if value == name: 
		answer = raw_input("Name allready present, do you wish to have"+
				" mulitple tags with this name y/N or do you " +
				" want to (r)eplace previus tag?")
		if answer in ("r", "R"):
			del(tags[key])
			break	
		elif answer != "y" and answer != "Y":
			print "didnt update tag"
			exit()
tags[tag] = name
print "tags before dump:", tags
file = open("tags.dat", "wb")
pickle.dump(tags, file)
file.close()
print "Written 1 tag to database of", len(tags), "tags."
