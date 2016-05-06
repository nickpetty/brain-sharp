import sys
import os

class BrainfuckInt:
	
	def __init__(self, code):
		self.bfStatements = ['>', '<', '+', '-', '.', ',', '[', ']']
		self.mem = [0] * 300
		self.pntr = 0
		self.tmpPntr = 0
		self.codePntr = 0		
		self.bfCode = self.clrCmnts(code)
		self.start()
		
	def clrCmnts(self, code):
		temp = []
		for x in code:
			if x in self.bfStatements:
				temp.append(x)
		return temp

	def parse(self, x):
		if x == '>': # Move pointer forward
			self.pntr += 1

		if x == '<': # Move pointer back
			self.pntr -= 1

		if x == '+': # Increment current byte pos by 1
			self.mem[self.pntr] += 1

		if x == '-': # Deincrement current byte pos by 1
			self.mem[self.pntr] -= 1

		if x == '.': # Print hex value for byte pos
			print chr(self.mem[self.pntr])

		if x == ',': # Get input
			i = raw_input
			self.mem[self.pntr] = i

		if x == '[': # Begin while loop
			self.tmpPntr = self.pntr
			self.codePntr += 1
			eol = int
			tcp = self.codePntr

			while self.mem[self.tmpPntr] != 0:
				i = self.bfCode[self.codePntr]
				
				if i == ']':
					self.codePntr = tcp
				
				self.parse(i)
				self.codePntr += 1
		
	def start(self):
		while self.codePntr < len(self.bfCode):
			self.parse(self.bfCode[self.codePntr])
			self.codePntr += 1

if len(sys.argv) > 1:
	bfFile = sys.argv[1]
	if os.path.isfile(bfFile):
		bfCode = list(open(bfFile).read())
		BrainfuckInt(bfCode)
	else:
		print "File '" + bfFile + "' not found..."
		exit()