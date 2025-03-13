from IPython.display import clear_output # Delete from main game
import os
import menu 

def main():
    playing = True
    while playing:

        menu.display_main_menu()
        choice = input("Please Select One (Enter a number 1 - 3): ")
        clear_output(wait=True)

        # Play the Game
        if choice == '1':
            menu.start_game()
            clear_output(wait=True)
            
        # Open the Options Menu
        elif choice == '2':
            options_open = True
            
            while options_open:
                menu.display_options_menu()
                option_choice = input("Select an Option (1 or 2)")
                clear_output(wait=True)
                
                if option_choice == '1':
                    menu.display_option_difficulty()
                    clear_output(wait=True)
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
    