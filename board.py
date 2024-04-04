import numpy as np

class Board:
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.board = np.empty((6, 7), dtype=str)

    def print_board(self):
        print(self.board)

    def mark_space(self, row, col, player):
        modified_row = row + 1
        modified_col = col + 1
        if 0 < modified_row < 6 and 0 < modified_col < 7:
            if self.board[row][col] == '':
                self.board[row][col] = piece
                return True
            else: 
                print("This space is already filled")
                return False
        else:
            print("Those coordinates are out of bounds! Try again.")
            return False
    
    def check_win(self, row, col, player):
        # Veritcal
        # Horizontal
        # Diagonal
        pass

    def __str__(self):
        return str(self.board)