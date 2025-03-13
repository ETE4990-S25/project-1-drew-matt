import os
import menu 
import Save_System
from Char_Classes import *
from Dungeon_Classes import Dungeon

def new_game():
    print("Welcome to our Python Dungeon Crawler Game!")
    name = input("Enter a name for your character: ")
    
    print("Choose Your Class: ")
    print("(1) Warrior")
    print("(1) Mage")
    print("(1) Cleric")
    choice = input("Enter Your Class Choice (Pick 1 - 3):")

    if choice == '1':
        player = Warrior(name)
    elif choice == '2':
        player = Mage(name)
    elif choice == '3':
        player = Cleric(name)
    else:
        print("Invalid Option. Selecting Default option (Warrior)")
        player = Warrior(name)
    
    dungeon = Dungeon()
    
    dungeon.run_dungeon(player)
    
    Save_System.save_game(player)

def main():
    playing = True
    while playing:
        os.system('cls')
        menu.display_main_menu()
        choice = input("Please Select One (Enter a number 1 - 4): ")
        os.system('cls')

        # Play the Game
        if choice == '1':
            menu.start_game()
            new_game()
            os.system('cls')
        # Load Game from Save File
        elif choice == '2':
            player = Save_System.load_game()
            if player:
                dungeon = Dungeon()
                dungeon.run_dungeon(player)

        # Open the Options Menu
        elif choice == '3':
            options_open = True
            
            while options_open:
                menu.display_options_menu()
                option_choice = input("Select an Option (1 or 2): ")
                os.system('cls')
                
                if option_choice == '1':
                    menu.display_option_difficulty()
                    os.system('cls')
                elif option_choice == '2':
                    print("Returning to Main Menu")
                    options_open = False
                else:
                    print("Invalid option, please try again.")
                    input("Press Enter to Continue...")

        # Quit the Game
        elif choice == '3':

            print("Thank You For Playing! Goodbye!")
            playing = False
        
        # Handle Numbers Outside of 1-3
        else:
            print("Invalid option, please try again.")
            input("Press Enter to Continue...")




if __name__ == "__main__":
    main()
    