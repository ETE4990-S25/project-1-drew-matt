import random

# Base Character Class
class Character:
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
                self.health = min(self.health + 30, self.max_health())
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

# Playable Subclasses
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health = 120, attack = 15, character_type = "Warrior", max_health = 120)
        self.ability = "Enraged Attack"
        self.add_to_inventory("Rusted Sword")
        self.add_to_inventory("Health Potion")

    def use_ability(self):
        return self.attack + 10

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health = 100, attack = 20, character_type = "Mage", max_health = 100)
        self.ability = "Fireball"
        self.add_to_inventory("Iron Staff")
        self.add_to_inventory("Health Potion")

    def use_ability(self):
        return self.attack +15

class Cleric(Character):
    def __init__(self, name):
        super().__init__(name, health = 100, attack = 10, character_type = "Cleric", max_health = 100)
        self.ability = "Heal"
        self.add_to_inventory("Staff of Moderate Healing")
        self.add_to_inventory("Health Potion")

    def use_ability(self):
        self.health = min(self.health + 20, self.max_health())

# Mob Subclasses
class Skeleton(Character):
    def __init__(self):
        super().__init__("Skeleton", health = 30, attack = 15, character_type = "Mob")

    def drop_loot(self, player):
        loot = random.choice(["Gold", "Health Potion", "Wooden Bow"]) 
        player.add_to_inventory(loot)

class Orc(Character):
    def __init__(self):
        super().__init__("Orc", health = 50, attack = 10, character_type = "Mob")

    def drop_loot(self, player):
        loot = random.choice(["Gold", "Health Potion", "Iron Sword"])
        player.add_to_inventory(loot)

class Dragon(Character):
    def __init__(self):
        super().__init__("Dragon", health = 150, attack = 25, character_type = "Boss")

    def drop_loot(self, player):
        loot = random.choice(["Gold", "Dragon's Blood Potion", "Dragon's Scale Armor"])
        player.add_to_inventory(loot)    
