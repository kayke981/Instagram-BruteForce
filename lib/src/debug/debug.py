from lib.src.debug.colors import colors

class Debug:
	def __init__(self, message):
		self.message = message
		self.pprint()
	def pprint(self):
		self.colors()
	def consoleColor(self, color, message):
		msg = "%s%s %s" % (color, self.message, colors.reset)
		print(msg)
	def colors(self):
		if '[*]' in self.message:
			self.consoleColor(colors.blue, self.message)
		elif '[!]' in self.message:
			self.consoleColor(colors.yellow, self.message)
		elif '[+]' in self.message:
			self.consoleColor(colors.green, self.message)
		elif '[-]' in self.message:
			self.consoleColor(colors.red, self.message)
		elif '[CRITICAL]'.lower() in self.message.lower():
			self.consoleColor(colors.critical, self.message)