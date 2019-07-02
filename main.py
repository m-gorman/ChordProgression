import json
import sys

class Chord():
	def __init__(self, frets, fingers):
		self.frets = frets
		self.fingers = fingers
		self.base_fret = min((f for f in frets if f > 0)) 
		self.finger_chart = self.generate_finger_chart(frets, fingers)
	
	def generate_finger_chart(self, frets, fingers):
		data = []
	
		for fret in range(self.base_fret, self.base_fret+6):
			data.append([])
			for string in range(1,7):
				if frets[string-1] == fret and fingers[string-1] != -1:
					data[fret-self.base_fret].append(fingers[string-1])
				else:
					data[fret-self.base_fret].append(-1)
					
	def print_chord(self):
		for j in "EADGBe":
			sys.stdout.write(j + ("  " * int(j != 'e')))
		sys.stdout.write("\n")
		for j in range(0, 6):
			sys.stdout.write("|" + ("==" * int(j != 5)))
		for j in range(self.base_fret-2, self.base_fret + 6):
			sys.stdout.write("\n")
			for i in range(1, 7):
				symbol = "|"
				if self.frets[i-1] == j and self.fingers[i-1] != 0:
					symbol = str(self.fingers[i-1])
				elif self.frets[i-1] == -1 and j == self.base_fret:
					symbol = "x"
				sys.stdout.write(symbol + ("--" * int(i != 6)))
			if (j == self.base_fret):
				sys.stdout.write("  " + str(self.base_fret))
				
		sys.stdout.write("\n" * 2)


chord_dict = {}

data = json.loads(open("guitar.json").read())

for chord_name in data["chords"]:
	chords = data["chords"][chord_name]
	for chord in chords:
		suffix = chord["suffix"]
		if suffix != "major" and suffix != "minor":
			continue
		name = chord_name + suffix
		for position in chord["positions"]:
			frets = position["frets"]
			fingers = position["fingers"]
			if name not in chord_dict:
				chord_dict[name] = []
			chord_dict[name].append(Chord(frets, fingers))
			
		

for chord in chord_dict["Emajor"]:
	chord.print_chord()
	
