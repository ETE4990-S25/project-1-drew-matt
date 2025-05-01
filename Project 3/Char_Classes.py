import random

# Player Class
class Player:
    def __init__(self, name, health, attack, character_type, max_health):
        self.name = name
        self.health = health
        self.attack = attack
        self.character_type = character_type
        self.inventory = []
        self.max_health = max_health

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
    
    def is_alive(self):
        return self.health > 0
    
    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} has been added to your inventory")

    def use_potion(self):
        for item in self.inventory:
            if item == "Health Potion":
                self.health = min(self.health + 30, self.max_health)
                self.inventory.remove(item)
                print("Your Health Has Been Restored By 30")
                print("-"*100)
                return
        print("You Have No More Health Potions :((")
        print("-"*100)

    def to_dict(self):
        return {"name": self.name, "health": self.health, "attack": self.attack,
                "character_type": self.character_type, "inventory": self.inventory}
    
    @classmethod
    def from_dict(cls, data):
        character = cls(data["name"], data["health"], data["attack"], data["character_type"])
        character.inventory = data["inventory"]
        return character

    def __str__(self):
        if self.character_type in ["Warrior", "Mage", "Cleric"]:
            return f"{self.name}: {self.character_type}, {self.health} HP, {self.attack} Damage, Inventory: {self.inventory}"
        else:
            return f"{self.name}: {self.character_type}, {self.health} HP, {self.attack} Damage"

# Enemy Class
class Enemy:
    def __init__(self, name, health, attack, character_type):
        self.name = name
        self.health = health
        self.attack = attack
        self.character_type = character_type

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
    
    def is_alive(self):
        return self.health > 0
    
    def __str__(self):
        return f"{self.name}: {self.character_type}, {self.health} HP, {self.attack} Damage"
             
    def drop_loot(self, player):
        loot = random.choice(self.loot)
        player.add_to_inventory(loot)
        
# Playable Subclasses
class Warrior(Player):
    def __init__(self, name):
        super().__init__(name, health = 120, attack = 15, character_type = "Warrior", max_health = 120)
        self.ability = "Enraged Attack"
        self.add_to_inventory("Rusted Sword")
        self.add_to_inventory("Health Potion")

    def use_ability(self):
        return self.attack + 10

class Mage(Player):
    def __init__(self, name):
        super().__init__(name, health = 100, attack = 20, character_type = "Mage", max_health = 100)
        self.ability = "Fireball"
        self.add_to_inventory("Iron Staff")
        self.add_to_inventory("Health Potion")

    def use_ability(self):
        return self.attack +15

class Cleric(Player):
    def __init__(self, name):
        super().__init__(name, health = 100, attack = 10, character_type = "Cleric", max_health = 100)
        self.ability = "Heal"
        self.add_to_inventory("Staff of Moderate Healing")
        self.add_to_inventory("Health Potion")

    def use_ability(self):
        self.health = min(self.health + 20, self.max_health())

# Enemy Subclasses
class Skeleton(Enemy):
    def __init__(self):
        super().__init__("Skeleton", health = 30, attack = 15, character_type = "Mob")
        self.loot = ["Gold", "Health Potion", "Wooden Bow"]

class Orc(Enemy):
    def __init__(self):
        super().__init__("Orc", health = 50, attack = 10, character_type = "Mob")
        self.loot = ["Gold", "Health Potion", "Iron Sword"]

class Dragon(Enemy):
    def __init__(self):
        super().__init__("Dragon", health = 150, attack = 25, character_type = "Boss")
        self.loot = ["Gold", "Dragon's Blood Potion", "Dragon's Scale Armor"]