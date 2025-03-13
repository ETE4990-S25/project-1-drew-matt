import random

# Base Character Class
class Character:
    def __init__(self, name, health, attack, character_class):
        self.name = name
        self.health = health
        self.attack = attack
        self.character_class = character_class
        self.inventory = []

# Playable Subclasses
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health = 120, attack = 15, character_class = "Warrior")
        self.ability = "Enraged Attack"
        
    def use_ability(self):
        return self.attack + 10

class Wizard(Character):
    def __init__(self, name):
        super().__init__(name, health = 100, attack = 20, character_class = "Wizard")
        self.ability = "Fireball"

    def use_ability(self):
        return self.attack +15

class Cleric(Character):
    def __init__(self, name):
        super().__init__(name, health = 100, attack = 10, character_class = "Cleric")
        self.ability = "Heal"

    def use_ability(self):
        self.health += 20

# Mob Subclasses
class Skeleton(Character):
    def __init__(self):
        super().__init__("Skeleton", health = 30, attack = 15, character_class = "Mob")

    def drop_loot(self, player):
        loot = random.choice(["Gold", "Health Potion", "Wooden Bow"]) 

class Orc(Character):
    def __init__(self):
        super().__init__("Orc", health = 50, attack = 10, character_class = "Mob")

    def drop_loot(self, player):
        loot = random.choice(["Gold", "Health Potion", "Iron Sword"])

class Dragon(Character):
    def __init__(self):
        super().__init__("Dragon", health = 150, attack = 25, character_class = "Boss")

    def drop_loot(self, player):
        loot = random.choice(["Gold", "Dragon's Blood Potion", "Dragon's Scale Armor"])    