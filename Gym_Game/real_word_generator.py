from random import *
from string import *
from random import randint as rnd

min_num = 0
max_num = 0
minidamage = 0

def equation():
    global mini_damage, max_num, min_num
    difficulty = int(input("Choose difficulty:\n1:easy\n2:medium\n3:hard\n"))
    if difficulty == 1:
        mini_damage = 10
        min_num = 1
        max_num = 500
    elif difficulty == 2:
        mini_damage = 25
        max_num = 1000
        min_num = 500
    elif difficulty == 3:
        mini_damage = 50
        max_num = 1500
        min_num = 1000
    else:
        equation()
    mini_ecuation = str(rnd(min_num, max_num))