import random

# Base Character Class
class Character:
    def __init__(self, name, health, attack, character_class):
        self.name = name
        self.health = health
        self.attack = attack
        self.character_class = character_class
        self.inventory = []

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
                self.health += 30
                self.inventory.remove(item)
                print("Your Health Has Been Restored By 30")
                return
            print("You Have No More Health Potions :((")

    def to_dict(self):
        return {"name": self.name, "health": self.health, "attack": self.attack,
                "character_class": self.character_class, "inventory": self.inventory}
    
    @classmethod
    def from_dict(cls, data):
        character = cls(data["name"], data["health"], data["attack"], data["character_class"])
        character.inventory = data["inventory"]
        return character

    def __str__(self):
        return f"{self.name}: {self.character_class}, {self.health} HP, {self.attack} Damage, Inventory: {self.inventory}"

# Playable Subclasses
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health = 120, attack = 15, character_class = "Warrior")
        self.ability = "Enraged Attack"
        self.add_to_inventory("Rusted Sword")
        self.add_to_inventory("Health Potion")

    def use_ability(self):
        return self.attack + 10

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health = 100, attack = 20, character_class = "Wizard")
        self.ability = "Fireball"
        self.add_to_inventory("Iron Staff")
        self.add_to_inventory("Health Potion")

    def use_ability(self):
        return self.attack +15

class Cleric(Character):
    def __init__(self, name):
        super().__init__(name, health = 100, attack = 10, character_class = "Cleric")
        self.ability = "Heal"
        self.add_to_inventory("Staff of Moderate Healing")
        self.add_to_inventory("Health Potion")

    def use_ability(self):
        self.health += 20

# Mob Subclasses
class Skeleton(Character):
    def __init__(self):
        super().__init__("Skeleton", health = 30, attack = 15, character_class = "Mob")

    def drop_loot(self, player):
        loot = random.choice(["Gold", "Health Potion", "Wooden Bow"]) 
        player.add_to_inventory(loot)

class Orc(Character):
    def __init__(self):
        super().__init__("Orc", health = 50, attack = 10, character_class = "Mob")

    def drop_loot(self, player):
        loot = random.choice(["Gold", "Health Potion", "Iron Sword"])
        player.add_to_inventory(loot)

class Dragon(Character):
    def __init__(self):
        super().__init__("Dragon", health = 150, attack = 25, character_class = "Boss")

    def drop_loot(self, player):
        loot = random.choice(["Gold", "Dragon's Blood Potion", "Dragon's Scale Armor"])
        player.add_to_inventory(loot)    
