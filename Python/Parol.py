#TODO: mem&cpu tracker
import string
from time import sleep, time
from colorama import Fore, Back, Style
logged = False
letters = list(string.printable)
ll = len(letters) - 1
attempts = list()
password = input("input password") # max 16 char.
counter = 0
a = list(string.printable)

def login(a):
    if a == password:
        logged = True
        if counter > 10:
            print(f"Logged In -- {counter} attemps lol unlucky лох")
        else:
            print(Back.GREEN, f"Logged In -- {counter} >:)", Style.RESET_ALL)
        end = time()
        print(f'{end-start}s')
        quit()
    else:
        print(Fore.RED + "Wrong idiot" + Fore.WHITE)

start = time()
while logged is False:
    for i in letters:
        sleep(0.1)
        print(i)
        login(i)
        attempts.append(i)
        print(attempts)
        i += i
        counter += 1
        if counter == 100:
            counter = 0
            i = letters + a