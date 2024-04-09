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

    def play(self, col):
        if self.board.full_board():
            return "Draw"
        if col > 6 or col < 0:
            print("That move is not valid. Please try again!")
            return False
        if self.board.drop_piece(col, self.current_player.piece) is None:
            print("This column is full! Please select a different column")
            return False
        if self.board.check_win(self.current_player.piece):
            self.board.print_board()
            print("{} wins!".format(self.current_player.name))
            return "Win"
        self.board.print_board()
        self.change_player()