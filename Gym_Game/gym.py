from time import sleep
from colorama import Fore, Back, Style
from random import randint as rnd
from sympy import limit
from threading import Timer
import sqlite3
# da
day = 0
day_in_apartment = 0
months_in_apartment = 1
player_has_apartment = True
days_at_home = 0
home_choice = 0
sucked = 0
next_enemy = 1

class Player:
    cum = int(100)  # hp
    max_cum = 100  # max hp
    bucks = 1000  # money
    damage = [0, 1]  # strength
    aim = 1
    anus_tightness = 1
    lungs = 1

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

# left_enemies = list(dungeon_master, fucking_slave, Billy, Van, Uncle_bogdan)

def fisting():
    global next_enemy
    if Player.bucks >= 300:
        enemy_choose = int(input("\n Choose your enemy\n1:fucking slave\n2:dungeon master\n3:Leatherman\n4:Uncle Bogdan\n5:Billy"))
        if enemy_choose > next_enemy:
            print('\nYou are too weak for him. Try someone else')
            fisting()
        enemy = functions.aboba[enemy_choose]
        print("\n", enemy.name)

        # fisting / attack functions
        def player_attack():
            player_damage = (rnd(Player.damage[0], Player.damage[1]))
            dice_roll = rnd(1, 100)
            player_aim = dice_roll + Player.aim
            if dice_roll == 1:
                print(Back.LIGHTRED_EX, Style.BRIGHT, "Critical miss! - enemy healed {player_damage}", Style.RESET_ALL)
                enemy.cum += player_damage
            elif dice_roll == 100:
                print(Back.LIGHTGREEN_EX, Style.BRIGHT, "Critical hit! - {player_damage*2}", Style.RESET_ALL)
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
                print(Back.LIGHTRED_EX, Style.BRIGHT, "Critical miss! - you healed {enemy_damage}", Style.RESET_ALL)
                Player.cum += enemy_damage
            elif dice_roll == 100:
                print(Back.LIGHTGREEN_EX, Style.BRIGHT, "Critical hit! - {enemy_damage*2}", Style.RESET_ALL)
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
            anus_tightness_addition = Player.anus_tightness / enemy.anus_tightness
            limit(anus_tightness_addition, Player.anus_tightness, enemy.anus_tightness / 10)
            Player.anus_tightness += anus_tightness_addition
            quit()
        elif enemy.cum <= 0:
            print("\nYou won!")
            if enemy.is_defeated == False:
                enemy.is_defeated = True
                next_enemy += 1
            Player.bucks += enemy.lvl * 100
            max_cum_addition = Player.max_cum / enemy.cum
            limit(anus_tightness_addition, Player.anus_tightness, enemy.anus_tightness / 10)
            Player.anus_tightness += anus_tightness_addition
            print(Fore.YELLOW, "You got ", enemy.lvl * 100, " bucks", Style.RESET_ALL)
            print(Fore.YELLOW, "Your money:", Player.bucks, Style.RESET_ALL)

    # fisting / not enough bucks
    else:
        print("\n-Fuck you")
        gym_choice()

def player_stats():
    print(f'-current cum {Player.cum}\n-max cum {Player.max_cum}\n-bucks {Player.bucks}\n-Damage {Player.damage[0]}-{Player.damage[1]}\n-Aiming {Player.aim}\n-Anus tightness {Player.anus_tightness}')



# choise that you make at home

def home_choice():
    global days_at_home
    h_choice = int(input('1:Stay at home 2:Show player stats 3:Go to gym'))
    if h_choice == 1:
        days_at_home+=1
        if player_has_apartment is True:
            Player.cum += Player.max_cum/days_at_home
        print('your cum ', Player.cum)
        cumming()
    elif h_choice == 2:
        player_stats()
        home_choice()
    else:
        gym_choice()

# going home

def cumming():
    global day, day_in_apartment, player_has_apartment, months_in_apartment
    day += 1
    if sucked == 1:
        print('you sucked too long and got kicked out of this gym')
        sucked = 0
    print('-day ', day, '\n-day_in_apartment', day_in_apartment, '\n-months_in_apartment', months_in_apartment)
    while player_has_apartment is True:
        print('\nyou are going home')
        day_in_apartment += 1
        print('your cum ', Player.cum)
        if day_in_apartment == 30:
            day_in_apartment = 0
            months_in_apartment += 1
            Player.bucks -=2000
        if day_in_apartment/30+months_in_apartment == months_in_apartment+1 and Player.bucks < 2000 and day > 1:
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
        player_has_apartment = True
        Player.bucks -= 2000
    home_choice()

# suction

def breathe_end():
    global sucked
    print("You can't breathe\n-Get out")
    sucked = 1

def suction():
    global gym
    suck_attempt = 0
    enemy_choose = int(input("\n Choose your enemy\n1:fucking slave\n2:dungeon master\n3:Leatherman\n4:Uncle Bogdan\n5:Billy"))
    enemy = functions.aboba[enemy_choose]
    print("\n", enemy.name)
    suction_number = rnd(1, enemy.lvl*20)
    print("\n-your enemy is ", enemy.name)
    breathe = Timer(100/enemy.lvl+Player.lungs/enemy.lvl, lambda:breathe_end())
    breathe.start()
    print("\nYou have", 100/enemy.lvl+Player.lungs/enemy.lvl, "seconds to suck!")
    print('you must find tempo from ', 1, 'to', enemy.lvl*20)
    while suck_attempt != suction_number:
        suck_attempt = int(input())
        if suck_attempt < suction_number:
            print('faster\n')
        if suck_attempt > suction_number:
            print('slower\n')
    breathe.cancel()
    Player.bucks += enemy.lvl*10
    print('you got', enemy.lvl*10, 'bucks\nYour balance is', Player.bucks)
    gym_choice()

# gym / stat progression
def gym():
    train_shoice = int(input('\nChoose your action:\n1. Fisting\n2. Cumming\n3. Suction\n4. Gym'))
    

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
            pass
        else:
            exit()
    print(Style.BRIGHT, Back.RED, "\n\nU got ur ass kicked out of the fucking gym\n\n", Style.RESET_ALL)
    cumming()

# start of the game
print('You are living in apartment for with you must pay 2000 bucks per month.\nIn gym you can do: fisting = attack someone / rank = see enemy stats / cumming = go home / suction = gather money / gym = gain strength')
if __name__ == "__main__":
    cumming() 
