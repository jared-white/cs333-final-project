import sys
from game import Game

def main():
    print("==== CONNECT FOUR ====")
    print("Welcome! Please enter the names for player 1 and 2.")
    name1 = input("Player 1: ")
    name2 = input("Player 2: ")
    game = Game(name1, name2)
    game.play()
    play_again()

def play_again():
    print("\n=== PLAY AGAIN? ===")
    print("Would you like to play again or quit the game?")
    selection = None
    while selection != 'play' and selection != 'quit':
        selection = input("Please enter 'play' or 'quit': ").lower()
        if selection == 'play':
            main()
        elif selection == 'quit':
            print("Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()