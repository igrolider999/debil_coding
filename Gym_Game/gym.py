from time import sleep
from colorama import Fore, Back, Style
from random import *
from random import randint as rnd
from string import *
from sympy import limit
from threading import Timer
import sqlite3

##############
connection = sqlite3.connect("Gym_Game/game_stats.db")
cursor = connection.cursor()

##############

home_choice = 0
words = ["gaysex", "semen", "fisting", "suction", "master", 'billy', 'fantasies', 'slave', 'lube', 'cum', 'anus', 'finger', 'dungeon', 'nextdoor', 'latexglove', 'van', 'weewee', 'darkholme', 'gaywebsite', 'gayporn', 'fatcock', 'dick', 'inmyass', 'bucks', 'hotloads', 'fistingass', 'balls', 'bondage']
real_word = ''
num = 0

class Player:
    cum = int(100)  # hp
    max_cum = 100  # max hp
    bucks = 1000  # money
    damage = [0, 1]  # strength
    aim = 1
    anus_tightness = 1
    lungs = 1
    sucked = 0
    next_enemy = 1
    day = 0
    day_in_apartment = 0
    months_in_apartment = 1
    player_has_apartment = True
    days_at_home = 0

class Enemies:
    class fucking_slave:
        name = "Fucking Slave"
        cum = 100
        max_cum = 100
        damage = [1, 2]
        lvl = 1
        anus_tightness = 5
        aim = 5
        is_defeated = False

    class dungeon_master:
        name = "Darkholme"
        cum = 500
        max_cum = 500
        damage = [1, 10]
        lvl = 15
        anus_tightness = 15
        aim = 20
        is_defeated = False

    class Leatherman:
        name = "Leatherman"
        cum = 3000
        max_cum = 3000
        damage = [10, 20]
        lvl = 50
        anus_tightness = 25
        aim = 30
        is_defeated = False

    class Uncle_Bogdan:
        name = "Bogdan"
        cum = 1000
        max_cum = 1000
        damage = [40, 75]
        lvl = 100
        anus_tightness = 55
        aim = 50
        is_defeated = False

    class Billy:
        name = 'Billy'
        cum = 1000
        max_cum = 10000
        damage = [50, 100]
        lvl = 1000
        anus_tightness = 90
        aim = 100
        is_defeated = False

class functions:
    aboba = {1: Enemies.fucking_slave, 2: Enemies.dungeon_master , 3: Enemies.Leatherman, 4: Enemies.Uncle_Bogdan,5: Enemies.Billy}

next_enemy_stats = functions.aboba[Player.next_enemy]
# left_enemies = list(dungeon_master, fucking_slave, Billy, Van, Uncle_bogdan)

