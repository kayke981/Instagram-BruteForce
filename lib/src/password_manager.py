from lib.src.file_manager import file

class Pw:
	def __init__(self, wordlist):
		self.wordlist = wordlist
	def read(self):
		lines = file(self.wordlist)
		return lines
		
	def password(self):
		return self.read()
		