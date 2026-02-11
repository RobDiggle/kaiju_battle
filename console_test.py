#ITERATION 4: 
# New Kaiju characters were added, the next iteration will focus
# on making them playable

class Kaiju:
    def __init__(self, name, health_level, attack_power):
        self.name = name
        self.health_level = health_level
        self.attack_power = attack_power

# 3.1: THE LOOP WILL KEEP COMING BACK TO HERE AGAIN AND AGAIN UNTIL A VICTORY IS ACHIEVED
# These are the moves for PLAYER 1
    def attack(self, enemy):
        enemy.health_level -= self.attack_power
        print(f'{self.name} does {self.attack_power} of damage to {enemy.name}!\n {enemy.name} has {enemy.health_level} health left.\n')

    def defend(self, enemy):
        self.health_level += 20
        enemy.name
        print(f"{self.name} has boosted his health by 20 to now have {self.health_level}!\n")

# 3.2: These are the moves for PLAYER 2
    def attack_2(self, player):
        player.health_level -= self.attack_power
        print(f'{self.name} does {self.attack_power} of damage to {player.name}!\n {player.name} has {player.health_level} health left.\n')

    def defend_2(self, player):
        self.health_level += 20
        player.name
        print(f"{self.name} has boosted his health by 20 to now have {self.health_level}!\n")

# 1. THE START OF THE GAME - THE START. 
def game_start():
    print("Character options: \n Godzilla \n Gigan \n King Kong \n King Ghidorah")
    p1_choose = input("You are playing Kaiju battle!\n What character does Player 1 choose?").lower()

    for kaiju in kaiju_list:
        if kaiju.name.lower() in p1_choose:
            player = kaiju

    p2_choose = input("What character does Player 2 choose?").lower()   

    for kaiju in kaiju_list:
        if kaiju.name.lower() in p2_choose:
            enemy = kaiju

    print(f"Player 1 has chosen {player.name}.\n")
    print(f"Player 2 will play as {enemy.name}.\n")
    print("BATTLE BEGINS\n")

    if "godzilla" == player.name.lower():
        print(f"Godzilla lumbers forward, he sees {enemy.name}, the battle starts!\n \n Player 1 attacks first!\n")
    elif "gigan" == player.name.lower():
        print(f"From space Gigan floats down, he sees {enemy.name}, the battle starts!\n \n Player 1 attacks first!\n")
    elif "king kong" == player.name.lower():
        print(f"Kong emerges from trees of Skull Island, he sees {enemy.name}, the battle starts!\n \n Player 1 attacks first!\n")
    elif "king ghidorah" == player.name.lower():
        print(f"Sent to destroy earth, {player.name} sees {enemy.name}, the battle starts!\n \n Player 1 attacks first!\n")

    
    game_middle(player, enemy) 


#2 : THE SECOND STAGE OF THE GAME - THE CONTROL FLOW.
def game_middle(player, enemy):


    while enemy.health_level > 0 and player.health_level > 0:
        move = input("PLAYER 1 MOVE: attack or defend!").lower()

        if move == "attack":
            player.attack(enemy)
            alternate_turns(player, enemy)
                        
        if move == "defend":
            player.defend(enemy)
            alternate_turns(player, enemy)

        if move == "break":
            break

        if enemy.health_level <= 0 and player.health_level >= 0:
            print(f"\n{player.name} wins against {enemy.name}! \nPLAYER 1 WINS \n BATTLE CONCLUDES")
            return

# 4: THE SECOND PART OF THE SECOND STAGE OF THE GAME - THE CONTROL FLOW
# This gives Player 2 the abiity to interact with the game state.
def alternate_turns(player, enemy):

    while player.health_level > 0 and enemy.health_level > 0:
     enemy_move = input("PLAYER 2 MOVE: attack or defend!").lower()
    
     if enemy_move == "attack":
          enemy.attack_2(player)
          game_middle(player, enemy)

     elif enemy_move == "defend":
          enemy.defend_2(player)
          game_middle(player, enemy)


     if player.health_level <= 0 and enemy.health_level >= 0:
        print(f"\n{enemy.name} wins against {player.name}! \n PLAYER 2 WINS \n BATTLE CONCLUDES")
        return
    
     

# Playable Kaiju characters     
Godzilla = Kaiju("Godzilla" , 70, 15)
Gigan = Kaiju("Gigan", 335, 55)
King_Kong = Kaiju("King Kong", 50, 35)
King_Ghidorah = Kaiju("King Ghidorah", 80, 20)

kaiju_list = [Godzilla, Gigan, King_Kong, King_Ghidorah]

game_start()