from __future__ import print_function
from colorama import Fore
from json import load
from urllib.request import urlopen
import os
import random
import sys
import time
import colorama
import string
import random
import __future__
import re
import numpy as np
import requests
import msvcrt

def freeze():
    print(f"{Fore.WHITE}Proxy{Fore.BLUE}@Dig>{Fore.BLUE} Press Enter to continue..")
    msvcrt.getch()

nds = [352, 368, 349, 355, 456]
lst = [1, 2, 3, 4, 5]
random_nds = random.choice(nds)
rdm_lst = random.choice(lst)
ndsnew = np.arange(0.0001, 0.0983, 0.0001)
ndst = np.random.choice(ndsnew)

def is_file_empty(file_path):
    return os.stat(file_path).st_size==0
def generate(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

rstring = generate(10)
while rstring[0] == ' ':
    rstring = generate(10)

file_name = "scrapped.txt"
numbers = [1, 2, 3, 4, 5]
random_number = random.choice(numbers)

def generate_random_string():
    random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(42))
    while random_string[0] == ' ':
        random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(42))
    return random_string


def main():
    global boot
    print(f"""
    
    
{Fore.BLUE}  ____                      ____  _       
{Fore.BLUE} |  _ \ _ __ ___{Fore.WHITE}__  __{Fore.BLUE}_   _|  _ \(_) __ _ 
{Fore.BLUE} | |_) | '__/ _ {Fore.WHITE}\ \/ /{Fore.BLUE} | | | | | | |/ _` |
{Fore.BLUE} |  __/| | | (_) {Fore.WHITE}>  <{Fore.BLUE}| |_| | |_| | | (_| |
{Fore.BLUE} |_|   |_|  \___{Fore.WHITE}/_/\_\{Fore.BLUE}\__, |____/|_|\__, |
{Fore.BLUE}                      |___/         |___/ 
{Fore.WHITE}
    [0] Exit
    [1] ETH Transfer
    [2] Wallet Database
{Fore.BLUE}    
    """)
    ins = input(f"{Fore.WHITE}Proxy{Fore.BLUE}@Dig>")
 
    if ins == "1":
        cpz = input(f"{Fore.WHITE}Proxy{Fore.BLUE}@Dig>{Fore.BLUE} Enter Proxy IP:Port :{Fore.BLUE}")
        match = re.match(r"^([0-9]{1,3}\.){3}[0-9]{1,3}:[0-9]{1,5}$", cpz)

        if is_file_empty(file_name):
            print(f"{Fore.WHITE}Proxy{Fore.BLUE}@Dig>{Fore.BLUE} You don't have any wallet loaded{Fore.BLUE}")
            time.sleep(2)
            boot()
    
        if match:
            print(f"{Fore.WHITE}Proxy{Fore.BLUE}@Dig>{Fore.BLUE} Connecting to Proxy :" + cpz)
            time.sleep(random_number)
            print(f"{Fore.WHITE}Proxy{Fore.BLUE}@Dig>{Fore.BLUE} Loaded Wallet : - 0x" + rstring + "################################")
            time.sleep(1)
            print(f"{Fore.WHITE}Proxy{Fore.BLUE}@Dig>{Fore.BLUE} Loading Exploit.. Could take some time")
            time.sleep(4)
            print(f"{Fore.WHITE}Proxy{Fore.BLUE}@Dig>{Fore.BLUE} Exploiting on - 0x" + rstring + "################################")
            time.sleep(1)
            print(f"{Fore.WHITE}Proxy{Fore.BLUE}@Dig>{Fore.BLUE} Using DIG Packets to force " + "- 0x" + rstring + "################################")
            time.sleep(10)
            print(f"{Fore.WHITE}Proxy{Fore.BLUE}@Dig>{Fore.BLUE} Bridge Established to DIG Server")
            time.sleep(6)
            print(f"{Fore.WHITE}Proxy{Fore.BLUE}@Dig>{Fore.BLUE} Linked DIG Script to Victim's Wallet")
            time.sleep(2)
            print(f"{Fore.WHITE}Proxy{Fore.BLUE}@Dig>{Fore.BLUE} Starting Digging, It'll take time to mine if the server is bad ")
            for rxc in range(10):
                time.sleep(1)#random_nds
                print("[+]", ndst, "| ETH - 0x" + rstring + "################################")
            print(f"{Fore.GREEN}[+]", ndst, "| ETH - 0x" + rstring + "################################")
            time.sleep(2)
            dsq = input(f"{Fore.WHITE}Proxy{Fore.BLUE}@Dig>{Fore.BLUE} Do you want to store eth ? y/n :")
            if dsq == "y":
                print(f"{Fore.WHITE}Proxy{Fore.BLUE}@Dig>{Fore.BLUE} Loading Data into Proxy Used")
                time.sleep(2)
                print(f"""{Fore.WHITE}Proxy{Fore.BLUE}@Dig> Registered as{Fore.CYAN}
[IP]:{load(urlopen('https://jsonip.com/'))['ip']}
[USERNAME]:{os.getlogin()}
[PC]:{os.getenv('COMPUTERNAME')}
[OS]:{os.getenv('OS')}
""")
                print(f"{Fore.WHITE}Proxy{Fore.BLUE}@Dig>{Fore.BLUE} SCREENSHOT YOUR INFORMATION (not the ip) SO WE CAN CHECK IT'S THE OWNER WHO WITHDRAW")
                freeze()
                boot()
            if dsq == "n":
                print(f"{Fore.WHITE}Proxy{Fore.BLUE}@Dig> Leaving ETH in wallet")
                time.sleep(2)
                boot()

            
        else:
            print("Proxy@Dig> Invalid IP:PORT")
            time.sleep(1)
            boot()

        
    if ins == "2":
        global loop
        print(f"{Fore.WHITE}Proxy{Fore.BLUE}@Dig> Scrapping Wallet From Database.. 10 max")
        time.sleep(random_number)
    def scr():
        global result
        global t
        for i in range(11):
            result = str(i)
    scr()
    time.sleep(1)
    print(f"{Fore.WHITE}Proxy{Fore.BLUE}@Dig> Saving to scrapped.txt")
    df=open('scrapped.txt','w')
    df.write(str("Proxy@Dig> //Wallet Loaded : ") + (result))
    df.write('\n')
    df.close()
    print(f"{Fore.WHITE}Proxy{Fore.BLUE}@Dig> Done.")
    time.sleep(1)
    boot()


def boot():
    os.system("cls && title ProxyDig - Premium")
    main()
        

boot()