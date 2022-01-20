""" 
This tool can run in Python 3.9 or 3.10
If have errors with passwords utf-8 or proxies please contact in github
"""
try:
	from lib.menu import menu
	from lib.src.debug.debug import Debug
except ImportError:
	print("Not supported for python 2 please use python 3", verbose=False)
import sys

if sys.version_info[0] != 3:
	Debug("[-] Not supported for python 2 please use python 3", verbose=False)

if __name__ == "__main__":
	try:
		menu()
	except KeyboardInterrupt:
		Debug('[-] User interrupted', verbose=False)
		pass