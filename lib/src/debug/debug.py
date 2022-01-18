from lib.src.debug.colors import colors
import logging
class Debug:
	def __init__(self, message, verbose = False):
		self.message = message
		self.verbose = verbose
		if verbose == False:
			self.pprint()
		else:
			self.verboseLog()
			if '[*]' in self.message:
				logging.info(colors.blue + message.replace('[*] ', '') + colors.reset)
			if '[+]' in self.message:
				logging.info(colors.green + message.replace('[+] ', '') + colors.reset)
			if '[-]' in self.message:
				logging.error(colors.red + message.replace('[-] ', '') + colors.reset)
			if '[!]' in self.message:
				logging.warning(colors.yellow + message.replace('[!] ', '') + colors.reset)
	def pprint(self):
		self.colors()
	def consoleColor(self, color, message):
		msg = "%s%s%s" % (color, self.message, colors.reset)
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
	def verboseLog(self):
		logging.basicConfig(format=f"[{colors.cyan}%(asctime)s{colors.reset}][{colors.pink}%(levelname)s{colors.reset}] %(message)s", datefmt="%H:%M:%S", level=logging.DEBUG)