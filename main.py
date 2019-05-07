import json

class Node():
	def __init__(self, fingers, barre):
		self.fingers = fingers
		self.barre = barre
		

data = json.loads(open("guitar.json").read())

print data["chords"]