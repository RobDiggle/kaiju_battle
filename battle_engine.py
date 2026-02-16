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

kaiju_list = {
    "Godzilla": Kaiju("Godzilla", 70, 25),
    "Gigan": Kaiju("Gigan", 70, 25),
    "King Kong": Kaiju("King Kong", 60, 35),
    "King Ghidorah": Kaiju("King Ghidorah", 80, 20),
    "Anguirus": Kaiju("Anguirus", 40, 10),
    "Megalon" : Kaiju("Megalon", 60, 30),
    "Rodan" : Kaiju("Rodan", 40, 15),
    "Mechagodzilla" : Kaiju("Mechagodzilla", 80, 20),
    "Mothra" : Kaiju("Mothra", 40, 40),
    "Gamera" : Kaiju("Gamera", 80, 20)
}

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

    if session["enemy_health"] >= 0 and session["player_health"] <=0:
        session["log"].append(f"\n{session["enemy_name"]} wins against {session["player_name"]},\nPLAYER 2 WINS. ")
        session["log"].append("\nBATTLE CONCLUDES")

# Puts the init session function into a variable
init_game_state = init_session

# ============================================================================
# 3. The following 3 variables allow the alteration of state in the game which 
# makes turn based combat possible.
# ============================================================================

# This function rebuilds the Kaiju objects in a new snapshot
# with changes based on the altered game state.

def rebuild(session):
    player = Kaiju(
        session["player_name"],
        session["player_health"],
        session["player_attack"]
    )
    enemy = Kaiju(
        session["enemy_name"],
        session["enemy_health"],
        session["enemy_attack"]
    )
    return player, enemy

rebuild_kaiju = rebuild

# After the state is mutated by the execution of a turn (done below in run_turn),
# this function saves the mutated state.

def persist(session, player, enemy):
    session["player_health"] = player.health_level
    session["enemy_health"] = enemy.health_level


# Each turn operates through the use of this function

def run_turn(player, enemy, move):
    if move == "attack":
        return player.attack(enemy)
    elif move == "defend":
        return player.defend()
    if move == "attack_2":
        return enemy.attack(player)
    elif move == "defend_2":
        return enemy.defend()
    return []

persist_state = persist
