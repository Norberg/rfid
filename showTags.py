import pickle

file = open("tags.dat", "rb")
tags = pickle.load(file)
print tags
