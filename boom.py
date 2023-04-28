# -*- coding: utf-8 -*-

import time
import os
import subprocess

subprocess.check_output('sudo apt update',shell=True)

try:
    check_net_tools = subprocess.check_output('dpkg -s net-tools', shell=True)
    if str('install ok installed') in str(check_net_tools):
        pass
except subprocess.CalledProcessError:
    print('[+] net-tools not installed. installing...')    
    subprocess.check_output('sudo apt install net-tools -y', shell=True)
    print('[!] net-tools installed succesfully')

try:
    check_iptables = subprocess.check_output('dpkg -s iptables', shell=True)
    if str('install ok installed') in str(check_iptables ):
        pass
except subprocess.CalledProcessError:
    print('[+] iptables not installed. installing...')
    subprocess.check_output('sudo apt install iptables -y', shell=True)
    print('[!] iptables installed succesfully')

try:
    check_pip3 = subprocess.check_output('dpkg -s python3-pip', shell=True)
    if str('install ok installed') in str(check_pip3):
        pass
except subprocess.CalledProcessError:
    print('[+] pip3 not installed. installing...')
    subprocess.check_output('sudo apt install python3-pip -y', shell=True)
    print('[!] pip3 installed succesfully')

try:
    import requests
except Exception:
    print('[+] python3 requests is not installed. installing...')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('[!] python3 requests is installed ')
    
try:
    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:

    print('[+] tor is not installed. installing...')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install tor -y',shell=True)
    print('[!] tor is installed succesfully ')
    
try:
    check_anonym8 = subprocess.check_output('which anonym8', shell=True)
    
    if check_anonym8 == 'anonym8 not found':
        print('[+] anonym8 is not installed. installing...')        
        subprocess.check_output('sudo bash install_anonym8.sh',shell=True)
        print('[!] anonym8 is installed succesfully ')    
    
except subprocess.CalledProcessError:
    print('[+] anonym8 is not installed !')
    subprocess.check_output('sudo bash install_anonym8.sh',shell=True)
    print('[!] anonym8 is installed succesfully ') 

os.system("clear")

def change():
    os.system("anonym8 change")
    os.system("anonym8 start_mac")
    os.system("service tor reload")    
    print ('[+] Your IP has been Changed .')

print('''\033[1;32;40m \n
 
██╗██████╗░███████╗███╗░░██╗████████╗██╗████████╗██╗░░░██╗  ██████╗░░█████╗░░█████╗░███╗░░░███╗
██║██╔══██╗██╔════╝████╗░██║╚══██╔══╝██║╚══██╔══╝╚██╗░██╔╝  ██╔══██╗██╔══██╗██╔══██╗████╗░████║
██║██║░░██║█████╗░░██╔██╗██║░░░██║░░░██║░░░██║░░░░╚████╔╝░  ██████╦╝██║░░██║██║░░██║██╔████╔██║
██║██║░░██║██╔══╝░░██║╚████║░░░██║░░░██║░░░██║░░░░░╚██╔╝░░  ██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║
██║██████╔╝███████╗██║░╚███║░░░██║░░░██║░░░██║░░░░░░██║░░░  ██████╦╝╚█████╔╝╚█████╔╝██║░╚═╝░██║
╚═╝╚═════╝░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░░╚═╝░░░░░░╚═╝░░░  ╚═════╝░░╚════╝░░╚════╝░╚═╝░░░░░╚═╝
        									   t1r4x @ V 1.0
from \033[1;40;31m http://johseffer.com.br/\n''')

os.system("service tor start")
os.system("anonym8 start")

time.sleep(3)
print("\033[1;32;40m change your  SOCKES to 127.0.0.1:9050 \n")
os.system("service tor start")
x = input("[+] time to change Ip in Sec [type=60] >> ")
lin = input("[+] how many time do you want to change your ip [type=1000]for infinte ip change type [0] >>")
if int(lin) ==int(0):

	while True:
		try:
			time.sleep(int(x))
			change()
		except KeyboardInterrupt:

		 	print('\nidentity boom is closed ')
		 	quit()

else:
	for i in range(int(lin)):
		    time.sleep(int(x))
		    change()
