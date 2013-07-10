from urllib import urlencode
import os
import time

def do_tweet (st):
	t = urlencode({'status':st})

def main():
	do_tweet ("Hello Goodmorning...!!!")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print "Ctrl-C pressed"
