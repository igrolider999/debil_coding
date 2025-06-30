from time import sleep
from colorama import Fore, Back, Style
from random import randint as rnd

class Player:
    cum = 100 #hp
    bucks = 300 #money
    damage = [0, 1] #strenght
    aim = 1
    anus_tightness = 1
class Enemies:
    class dungeon_master:
        name = "Darkholme"
        cum = 500
        damage = [1, 10]
        lvl = 15
        anus_tightness = 15
    class fucking_slave:
        name = "Fucking Slave"
        cum = 100
        damage = [1, 2]
        lvl = 1
        anus_tightness = 5
        aim = 2
    class Billy:
        name = 'Billy'
        cum = 10000
        damage = [50, 100]
        lvl = 1000
        anus_tightness = 90
    class Leatherman:
        name = "Leatherman"
        cum = 3000
        damage = [10, 20]
        lvl = 50
        anus_tightness = 25
    class Uncle_Bogdan:
        name = "Bogdan"
        cum = 1000
        damage = [40, 75]
        lvl = 100
        anus_tightness = 55

class functions:
    aboba = {1:Enemies.dungeon_master, 2:Enemies.fucking_slave, 3:Enemies.Billy, 4:Enemies.Leatherman, 5:Enemies.Uncle_Bogdan}
    
# left_enemies = list(dungeon_master, fucking_slave, Billy, Van, Uncle_bogdan)

def fisting():
    if Player.bucks >= 300:
        enemy_choose = int(input("\nChoose ur enemy\n1. Dungeon Master\n2. Fucking slave\n3. Billy\n4. Leatherman\n5. Bogdan\n"))
        enemy = functions.aboba[enemy_choose]
        print("\n", enemy.name)

        # attack functions

        def player_attack():
            player_damage = (rnd(Player.damage[0], Player.damage[1]))
            dice_roll = rnd(1, 100)
            player_aim = dice_roll + Player.aim
            if dice_roll == 1:
                print(Back.LIGHTRED_EX, Style.BRIGHT, "Critical miss!", Style.RESET_ALL)
                player_damage = 0
            elif dice_roll == 100:
                print(Back.LIGHTGREEN_EX, Style.BRIGHT, "Critical hit!", Style.RESET_ALL)
                player_damage *= 2
            elif player_damage == 0 or player_aim < enemy.anus_tightness:
                print(Back.LIGHTRED_EX,"Missed!",Style.RESET_ALL)
            else:
                print(Back.LIGHTGREEN_EX,Style.BRIGHT,f"Hit - {player_damage}",Style.RESET_ALL)
            enemy.cum -= player_damage
        def enemy_attack():
            enemy_damage = (rnd(enemy.damage[0], enemy.damage[1]))
            enemy_aim = rnd(1, 100)+ enemy.aim
            if enemy_damage == 0 or enemy_aim < Player.anus_tightness:
                print(Back.LIGHTRED_EX,"Missed!",Style.RESET_ALL)
            else:
                Player.cum -= enemy_damage
                print(Back.YELLOW,f"{enemy.name} hit you {enemy_damage}",Style.RESET_ALL)

        # battle loop

        while Player.cum > 0 and enemy.cum > 0:
            player_attack()
            sleep(0.01)
            enemy_attack()
            sleep(0.01)
            print("\nYour cum:", Player.cum)
            print(enemy.name, "cum:", enemy.cum)

        # end of battle

        if Player.cum <= 0:
            print(Style.BRIGHT,Back.RED, "\n\nU got ur ass kicked out of the fucking gym\n\n", Style.RESET_ALL)
            Player.anus_tightness =+ enemy.lvl
            quit()
        elif enemy.cum <= 0:
            print("\nYou won!")
            Player.bucks += enemy.lvl * 100
            print(Fore.YELLOW, "You got ", enemy.lvl*100, " bucks", Style.RESET_ALL)
            print(Fore.YELLOW, "Your money:", Player.bucks, Style.RESET_ALL)

    else:
        Player.cum -= 10
        print("\n-Fuck you")
        print(Fore.RED, '"You are cummng"', Style.RESET_ALL)
        print(Fore.YELLOW, 'leftover cum', Player.cum, Style.RESET_ALL)
        choice()

#fisting = atack / cumming = go home / Suction = gather money / gym = lvl gain

def choice():
    while Player.cum > 0:
        a = input("\nChoose ur action:\n1. Fisiting\n2. Cumming\n3. Suction\n4. Gym")
        if a == "1":
            fisting()
        elif a == "2":
            quit()
        elif a == "3":
            pass
        elif a == "4":
            pass
    print(Style.BRIGHT,Back.RED, "\n\nU got ur ass kicked out of the fucking gym\n\n", Style.RESET_ALL)
    quit()
    

if __name__ == "__main__":
    choice()