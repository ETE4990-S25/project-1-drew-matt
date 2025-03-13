from IPython.display import clear_output # Delete from main game
import os
def clear_screen():
    # Clear the terminal (This was copied from ChatGPT)
    os.system('cls' if os.name == 'nt' else 'clear')
    

# Display the Main Menu
def display_main_menu():
    print("Welcome to the Game!")
    print("(1) Start the game")
    print("(2) Options")
    print("(3) Quit Game")

# Begin the game
def start_game():
    print("Starting the Game . . .")

    print("Game Over! Press Enter to Return to Main Menu.")
    input("Press Enter to Continue")

# Enter Options Menu
def display_options_menu():
    print("Options Menu")
    print("(1) Change the Difficulty")  
    print("(2) Back to Main Menu")    

def display_option_difficulty():
    print("Difficulty Options:")
    print("(1) Easy Mode")
    print("(2) Intermediate Mode")
    print("(3) Hardcore Mode")
    input("Select a Difficulty Option (Enter a Number 1-3)")