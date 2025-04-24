from Char_Classes import Character, Warrior, Mage, Cleric
import json
import os

def save_game(player):
    save_data = player.to_dict()
    with open("save_file.json", "w") as file:
        json.dump(save_data, file)
    print("Game Saved")

def load_game():
    if not os.path.exists("save_file.json"):
        print("No Save Game File Found")
    with open("save_file.json", "r") as file:
        save_data = json.load(file)
    
    if save_data["character_type"] == "Warrior":
        player = Warrior(save_data["name"])
    elif save_data["character_type"] == "Mage":
        player = Mage(save_data["name"])
    elif save_data["character_type"] == "Cleric":
        player = Cleric(save_data["name"])
    else:
        print("Invalid File information")
    
    player.health = save_data["health"]
    player.attack = save_data["attack"]
    player.inventory = save_data["inventory"]
    print("Game File Successfully Loaded!")
    return player
