import sys
from game import Game

def main():
    print("==== CONNECT FOUR ====")
    print("Welcome! Please enter the names for player 1 and 2.")
    name1 = input("Player 1: ")
    name2 = input("Player 2: ")
    game = Game(name1, name2)
    while True:
        print("=== {}'s Turn ===".format(game.current_player.name))
        col = int(input("Please enter the column (1-7) you drop a piece in: ")) - 1
        result = game.play(col)
        # Break the while loop if either game over condition is met
        if result == "Draw":
            break
        if result == "Win":
            break
    play_again()

# Play again function
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