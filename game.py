from board import Board
from player import Player

# Game class
class Game:
    # Initialization
    def __init__(self, name1, name2):
        self.board = Board()

        self.player1 = Player(name1, '●')
        self.player2 = Player(name2, '○')

        self.current_player = self.player1

    # Function to change the player turns
    def change_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2;
        else:
            self.current_player = self.player1;

    # Handles playing the game itself
    def play(self, col):
        # If the board is full, a draw has occurred and the game is over
        if self.board.full_board():
            return "Draw"
        # If the given column is out of bounds, let the player know the move is invalid
        if col > 6 or col < 0:
            print("That move is not valid. Please try again!")
            return False
        # If the Board drop_piece function returns "None", that means this particular column is full and the player will need to select a different column
        if self.board.drop_piece(col, self.current_player.piece) is None:
            print("This column is full! Please select a different column")
            return False
        # Check for a win after the prior three if conditions have been checked, if a player wins, return this
        if self.board.check_win(self.current_player.piece):
            self.board.print_board()
            print("{} wins!".format(self.current_player.name))
            return "Win"
        # Print the board and change the player after each move
        self.board.print_board()
        self.change_player()