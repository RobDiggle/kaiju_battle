# ============================================================================
#KAIJU CLASS - Defining Kaiju / Listing Kaiju as playable characters
# ============================================================================

class Kaiju:
    def __init__(self, name, health_level, attack_power):
        self.name = name
        self.health_level = health_level
        self.attack_power = attack_power

# 3.1 PLAYER 1 MOVES
    def attack(self, enemy):
        enemy.health_level -= self.attack_power
        return [
            f"{self.name} does {self.attack_power} damage to {enemy.name}!\n",
        ]

    def defend(self):
        self.health_level += 20
        return [
            f"{self.name} boosts health by 20.",
        ]

# 3.2 PLAYER 2 MOVES
    def attack_2(self, player):
        player.health_level -= self.attack_power
        return [
            f"{self.name} does {self.attack_power} damage to {player.name}!\n",
        ]

    def defend_2(self):
        self.health_level += 20
        return [
            f"{self.name} boosts health by 20."
                            ]



# Sub Class creation so the Kaiju can have special moves and different rates of defend
class slasher(Kaiju):
    def __init__(self, name, special_name, health_level, attack_power, slash_power, slash_quantity,defend_level):
        super().__init__(name, health_level, attack_power)
        self.special_name = special_name
        self.slash_power = slash_power
        self.slash_quantity = slash_quantity
        self.defend_level = defend_level

# Player 1 moves
    def attack(self, enemy):
            enemy.health_level -= self.attack_power
            return [
                f"{self.name} does {self.attack_power} damage to {enemy.name}!\n",
                    ]

    def defend(self):
            self.health_level += self.defend_level
            return [
            f"{self.name} boosts health by {self.defend_level}.",
                    ]

    def special(self, enemy):
        if self.slash_quantity <= 0:
            return [f"{self.name} has no {self.special_name}'s left!"]

        self.slash_quantity -= 1
        enemy.health_level -= self.slash_power
        return [
            f"{self.name} uses {self.special_name} attack and does {self.slash_power} damage to {enemy.name}!\n"
            f"{self.name} has {self.slash_quantity} {self.special_name}'s left!\n"
        ]

    # Player 2 moves

    def attack_2(self, player):
        player.health_level -= self.attack_power
        return [
            f"{self.name} does {self.attack_power} damage to {player.name}!\n",
        ]

    def defend_2(self):
        self.health_level += self.defend_level
        return [
            f"{self.name} boosts health by {self.defend_level}.",
                            ]
    def special_2(self, player):
            if self.slash_quantity <= 0:
                return [f"{self.name} has no {self.special_name}'s left!"]

            self.slash_quantity -= 1
            player.health_level -= self.slash_power
            return [
            f"{self.name} uses a {self.special_name} attack and does {self.slash_power} damage to {player.name}!\n"
            f"{self.name} has {self.slash_quantity} {self.special_name}'s left!\n"                     
              ]

class smasher(Kaiju):
        def __init__(self, name, special_name, health_level, attack_power, smash_power, smash_quantity,defend_level):
            super().__init__(name, health_level, attack_power)
            self.special_name = special_name
            self.smash_power = smash_power
            self.smash_quantity = smash_quantity
            self.defend_level = defend_level

    # Player 1 moves
        def attack(self, enemy):
                enemy.health_level -= self.attack_power
                return [
                    f"{self.name} does {self.attack_power} damage to {enemy.name}!\n",
                        ]

        def defend(self):
                self.health_level += self.defend_level
                return [
                f"{self.name} boosts health by {self.defend_level}.",
                        ]

        def special(self, enemy):
                    if self.smash_quantity <= 0:
                        return  [f"{self.name} has no {self.special_name} attacks left!"]
                    
                    self.smash_quantity -= 1
                    enemy.health_level -= self.smash_power
                    return [
                        f"{self.name} uses a {self.special_name} and does {self.smash_power} damage to {enemy.name}!",
                        f"{self.name} has {self.smash_quantity} {self.special_name} attacks left!\n"                     

                        ]
        # Player 2 moves

        def attack_2(self, player):
            player.health_level -= self.attack_power
            return [
                f"{self.name} does {self.attack_power} damage to {player.name}!\n",
            ]

        def defend_2(self):
            self.health_level += self.defend_level
            return [
                f"{self.name} boosts health by {self.defend_level}.",
                                ]
        def special_2(self, player):
                    self.smash_quantity -= 1
                    player.health_level -= self.slash_power
                    return [
                        f"{self.name} uses a {self.special_name} and does {self.smash_power} damage to {player.name}!\n",
                        f"{self.name} has {self.smash_quantity} {self.special_name}'s left!"
                        ]
        
