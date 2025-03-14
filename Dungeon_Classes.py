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
            
            # Handle Player Actions
            action = input("Do You Want to (1) attack, (2) use an ability or (3) use a health potion? ")
            if action == '1':
                mob.take_damage(player.attack)
            elif action == '2':
                if player.character_class == 'Warrior':
                    mob.take_damage(player.use_ability())
                elif player.character_class == 'Mage':
                    mob.take_damage(player.use_ability())
                elif player.character_class == 'Cleric':
                    player.use_ability()
            elif action == '3':
                player.use_potion()

            if mob.is_alive():
                player.take_damage(mob.attack)
        
        # Handle Victory or Death of the Player
        if player.is_alive():
            print(f"You Have Defeated the {mob.name}")
            mob.drop_loot(player)
        else:
            print(f"The {mob.name} has impaled you  against the wall . . .")
    
    def fight_boss(self, player):
        boss = Dragon()
        print("You have reached the final level, a Dragon lumbers down from a mountain of gold")
        while boss.is_alive() and player.is_alive():
            print(player)
            print(boss)
            action = input("Do You Want to (1) attack, (2) use an ability or (3) use a health potion? ")

            if action == '1':
                boss.take_damage(player.attack)
            elif action == '2':
                if player.character_class == 'Warrior':
                    boss.take_damage(player.use_ability())
                elif player.character_class == 'Mage':
                    boss.take_damage(player.use_ability())
                elif player.character_class == 'Cleric':
                    player.use_ability()
            elif action == '3':
                player.use_potion()

            if boss.is_alive():
                player.take_damage(boss.attack)
        if player.is_alive():
            print("Congratulations on Killing the Dragon and Beating the Game!")
            boss.drop_loot(player)
        else:
            print("The Dragon has seared off your face . . .")

    
    def enter_room(self, player):
        if self.room_type == "treasure":
            print("Congratulations! You Have Found a "
            "Treasure Room! You May Obtain a Random Item")

            player.add_to_inventory(random.choice(["Gold", "Health Potion", "Magic Cloak"]))
        elif self.room_type == "mob":
            self.fight_mob(player)
        elif self.room_type == "boss":
            self.fight_boss(player)

class Dungeon:
    def __init__(self, floors = random.randint(5, 10)):
        self.floors = floors
    
    def generate_floor(self, floor_number):
        if floor_number == self.floors:
            return Room("boss")
        else:
            return Room(random.choice(["treasure", "mob"]))
        
    def run_dungeon(self, player):
        for floor in range(1, self.floors + 1):
            print(f"\n--- Floor {floor} ---")
            room = self.generate_floor(floor)
            room.enter_room(player)
            if not player.is_alive():
                break
            if floor < self.floors:
                input("Press Enter to Enter the Next Room")
                
        
