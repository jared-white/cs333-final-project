from game import Game

def main():
    print("Welcome! Please enter the names for player 1 and 2.")
    name1 = input("Player 1: ")
    name2 = input("Player 2: ")
    game = Game(name1, name2)

if __name__ == "__main__":
    main()