class blaster(Kaiju):
        def __init__(self, name, special_name,health_level, attack_power, blast_power, blast_quantity,defend_level):
            super().__init__(name, health_level, attack_power)
            self.special_name = special_name
            self.blast_power = blast_power
            self.blast_quantity = blast_quantity
            self.defend_level = defend_level

    # Player 1 moves
        def attack(self, enemy):
                enemy.health_level -= self.attack_power
                return [
                    f"{self.name} does {self.attack_power} damage to {enemy.name}!\n",
                        ]

        def defend(self):
                self.health_level += self.defend_level
                return [
                f"{self.name} boosts health by {self.defend_level}.",
                        ]

        def special(self, enemy):
                    if self.blast_quantity <= 0:
                        return  [f"{self.name} has no {self.special_name}'s left!"]
                    
                    self.blast_quantity -= 1
                    enemy.health_level -= self.blast_power
                    return [
                        f"{self.name} uses {self.special_name} and does {self.blast_power} damage to {enemy.name}!",
                        f"{self.name} has {self.blast_quantity} {self.special_name}'s left!\n"                     

                        ]
        # Player 2 moves

        def attack_2(self, player):
            player.health_level -= self.attack_power
            return [
                f"{self.name} does {self.attack_power} damage to {player.name}!\n",
            ]

        def defend_2(self):
            self.health_level += self.defend_level
            return [
                f"{self.name} boosts health by {self.defend_level}.",
                                ]
        def special_2(self, player):
                    if self.blast_quantity <= 0:
                        return  [f"{self.name} has no {self.special_nam}'s left!"]
                    
                    self.blast_quantity -= 1
                    player.health_level -= self.blast_power
                    return [
                        f"{self.name} uses {self.special_name} and does {self.blast_power} damage to {player.name}!\n"
                        f"{self.name} has {self.blast_quantity} {self.special_name}'s left!",
                        ]
kaiju_list = {
        "Godzilla": blaster("Godzilla", "ATOMIC BLAST", 100, 25, 65, 1, 20),
        "Gigan": slasher("Gigan", "BUZZSAW SLASH", 100, 20, 35, 3, 15),
        "King Kong": smasher("King Kong", "LIGHTNING PUNCH", 80, 35, 50, 1, 10),
        "King Ghidorah": blaster("King Ghidorah", "GRAVITY BEAM BLAST", 120, 20, 30, 3, 15),
        "Anguirus": smasher("Anguirus","SOUND WAVE",  70, 20, 25, 5, 10),
        "Megalon" : slasher("Megalon","DRILL SLASH", 70, 15, 35, 2, 10),
        "Rodan" : smasher("Rodan","GIANT CLAW", 70, 15, 30, 4, 25),
        "Mechagodzilla" : blaster("Mechagodzilla","LASER BLAST", 120, 20, 55, 1, 25),
        "Mothra" : Kaiju("Mothra", 40, 40),
        "Gamera" : slasher("Gamera","SHELL SPIN", 80, 10, 25, 3, 25)
    }

class creator(Kaiju):
     pass

# Sub classes:
# Slashers: Gigan, Gamera, Megalon
# Smashers: King Kong, Anguirus, Rodan
# Blasters: Godzilla, King Ghidorah, MechaGodzilla
# Creator: Mothra

# ============================================================================
# 2. Function initializing the session. 
# The bottom of the init_session has the WIN CONDITION logic.
# ============================================================================


from io import StringIO
from contextlib import redirect_stdout

def init_session(session):
    if "player_health" not in session:
# player_name and enemy_name must already be set by the route. 
# This 'redefining' of names is only really relevant in the rebuild_kaiju function down below
        player = kaiju_list[session["player_name"]]
        enemy = kaiju_list[session["enemy_name"]]

        session["player_health"] = player.health_level
        session["enemy_health"] = enemy.health_level
        session["player_attack"] = player.attack_power
        session["enemy_attack"] = enemy.attack_power


