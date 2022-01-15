from lib.src.file_manager import file

class Px:
	def __init__(self, proxylist):
		self.wordlist = proxylist
	def read(self):
		lines = file(self.wordlist)
		return lines
	def proxy(self):
		return self.read()
		