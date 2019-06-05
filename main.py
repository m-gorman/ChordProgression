import json
import sys

class Node():
	def __init__(self, frets, fingers, barre):
		self.frets = frets
		self.fingers = fingers
		self.barre = barre
		self.finger_chart = self.generate_finger_chart(frets, fingers)
	
	def generate_finger_chart(self, fingers, barre):
		data = []
	
		for fret in range(base_fret, base_fret+6):
			data.append([])
			for string in range(1,7):
				if frets[string-1] == fret and fingers[string-1] != -1:
					data[fret-base_fret].append(fingers[string-1])
				else:
					data[fret-base_fret].append(-1)
					
	def print_chord(self):
		base_fret = min((f for f in self.frets if f > 0))
		for j in "EADGBe":
			sys.stdout.write(j + ("  " * int(j != 'e')))
		sys.stdout.write("\n")
		for j in range(0, 6):
			sys.stdout.write("|" + ("==" * int(j != 5)))

		for j in range(base_fret, base_fret + 6):
			sys.stdout.write("\n")
			for i in range(1, 7):
				symbol = "|"
				if frets[i-1] == j and fingers[i-1] != 0:
					symbol = str(fingers[i-1])
				elif frets[i-1] == -1 and j == base_fret:
					symbol = "x"
				sys.stdout.write(symbol + ("--" * int(i != 6)))
			if (j == base_fret):
				sys.stdout.write("  " + str(base_fret))


chords = {}

data = json.loads(open("guitar.json").read())

"""for chord in data["chords"]:
	chord_info = data["chords"][chord]
	for chord_suffix in chord_info:
		suffix = chord_suffix["suffix"]
		if suffix != "major" and suffix != "minor":
			continue
		print suffix
"""
	
frets = [-1, 7, 9, 9, 9, 7]
fingers = [-1, 1, 3, 3, 3, 1]
base_fret = min((f for f in frets if f > 0))

chord = Node([-1, 7, 9, 9, 9, 7], [-1, 1, 3, 3, 3, 1], 2)

chord.print_chord()
	
