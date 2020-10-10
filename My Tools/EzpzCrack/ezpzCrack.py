# !/usr/bin/python
# coding=utf-8
import requests,sys,base64,os
from colorama import Fore, Back, Style
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# Header
def header():
	SIG = headercolor('''                      
  ____ ______________________         
_/ __ \\___   /\____ \___   /         
\  ___/ /    / |  |_> >    /          
 \___  >_____ \|   __/_____ \         
     \/      \/|__|        \/         
	_________                       __    
	\_   ___ \____________    ____ |  | __
	/    \  \/\_  __ \__  \ _/ ___\|  |/ /
	\     \____|  | \// __ \\  \___|    < 
	 \______  /|__|  (____  /\___  >__|_ \
		
		\/            \/     \/     \/
        		  [Customize by H0j3n]                   
''')
    	return SIG
    	
# Color Function
def headercolor(STRING):
    return Style.BRIGHT+Fore.GREEN+STRING+Fore.RESET
    
def formatHelp(STRING):
    return Style.BRIGHT+Fore.RED+STRING+Fore.RESET
    
# Variables
LIST_CRACK = {
	"ssh" : ["aHlkcmEgIC1MIGVtYWlsLnR4dCAtUCBwYXNzd29yZC50eHQgLWYgMTAuMTAuMTAuOCBzc2ggLXMgOTk5OQo="],
	"ftp" : ["aHlkcmEgIC1MIGVtYWlsLnR4dCAtUCBwYXNzd29yZC50eHQgLWYgMTAuMTAuMTAuOCBmdHAgLXMgOTk5OQo="],
	"http" : ["d2Z1enogLXUgaHR0cDovLzEwLjEwLjEwLjgvbG9naW4ucGhwIC13IGVtYWlsLnR4dCAtZCAnZW1haWw9RlVaWiZwYXNzd29yZD1RdWljazRjYzM5NDk2JyAtLWhjIDQwMQo=","aHlkcmEgLWwgJycgLVAgcGFzc3dvcmQudHh0IDEwLjEwLjEwLjggaHR0cC1wb3N0LWZvcm0gJy9p	bmRleC5waHA6a2V5PV5QQVNTXjppbnZhbGlkIGtleScK","aHlkcmEgLWwgZm94IC1QIHBhc3N3b3JkLnR4dCAtZiAxMC4xMC4xMC44IGh0dHAtZ2V0IC8K","aHlkcmEgLWwgZm94IC1QIHBhc3N3b3JkLnR4dCAxMC4xMC4xMC44IC1zIDgwODAgaHR0cC1wb3N0LWZvcm0gJy9pbmRleC5waHA6dXNlcm5hbWU9XlVTRVJeJnBhc3N3b3JkPV5QQVNTXjpJbnZhbGlkJwo="],
	"smb" : ["aHlkcmEgLWwgZm94IC1QIHBhc3N3b3JkLnR4dCAtZiAtbSBET01BSU4gMTAuMTAuMTAuOCBzbWIK"]
}

# Main    	
if __name__ == "__main__":
	print header()
	if len(sys.argv) == 1:
		print formatHelp("(+) Usage :\t\t python %s <TYPE> " % sys.argv[0])
		print headercolor("Available Type =>\t ssh, ftp, http, smb")
		sys.exit(-1)
	OPTIONS = sys.argv[1]
	COUNTER = 0
	CHECK = True
	for i in LIST_CRACK:
			if i == OPTIONS:
				for j in LIST_CRACK[i]:
					print headercolor("[+] Example #" + str(COUNTER+1)+"\n")
					TEMP = base64.b64decode(j).decode('utf-8')
					print TEMP
					COUNTER += 1
					CHECK = False
				break
	if CHECK:
		print formatHelp("(+) Usage :\t\t python %s <TYPE> " % sys.argv[0])
		print headercolor("Available Type =>\t ssh, ftp, http, smb")
		sys.exit(-1)
