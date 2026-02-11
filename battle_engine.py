#KAIJU CLASS DEFINITION

class Kaiju:
    def __init__(self, name, health_level, attack_power):
        self.name = name
        self.health_level = health_level
        self.attack_power = attack_power

    # 3.1 PLAYER 1 MOVES
    def attack(self, enemy):
        enemy.health_level -= self.attack_power
        return [
            f"{self.name} does {self.attack_power} damage to {enemy.name}!",
            f"{enemy.name} has {enemy.health_level} health left."
        ]

    def defend(self):
        self.health_level += 20
        return [
            f"{self.name} boosts health by 20.",
            f"{self.name} now has {self.health_level} health."
        ]

    # 3.2 PLAYER 2 MOVES
    def attack_2(self, player):
        player.health_level -= self.attack_power
        return [
            f"{self.name} does {self.attack_power} damage to {player.name}!",
            f"{player.name} has {player.health_level} health left."
        ]

    def defend_2(self):
        self.health_level += 20
        return [
            f"{self.name} boosts health by 20.",
            f"{self.name} now has {self.health_level} health."
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


# 2. ONCE THE PAGE LOADS THIS BECOMES THE FIRST SESSION AND THE GAME IS READY TO START
# The bottom of the init_session has the WIN CONDITION logic.

from io import StringIO
from contextlib import redirect_stdout

def init_session(session):
    if "player_health" not in session:
        # player_name and enemy_name must already be set by the route
        player = kaiju_list[session["player_name"]]
        enemy = kaiju_list[session["enemy_name"]]

        session["player_health"] = player.health_level
        session["enemy_health"] = enemy.health_level
        session["player_attack"] = player.attack_power
        session["enemy_attack"] = enemy.attack_power

        session["turn"] = "player"
        session["log"] = ["BATTLE BEGINS"]
        #Game start log lines
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
        session["log"].append(f"\n{session["player_name"]} wins against {session["enemy_name"]},\nPLAYER 1 WINS \n BATTLE CONCLUDES ")
    if session["enemy_health"] >= 0 and session["player_health"] <=0:
        session["log"].append(f"\n{session["enemy_name"]} wins against {session["player_name"]},\nPLAYER 2 WINS \n BATTLE CONCLUDES ")

# Every time state changes this updates it:
# REBUILD OBJECTS FROM SESSION SNAPSHOT

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


# 3. SINGLE TURN EXECUTION

def run_turn(player, enemy, move, turn):
    if move == "attack":
        return player.attack(enemy)
    elif move == "defend":
        return player.defend()
    if move == "attack_2":
        return enemy.attack(player)
    elif move == "defend_2":
        return enemy.defend()
    return []


# SAVE MUTATED STATE BACK TO SESSION

def persist(session, player, enemy):
    session["player_health"] = player.health_level
    session["enemy_health"] = enemy.health_level



init_game_state = init_session
rebuild_kaiju = rebuild
persist_state = persist