#Game start log lines - standard BATTLE BEGINS and dynamic opening lines based on player character.
        session["log"] = ["BATTLE BEGINS"]

        if session["player_name"].lower() == "godzilla" and session["enemy_name"].lower()!= "godzilla":
            session["log"].append(f"{session["player_name"]} lumbers forward, he sees {session["enemy_name"]}, the battle starts!\n")
        if session["player_name"].lower() == "gigan" and session["enemy_name"].lower() != "gigan":
            session["log"].append(f"From space Gigan floats down, he sees {session["player_name"]}, the battle starts!\n")
        if session["player_name"].lower() == "king kong" and session["enemy_name"].lower()!= "king kong":
            session["log"].append(f"Kong emerges from trees of Skull Island, he sees {session["enemy_name"]}, the battle starts!\n")
        if session["player_name"].lower() == "king ghidorah" and session["enemy_name"].lower()!= "king ghidorah":
            session["log"].append(f"Sent to destroy earth, {player.name} sees {session["enemy_name"]}, the battle starts!\n")
        if session["player_name"].lower() == "anguirus" and session["enemy_name"].lower()!= "anguirus":
            session["log"].append(f"{session["player_name"]} emerges from the valleys of Monster Island, he sees {session["enemy_name"]}, the battle starts!\n")
        if session["player_name"].lower() == "megalon" and session["enemy_name"].lower()!= "megalon":
            session["log"].append(f"{session["player_name"]} swims up from the bottom of the ocean to destroy the land dwellers, {session["enemy_name"]} is in his way, the battle starts!\n")
        if session["player_name"].lower() == "rodan" and session["enemy_name"].lower()!= "rodan":
            session["log"].append(f"{session["player_name"]} swoops down from the sky in a violent rush at {session["enemy_name"]}, the battle starts!\n")
        if session["player_name"].lower() == "mechagodzilla" and session["enemy_name"].lower()!= "mechagodzilla":
            session["log"].append(f"{session["player_name"]} has been built by aliens to conquer Earth. \n He lands ready to begin his invasion and sees {session["enemy_name"]}, the battle starts!\n")
        if session["player_name"].lower() == "mothra" and session["enemy_name"].lower()!= "mothra":
            session["log"].append(f"{session["player_name"]} senses a threat to the Earths security. She sees {session["enemy_name"]}, the battle starts!\n")
        if session["player_name"].lower() == "gamera" and session["enemy_name"].lower()!= "gamera":
            session["log"].append(f"{session["player_name"]} lumbers forward, he sees {session["enemy_name"]}, the battle starts!\n")

# Game conclusion log lines

    if session["player_health"] >= 0 and session["enemy_health"] <=0:
        session["log"].append(f"\n{session["player_name"]} wins against {session["enemy_name"]},\nPLAYER 1 WINS. ")
        session["log"].append("\nBATTLE CONCLUDES")
        session["enemy_health"] = 0


    if session["enemy_health"] >= 0 and session["player_health"] <=0:
        session["log"].append(f"\n{session["enemy_name"]} wins against {session["player_name"]},\nPLAYER 2 WINS. ")
        session["log"].append("\nBATTLE CONCLUDES")
        session["player_health"] = 0

# Puts the init session function into a variable
init_game_state = init_session

# ============================================================================
# 3. The following 3 variables allow the alteration of state in the game which 
# makes turn based combat possible.
# ============================================================================

# This function rebuilds the Kaiju objects in a new snapshot
# with changes based on the altered game state.

def rebuild_kaiju(session):
    base_player = kaiju_list[session["player_name"]]
    base_enemy = kaiju_list[session["enemy_name"]]

    player = base_player.__class__(**base_player.__dict__)
    enemy = base_enemy.__class__(**base_enemy.__dict__)

    player.__dict__.update(session.get("player_extras", {}))
    enemy.__dict__.update(session.get("enemy_extras", {}))
    
    return player, enemy

# After the state is mutated by the execution of a turn (done below in run_turn),
# this function saves the mutated state.

def persist(session, player, enemy):
    session["player_health"] = player.health_level
    session["enemy_health"] = enemy.health_level

    # store any subclass-only attrs automatically
    session["player_extras"] = player.__dict__.copy()
    session["enemy_extras"] = enemy.__dict__.copy()


# Each turn operates through the use of this function

def run_turn(player, enemy, move):
# Player 1 moves
    if move == "attack":
        return player.attack(enemy)
    elif move == "defend":
        return player.defend()
    elif move == "special":
         return player.special(enemy)
# Player 2 moves
    if move == "attack_2":
        return enemy.attack(player)
    elif move == "defend_2":
        return enemy.defend()
    elif move == "special_2":
         return enemy.special(player)
    return []

persist_state = persist
