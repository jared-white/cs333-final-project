from board import Board
from player import Player

class Game:
    def __init__(self, name1, name2):
        self.board = Board()

        self.player1 = Player(name1, '●')
        self.player2 = Player(name2, '○')

        self.current_player = self.player1

    def change_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2;
        else:
            self.current_player = self.player1;

    def play(self):
        while not self.board.full_board():
            self.board.print_board()
            print("=== {}'s Turn ===".format(self.current_player.name))
            col = int(input("Please enter the column (1-7) you drop a piece in: ")) - 1
            if col > 6 or col < 0:
                print("That move is not valid. Please try again!")
                continue
            if not self.board.drop_piece(col, self.current_player.piece):
                print("This column is full! Please select a different column")
                continue
            if self.board.check_win(self.current_player.piece):
                self.board.print_board()
                print("{} wins!".format(self.current_player.name))
                break
            self.change_player()
            print("Draw!")