import json
import sys

class Node():
	def __init__(self, fingers, barre):
		self.fingers = fingers
		self.barre = barre
		

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
	
def print_chord(chord):
	frets = [0, 2, 2, 1, 0, 0]
	fingers = [-1, 3, 4, 1, -1, -1]
	base_fret = min((f for f in frets if f > 0))

	data = []
	
	for fret in range(base_fret, base_fret+6):
		data.append([])
		for string in range(1,7):
			if frets[string-1] == fret and fingers[string-1] != -1:
				data[fret-base_fret].append(fingers[string-1])
			else:
				data[fret-base_fret].append(-1)
	
	for i in data:
		print i
			
	1/0
	
	
	print base_fret 
	
	for j in "ADGDBe":
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
			sys.stdout.write(symbol + ("--" * int(i != 6)))
		if (j == base_fret):
			sys.stdout.write("  5")


		#sys.stdout.write("\n")
		#for i in range(0, 6):
			#if (j < 5):
				#sys.stdout.write("|" + ("  " * int(i != 5)))
	
	
	
print_chord(1)
	
