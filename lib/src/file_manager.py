from lib.src.debug.debug import Debug
import sys

def file(path_to_file):
	try:
		with open(path_to_file) as file:
			lines = file.readlines()
			linesW = [line.rstrip() for line in lines]
			return lines
	except:
		Debug(f'[-] File {path_to_file} not found', verbose=False)
		sys.exit()
		pass