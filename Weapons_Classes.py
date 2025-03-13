#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Weapon:
    def __init__(self, name, damage, value):
        self.name = name
        self.damage =damage
        self.value = value
        
class Melee(Weapon):
    def __init__(self, name, damage, value):
        super().__init__(name=name, damage=damage, value=value)

class Ranged(Weapon):
    def __init__(self, name, damage, value):
        super().__init__(name=name, damage=damage, value=value)

basic_sword = Melee(name="basic_sword", damage=5, value=1)

basic_staff = Ranged(name="basic_staff", damage=8, value=2)
    

