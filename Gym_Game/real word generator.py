from random import *
from string import *

words = ["gaysex", "semen", "fisting", "suction", "master", 'billy', 'fantasies', 'slave', 'lube', 'cum', 'anus', 'finger', 'dungeon', 'nextdoor', 'latexglove', 'van', 'weewee', 'darkholme', 'gaywebsite', 'gayporn', 'fatcock', 'dick', 'inmyass', 'bucks', 'hotloads', 'fistingass', 'balls', 'bondage']
real_word = ''
num = 0

def generate_word():
    global real_word, choosen_word, num
    word = choice(words)
    choosen_word = word
    difficulty = int(input("Choose difficulty:\n1:easy\n2:medium\n3:hard\n"))
    if difficulty == 1:
        real_word = word
    elif difficulty == 2:
        num = 10
    elif difficulty == 3:
        num = 20
    while len(word) < num:
        word += choice(ascii_lowercase)
    letter_list = list(word)
    shuffle(letter_list)
    real_word = str("".join(letter_list))

def try_word():
    win = 0
    generate_word()
    while win != 1:
        print('\nYou must do an gachi word from these letters:', '\n', real_word)
        print(choosen_word)
        trying = input()
        if trying == choosen_word:
            win = 1
        else:
            print('you must do an gachi word from  ony from these letters:', '\n', real_word)
    print('you won!')