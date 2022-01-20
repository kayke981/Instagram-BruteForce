""" 
This tool can run in Python 3.9 or 3.10
If have errors with passwords utf-8 or proxies please contact in github
"""

from lib.menu import menu
from lib.src.debug.debug import Debug



if __name__ == "__main__":
	try:
		menu()
	except KeyboardInterrupt:
		Debug('[-] User interrupted')