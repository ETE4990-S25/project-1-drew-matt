#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.max_health = health

    def attack(self, enemy):
        enemy.health -= self.weapon.damage
        enemy.health = max(enemy.health, 0)

    def equip(self, weapon):
        self.weapon = weapon
        print(f"{self.name} has equipped {self.weapon.name}")
        
class Warrior(Character):
    def __init__(self, name, health=100):
        super().__init__(name=name, health=health)
        self.weapon = basic_sword

class Mage(Character):
    def __init__(self, name, health=75):
        super().__init__(name=name, health=health)
        self.weapon = basic_staff


# In[ ]:




