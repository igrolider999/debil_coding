from time import sleep
from colorama import Fore, Back, Style
from random import randint as rnd
from sympy import limit
from inputimeout import inputimeout
import signal

day = 0
day_in_apartment = 0
months_in_apartment = 1
player_has_apartment = True
days_at_home = 0
home_choice = 0

class Player:
    cum = 100  # hp
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

    class dungeon_master:
        name = "Darkholme"
        cum = 500
        max_cum = 500
        damage = [1, 10]
        lvl = 15
        anus_tightness = 15
        aim = 20

    class Leatherman:
        name = "Leatherman"
        cum = 3000
        max_cum = 3000
        damage = [10, 20]
        lvl = 50
        anus_tightness = 25

    class Uncle_Bogdan:
        name = "Bogdan"
        cum = 1000
        max_cum = 1000
        damage = [40, 75]
        lvl = 100
        anus_tightness = 55

    class Billy:
        name = 'Billy'
        cum = 10000
        max_cum = 10000
        damage = [50, 100]
        lvl = 1000
        anus_tightness = 90

class functions:
    aboba = {1: Enemies.dungeon_master, 2: Enemies.fucking_slave, 3: Enemies.Billy, 4: Enemies.Leatherman,5: Enemies.Uncle_Bogdan}

# left_enemies = list(dungeon_master, fucking_slave, Billy, Van, Uncle_bogdan)

def fisting():
    if Player.bucks >= 300:
        enemy_choose = int(input("\nChoose ur enemy\n1. Dungeon Master\n2. Fucking slave\n3. Billy\n4. Leatherman\n5. Bogdan\n"))
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
            Player.bucks += enemy.lvl * 100
            print(Fore.YELLOW, "You got ", enemy.lvl * 100, " bucks", Style.RESET_ALL)
            print(Fore.YELLOW, "Your money:", Player.bucks, Style.RESET_ALL)

    # fisting / not enough bucks
    else:
        Player.cum -= 10
        print("\n-Fuck you")
        print(Fore.RED, '"You are cumming"', Style.RESET_ALL)
        print(Fore.YELLOW, 'leftover cum', Player.cum, Style.RESET_ALL)
        gym_choice()

def player_stats():
    print(f'-current cum {Player.cum}\n-max cum {Player.max_cum}\n-bucks {Player.bucks}\n-Damage {Player.damage[0]}-{Player.damage[1]}\n-Aiming {Player.aim}\n-Anus tightness {Player.anus_tightness}')


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

def cumming():
    global day, day_in_apartment, player_has_apartment, months_in_apartment
    day += 1
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
        player_has_apartment = Ture
        Player.bucks -= 2000
    home_choice()

def suction():
    global b
    enemy_choose = int(input("\nChoose ur enemy\n1. Dungeon Master\n2. Fucking slave\n3. Billy\n4. Leatherman\n5. Bogdan\n"))
    enemy = functions.aboba[enemy_choose]
    print("\n", enemy.name)
    suction_number = rnd(1, enemy.lvl*20)
    print("\n-your enemy is ", enemy.name)
    print("\nYou have", {100/enemy.lvl+Player.lungs/enemy.lvl}, "seconds to suck!")
    
# fisting = attack / cumming = go home / Suction = gather money / gym = gain strength
def gym_choice():
    while Player.cum > 0:
        a = input("\nChoose ur action:\n1. Fisting\n2. Cumming\n3. Suction\n4. Gym")
        if a == "1":
            fisting()
        elif a == "2":
            cumming()
        elif a == "3":
            suction()
        elif a == "4":
            pass
    print(Style.BRIGHT, Back.RED, "\n\nU got ur ass kicked out of the fucking gym\n\n", Style.RESET_ALL)
    cumming()

# start of the game
print('You are living in apartment for with you must pay 2000 bucks per month.\nIn gym you can do: fisting = attack someone / rank = see enemy stats / cumming = go home / suction = gather money / gym = gain strength')
if __name__ == "__main__":
    cumming()
