import random
from Char_Classes import Character, Warrior, Mage, Cleric, Skeleton, Orc, Dragon
class Room:
    def __init__(self, room_type):
        self.room_type = room_type

    def fight_mob(self, player):
        mob = random.choice([Skeleton(), Orc()])
        print(f"A {mob.name} has stepped out from the shadows")
        
        while mob.is_alive() and player.is_alive():
            print(player)
            print(mob)

            action = input("Do You Want to (1) attack, (2) use an ability or (3) use a health potion? ")
            if action == '1':
                mob.take_damage(player.attack)
            elif action == '2':
                if player.character_type == 'Warrior':
                    mob.take_damage(player.use_ability())
    
    def enter_room(self, player):
        if self.room_type == "Treasure":
            print("Congratulations! You Have Found a "
            "Treasure Room! You May Obtain a Random Item")

            player.add_to_inventory(random.choice(["Gold", "Health Potion", "Magic Cloak"]))