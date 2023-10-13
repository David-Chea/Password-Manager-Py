import colorama
from colorama import Fore, Style

import sys, subprocess

import os
os.system("cls||clear")

print(f"{Fore.LIGHTWHITE_EX}Welcome to Password Manager \n")

def clear_prompt():
    operating_system = sys.platform
    
    if operating_system == 'win32':
        subprocess.run('cls', shell=True)
        
    if operating_system == 'linux' or operating_system == 'darwin':
        subprocess.run('clear, shell=True')
        
clear_prompt()

def View():
    with open('DataPWD.txt', 'r') as f:
        for line in f.readlines():
            print(line.rstrip())

def Add():
    website = input(f"{Fore.LIGHTYELLOW_EX}Website: {Fore.LIGHTWHITE_EX}")
    email = input(f"{Fore.LIGHTYELLOW_EX}User/Email : {Fore.LIGHTWHITE_EX}")
    pwd = input(f"{Fore.LIGHTYELLOW_EX}Password: {Fore.LIGHTWHITE_EX}")
    
    print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}> Information Successfuly Saved <{Fore.LIGHTWHITE_EX}{Style.NORMAL}")
    
    with open('DataPWD.txt', 'a') as f:
        f.write("Website: " + website + " | " + "Email/User: " + email + " | " + "Password: " + pwd + "\n")

while True:
    
    mode = input(f"{Fore.LIGHTCYAN_EX}Would you like to view or add any passwords? ('a' or 'v') Quit(q) :{Fore.LIGHTWHITE_EX}").lower()
    
    if mode == "q":
        print(f"{Fore.RED}Quiting Password Manager...{Fore.LIGHTWHITE_EX}")
        quit()
    
    if mode == "v":
        View()
    elif mode == "a":
        Add()