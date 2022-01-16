import argparse
from sys import exit
from lib.src.brute import Brute
import sys
from lib.src.const import version
import os

def parser_args():
	parser = argparse.ArgumentParser(description='Brute force instagram for hacking')
	parser.add_argument('-w', '--wordlist', type=str, help="List of passwords (ins't optional)")
	parser.add_argument('-u', '--username', type=str, help="Username of target (ins't optional)")
	parser.add_argument('-p', '--proxy', action='store_true', default=False, help='Enable proxy (is optional)')
	parser.add_argument('-pf', '--proxy-file', type=str, help='List of proxy file (is optional)')
	parser.add_argument('-d', '--delay',default=5, type=int, help='Delay between requests (default is 5)')
	parser.add_argument('-v', '--verbose', action='store_true', help='Debug log')
	parser.add_argument('--update', action='store_true', help='Update repositore')
	parser.add_argument('--version', action='store_true', help='Version')
	return parser

def menu():
	parser = parser_args()
	args = parser.parse_args()
	if args.update:
		os.system('git pull')
		sys.exit()
	if args.version:
		print(version)
		sys.exit()
	if args.wordlist is None and args.username is None:
		parser.print_help()
		sys.exit()
	delay = args.delay
	proxy = False
	verbose = False
	if args.verbose:
		verbose = True
	if args.delay is None:
		delay = 5
	if args.proxy == False:
		proxy = False
		Brute(username=args.username, wordlist=args.wordlist, timeout=delay, verbose=verbose).start()
	else:
		proxy = True
		if args.proxy_file is not None:
			Brute(username=args.username, wordlist=args.wordlist, timeout=delay, proxy=args.proxy_file, verbose=verbose).start()