def fisting():
    global next_enemy, next_enemy_stats
    if Player.bucks >= 300:
        enemy_choose = int(input("\n Choose your enemy\n1:fucking slave\n2:dungeon master\n3:Leatherman\n4:Uncle Bogdan\n5:Billy"))
        if enemy_choose > next_enemy:
            print(Fore.MAGENTA, '\nYou are too weak for him. Try someone else', Style.RESET_ALL)
            fisting()
        enemy = functions.aboba[enemy_choose]
        print("\n", enemy.name)

        # fisting / attack functions
        def player_attack():
            player_damage = (rnd(Player.damage[0], Player.damage[1]))
            dice_roll = rnd(1, 100)
            player_aim = dice_roll + Player.aim
            if dice_roll == 1:
                print(Back.LIGHTRED_EX, Style.BRIGHT, f"Critical miss! - enemy healed {player_damage}", Style.RESET_ALL)
                enemy.cum += player_damage
            elif dice_roll == 100:
                print(Back.LIGHTGREEN_EX, Style.BRIGHT, f"Critical hit! - {player_damage*2}", Style.RESET_ALL)
                player_damage *= 2
            elif player_damage == 0 or player_aim < enemy.anus_tightness:
                print(Back.LIGHTRED_EX, "Missed!", Style.RESET_ALL)
            else:
                print(Back.LIGHTGREEN_EX, Style.BRIGHT, f"Hit - {player_damage}", Style.RESET_ALL)
            enemy.cum -= player_damage

        def enemy_attack():
            enemy_damage = (rnd(enemy.damage[0], enemy.damage[1]))
            dice_roll = rnd(1, 100)
            enemy_aim = dice_roll + enemy.aim
            if dice_roll == 1:
                print(Back.LIGHTRED_EX, Style.BRIGHT, f"Critical miss! - you healed {enemy_damage}", Style.RESET_ALL)
                Player.cum += enemy_damage
            elif dice_roll == 100:
                print(Back.LIGHTGREEN_EX, Style.BRIGHT, f"Critical hit! - {enemy_damage*2}", Style.RESET_ALL)
                enemy_damage *= 2
            elif enemy_damage == 0 or enemy_aim < Player.anus_tightness:
                print(Back.LIGHTRED_EX, "Missed!", Style.RESET_ALL)
            else:
                Player.cum -= enemy_damage
                print(Back.YELLOW, f"{enemy.name} hit you {enemy_damage}", Style.RESET_ALL)

        # fisting / battle loop
        while Player.cum > 0 and enemy.cum > 0:
            player_attack()
            sleep(0.01)
            enemy_attack()
            sleep(0.01)
            print("\nYour cum:", Player.cum)
            print(enemy.name, "cum:", enemy.cum)

        # fisting / end of battle
        if Player.cum <= 0:
            print(Style.BRIGHT, Back.RED, "\n\nU got ur ass kicked out of the fucking gym\n\n", Style.RESET_ALL)
            anus_tightness_addition = next_enemy_stats.anus_tightness / Player.anus_tightness
            limit(anus_tightness_addition, Player.anus_tightness, next_enemy_stats.anus_tightness / 10)
            Player.anus_tightness += anus_tightness_addition
            quit()
        elif enemy.cum <= 0:
            print(Fore.YELLOW, "\nYou won!", Style.RESET_ALL)
            if enemy.is_defeated == False:
                enemy.is_defeated = True
                next_enemy += 1
            Player.bucks += enemy.lvl * 100
            max_cum_addition = next_enemy_stats.max_cum / Player.max_cum
            limit(max_cum_addition, Player.max_cum, next_enemy_stats.max_cum / 10)
            Player.max_cum += max_cum_addition
            print(Fore.YELLOW, "You got ", enemy.lvl * 100, " bucks", Style.RESET_ALL)
            print(Fore.YELLOW, "Your money:", Player.bucks, Style.RESET_ALL)

    # fisting / not enough bucks
    else:
        print(Fore.RED, "\n-Fuck you", Style.RESET_ALL)
        gym_choice()

def player_stats():
    print(f'-current cum {Player.cum}\n-max cum {Player.max_cum}\n-bucks {Player.bucks}\n-Damage {Player.damage[0]}-{Player.damage[1]}\n-Aiming {Player.aim}\n-Anus tightness {Player.anus_tightness}')

# choise that you make at home

def home_choice():
    global Player
    h_choice = int(input('1:Stay at home 2:Show player stats 3:Go to gym'))
    if h_choice == 1:
        Player.days_at_home += 1
        if player_has_apartment is True:
            Player.cum += Player.max_cum/Player.days_at_home
        print('your cum ', Player.cum)
        cumming()
    elif h_choice == 2:
        player_stats()
        home_choice()
    else:
        gym_choice()

# going home

