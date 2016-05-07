import sys
import os
import time

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

	def whloop(self):
		m = self.pntr
		tcp = self.codePntr
		loopend = 0

		while self.mem[m] != 0:
			self.codePntr += 1
			if self.bfCode[self.codePntr] == ']':
				loopend = self.codePntr			
				self.codePntr = tcp
			else:
				self.parse(self.bfCode[self.codePntr])

		if self.mem[m] == 0:
			self.codePntr = loopend

	def parse(self, x):
		if x == '>': # Move pointer forward
			print self.pntr
			self.pntr += 1

		if x == '<': # Move pointer back
			print self.pntr
			self.pntr -= 1

		if x == '+': # Increment current byte pos by 1
			print self.mem[:10]
			self.mem[self.pntr] += 1

		if x == '-': # Deincrement current byte pos by 1
			print self.mem[:10]
			self.mem[self.pntr] += -1

		if x == '.': # Print hex value for byte pos
			#time.sleep(.2) # Makes it cool... :D
			print chr(self.mem[self.pntr]),

		if x == ',': # Get input
			i = raw_input
			self.mem[self.pntr] = i

		if x == '[':
			self.whloop()

	def start(self):
		while self.codePntr < len(self.bfCode):
			
			self.parse(self.bfCode[self.codePntr])
			self.codePntr += 1


if len(sys.argv) > 1:
	if sys.argv[1] == '-i':
		bfCode = sys.argv[2]
		BrainfuckInt(bfCode)

	else:

		bfFile = sys.argv[1]
		if os.path.isfile(bfFile):
			bfCode = list(open(bfFile).read())
			BrainfuckInt(bfCode)
		else:
			print "File '" + bfFile + "' not found..."
			exit()