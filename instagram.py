""" 
This tool can run in Python 3.9 or 3.10
If have errors with passwords utf-8 or proxies please contact in github
"""

import sys
import os

if sys.version_info[0] != 3:
	print("[-] Not supported for python 2 please use python 3")
	exit()

try:
	from lib.menu import menu
except ModuleNotFoundError:
	os.system('pip install -r requirements.txt')
from lib.menu import menu
from lib.src.debug.debug import Debug

if __name__ == "__main__":
	try:
		menu()
	except KeyboardInterrupt:
		Debug('[-] User interrupted', verbose=False)
		pass