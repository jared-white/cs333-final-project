import numpy as np

# Board class
class Board:
    # Initialzation
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.board = np.full((6, 7), ' ')

    # Ensures the board is printed instead of the object address    
    def __str__(self):
        return str(self.board)

    # Display the board
    def print_board(self):
        print("The current board:")
        print(self.board)

    # Drops the current player's piece into the appropriate position based off the column selected and rows left
    def drop_piece(self, col, piece):
        row = self.rows - 1
        # While the row is greater than/equal to 0
        while row >= 0:
            # Check if this particlar spot on the board is blank
            if self.board[row][col] == ' ':
                # If it is, fill this spot in the array with the current player's piece
                self.board[row][col] = piece
                return True
            # Decrement the row since we are "dropping in" pieces
            row -= 1
        return None # The column is full

    # Checks if the board is full/draw condition
    def full_board(self):
        return ' ' not in self.board[0] 
    
    # Checks for win conditions
    def check_win(self, piece):
        # Check rows for win condition
        for row in range(self.rows):
            for col in range(self.cols - 3): # Ensures the loop does not check columns out of bounds
                if np.all(self.board[row, col:col+4] == piece):
                    return True

        # Check columns for win condition
        for col in range(self.cols):
            for row in range(self.rows - 3): # Ensures the loop does not check rows out of bounds
                if np.all(self.board[row:row+4, col] == piece):
                    return True

        # Check diagonals for win condition
        for row in range(self.rows - 3): # Ensures rows out of bounds are not checked
            for col in range(self.cols - 3): # Ensures columns out of bounds are not checked
                if np.all(self.board[row:row+4, col:col+4].diagonal() == piece):
                    return True
                if np.all(np.fliplr(self.board[row:row+4, col:col+4]).diagonal() == piece):
                    return True

        # No win condition met
        return False