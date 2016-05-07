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

	def debug(self):
		print str(self.mem[0]) + '|' + str(self.mem[1]) + '|' + str(self.mem[2]) + '|' + str(self.mem[3]) + '|' + str(self.mem[4]) + '|' + str(self.mem[5]) + '|' + str(self.mem[6])

	def parse(self, x):
		if x == '>': # Move pointer forward
			self.pntr += 1

		if x == '<': # Move pointer back
			#print 'called'
			self.pntr -= 1

		if x == '+': # Increment current byte pos by 1
			#self.debug()
			self.mem[self.pntr] += 1

		if x == '-': # Deincrement current byte pos by 1
			#self.debug()
			#print self.mem[self.pntr]
			self.mem[self.pntr] += -1
			#print self.mem[self.pntr]

		if x == '.': # Print hex value for byte pos
			print chr(self.mem[self.pntr])

		if x == ',': # Get input
			i = raw_input
			self.mem[self.pntr] = i

		if x == '[':
			m = self.pntr
			tcp = self.codePntr
			loopend = int

			while self.mem[m] != 0:
				self.codePntr += 1
				if self.bfCode[self.codePntr] == ']':
					loopend = self.codePntr			
					self.codePntr = tcp
				else:
					self.parse(self.bfCode[self.codePntr])

			if self.mem[m] == 0:
				#print 'loopend'
				self.codePntr = loopend

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