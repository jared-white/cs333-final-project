import numpy as np
from board import Board
from player import Player

class Game:
    def __init__(self, name1, name2):
        self.board = Board()

        self.player1 = Player(name1, '●')
        self.player2 = Player(name2, '○')

        self.current_player = self.player1

    def change_player(self):
        pass

    def play(self):
        pass