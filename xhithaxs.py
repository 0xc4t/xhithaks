import requests as req
import colorama 
from colorama import Fore
import socket
import os
import webbrowser as web

os.system ("clear")

print (Fore.GREEN ,"""" 
M""MMMM""M dP       oo   dP   M""MMMMM""MM          dP                
M  `MM'  M 88            88   M  MMMMM  MM          88                
MM.    .MM 88d888b. dP d8888P M         `M .d8888b. 88  .dP  .d8888b. 
M  .mm.  M 88'  `88 88   88   M  MMMMM  MM 88'  `88 88888"   Y8ooooo. 
M  MMMM  M 88    88 88   88   M  MMMMM  MM 88.  .88 88  `8b.       88 
M  MMMM  M dP    dP dP   dP   M  MMMMM  MM `88888P8 dP   `YP `88888P' 
MMMMMMMMMM                    MMMMMMMMMMMM                            
""")
def SimDirBrute():

    os.system ("clear")
    print (Fore.GREEN,"""
    /~~\'             |~~\ '    |~~\          |    
    `--.||/~\ /~\ |~~\|   |||/~\|--<|/~\|   |~|~/~/
    \__/||   |   ||__/|__/ ||   |__/|    \_/| | \/_
                  |                                \n
    """)
    print ("Author : VarelSecurity")
    print ("Github : github.com/varelvalensio")
    print ("example : 192.168.1.1 / example.com")
    print ("")
    url = input("masukan url : ")
    wordlists = input("masukan wordlists : ")
    print ("")
    file = open(wordlists, "r")
    line = file.readlines()
    for lines in line:
        list = lines.strip()
        r = req.get(f"{url}/{list}")
        if r.status_code ==200:
            print (Fore.BLUE,f"{url}/{list} : {r.status_code}")
        elif r.status_code ==404:
            print (Fore.RED, f"{url}/{list} : {r.status_code}")

def PortScan():
    print (Fore.GREEN,"""
    888888                   888888                  
    8    8 eeeee eeeee eeeee 8      eeee eeeee eeeee 
    8eeee8 8  88 8   8   8   8eeeee 8  8 8   8 8   8 
    88     8   8 8eee8e  8e      88 8e   8eee8 8e  8 
    88     8   8 88   8  88  e   88 88   88  8 88  8 
    88     8eee8 88   8  88  8eee88 88e8 88  8 88  8 
    """)
    print ("Author : VarelSecurity")
    print ("Github : github.com/varelvalensio")
    print ("")
    ip = input("masukan ip\t : ")
    for ports in range(1,65535):
      s = socket.socket()
      socket.setdefaulttimeout(1)
      host = s.connect_ex((ip, ports))
      s.close()
      if host ==0:
        print (Fore.BLUE, f"{ports} is open good to attack")

print ("Author : VarelSecurity")
print ("Github : github.com/varelvalensio")
print ("")
print ("[+]------------------------[+]")
print ("[1] Brute force directory")
print ("[2] Port scanner")
print ("[3] Kasih saran pembuat")
print ("[+]------------------------[+]")
pilih = input ("root@xhithaks:~# ")
if pilih =="1":
    SimDirBrute()

elif pilih =="2":
    PortScan()
elif pilih =="3":
    web.open_new("https://wa.me/6282175280152/")