def cumming():
    global Player
    Player.day += 1
    if Player.sucked == 1:
        print('you sucked too long and got kicked out of this gym')
    print('-day ', Player.day, '\n-day_in_apartment', Player.day_in_apartment, '\n-months_in_apartment', Player.months_in_apartment)
    while Player.player_has_apartment is True:
        print('\nyou are going home')
        Player.day_in_apartment += 1
        print('your cum ', Player.cum)
        if Player.day_in_apartment == 30:
            Player.day_in_apartment = 0
            Player.months_in_apartment += 1
            Player.bucks -=2000
        if Player.day_in_apartment/30+Player.months_in_apartment == Player.months_in_apartment+1 and Player.bucks < 2000 and day > 1:
                print('you are too broke for an apartment')
                day_in_apartment = 0
                months_in_apartment = 0
                player_has_apartment = False
        home_choice()
    if Player.bucks <= 0:
        print('you are dead')
        exit()
    print('\nyou are going to your dormitory')
    Player.cum = 1
    print('your cum ', Player.cum)
    if Player.bucks > 4000:
        Player.player_has_apartment = True
        Player.bucks -= 2000
    home_choice()

# suction

def suction():
    global gym
    suck_attempt = 0
    enemy_choose = int(input("\n Choose your enemy\n1:fucking slave\n2:dungeon master\n3:Leatherman\n4:Uncle Bogdan\n5:Billy"))
    enemy = functions.aboba[enemy_choose]
    print("\n", enemy.name)
    suction_number = rnd(1, enemy.lvl*20)
    print("\n-your enemy is ", enemy.name)
    breathe = Timer(100/enemy.lvl+Player.lungs, lambda:print('you sucked too long'))
    breathe.start()
    print("\nYou have", 100/enemy.lvl+Player.lungs, "seconds to suck!")
    print('you must find tempo from ', 1, 'to', enemy.lvl*20)
    while suck_attempt != suction_number:
        suck_attempt = int(input())
        if suck_attempt < suction_number:
            print('faster\n')
        if suck_attempt > suction_number:
            print('slower\n')
    breathe.cancel()
    Player.bucks += enemy.lvl*10
    print(Fore.YELLOW, 'you got', enemy.lvl*10, 'bucks\nYour balance is', Player.bucks, Style.RESET_ALL)
    gym_choice()

# gym / stat progression / Self fisting = max gamage / Masturbating = min gamage / Banana suction = lungs / anal bot = aim
def gym():
    train_choice = int(input('\nChoose your training:\n1. Self fisting\n2. Masturbating\n3. Banana suction\n4. Anal bot'))
    if train_choice == 1:
        gym()
    elif train_choice == 2:
        gym()
    elif train_choice == 3:
        try_word()
    elif train_choice == 4:
        gym()
    else:
        gym_choice()
#gym / Banana suction
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
        print(Fore.CYAN, '\nYou must do an gachi word from these letters:', '\n', real_word, Style.RESET_ALL)
        print(choosen_word)
        trying = input()
        if trying == choosen_word:
            win = 1
        else:
            print('you must do an gachi word from  ony from these letters:', '\n', real_word)
    print(Fore.YELLOW, 'you won!', Style.RESET_ALL)
    lungs_addition = next_enemy_stats.lvl / Player.lungs
    limit(lungs_addition, Player.lungs, next_enemy_stats.lvl / 10)
    Player.max_cum += lungs_addition
    print(Fore.YELLOW, 'your lungs have increased to ', Player.lungs, Style.RESET_ALL)
    gym_choice()

# fisting = attack / cumming = go home / Suction = gather money / gym = gain strength
def gym_choice():
    while Player.cum > 0:
        a = input("\nChoose your action:\n1. Fisting\n2. Cumming\n3. Suction\n4. Gym")
        if a == "1":
            fisting()
        elif a == "2":
            cumming()
        elif a == "3":
            suction()
        elif a == "4":
            gym()
        else:
            exit()
    print(Style.BRIGHT, Back.RED, "\n\nU got ur ass kicked out of the fucking gym\n\n", Style.RESET_ALL)
    cumming()

# start of the game
print(f'{Fore.GREEN}{Style.BRIGHT}\nYou are living in apartment for with you must pay 2000 bucks per month.{Style.RESET_ALL}\nIn gym you can do: fisting = attack someone / rank = see enemy stats / cumming = go home / suction = gather money / gym = gain strength')
if __name__ == "__main__":
    cumming()
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS statistics({Player.cum} INTEGER, {Player.bucks} INTEGER, {Player.damage} INTEGER)""")
