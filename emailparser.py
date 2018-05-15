#!/usr/bin/env python

import argparse
import os
import sys

# Just some colors and shit
white = '\033[1;97m'
green = '\033[1;32m'
red = '\033[1;31m'
yellow = '\033[1;33m'
end = '\033[1;m'
info = '\033[1;33m[!]\033[1;m'
que =  '\033[1;34m[?]\033[1;m'
bad = '\033[1;31m[-]\033[1;m'
good = '\033[1;32m[+]\033[1;m'
run = '\033[1;97m[~]\033[1;m'



#adding parameters
parser = argparse.ArgumentParser(description="Email Parser")
parser.add_argument('-f',help="file that contains emails",metavar="FILE")
parser.add_argument('-o',help="Path to save the results",metavar="PATH")
parser.add_argument('-i',help="Create a file for each domain and save emails in it",action = "store_true")


def main() :
	args = parser.parse_args()

	filename = args.f

	#Check if files exists
	if not os.path.exists(filename):
		print red + '[-] ' + filename + ' Does not exist' + end
		exit()

	#Check file permissions
	elif not os.access(filename,os.R_OK):
		print red + '[-] ' + filename + ' access denied' + end
		exit()

	#strip white space and Create an email list out of the inputted files.
	with open(filename,'r') as f:
		emails = [l.strip() for l in f]

	#Create a dict to store results
	results = {}

	for email in emails:

		#splitting emails to, for example "kendoclaw@example.com" will become "kendoclaw","example.com"
		name,domain = email.split("@")

		if domain in results:
			results[domain].append(email)


		else:
			results[domain] = [email]


	if args.o:

		resultfile = open(args.o,'w')

		for key,lists in results.iteritems():
			resultfile.write("################################################\n")
			resultfile.write(key + ":\n\n")


			for a in lists:
				resultfile.write(a + "\n")



	elif args.i:

		for key,lists in results.iteritems():
			domainname,bla = key.split(".")
			destfile = open(domainname+".txt",'w')


			for a in lists:
				destfile.write(a + "\n")


	print green + "Done !!" + white + " Good Bye :) " + end

try:
	main()
except:
	print red+"[-] Usage: "+white+"python "+sys.argv[0]+" -h"+ end
