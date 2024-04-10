import unittest
import numpy as np
from board import Board
from game import Game

class TestConnectFourClass(unittest.TestCase):
    def setUp(self):
        self.test_board = Board()
        player1 = "Player 1"
        player2 = "Player 2"
        self.test_game = Game(player1, player2)

    # Tests that the Board object properly initalized 
    def test_board_initalization(self):
        self.assertIsNotNone(self.test_board.board)

    # Tests drop_piece() "drops" a player's piece into a column
    def test_drop_piece(self):
        empty_board = np.full((6, 7), ' ')
        self.test_board.drop_piece(0, '●')
        np.all(np.not_equal(self.test_board, empty_board))

    # Tests that full_board() properly returns "False" if the board is not full 
    def test_full_board_false(self):
        self.test_board.board[0] = ['●', '●', '●', '●', ' ', ' ', ' ']
        result = self.test_board.full_board()
        self.assertFalse(result)

    # Tests that full_board() properly returns "True" if the board is full
    def test_full_board(self):
        # Fill the board completely
        for col in range(self.test_board.cols):
            for row in range(self.test_board.rows):
                self.test_board.board[row][col] = '●'
        # Check that the board is full
        result = self.test_board.full_board()
        self.assertTrue(result)

    # Tests that drop_piece() doesn't allow a piece to be dropped in a full row
    # drop_piece() returns None if the column is full
    def test_drop_piece_full(self):
        for _ in range(self.test_board.rows):
            self.test_board.drop_piece(0, '●')
        result = self.test_board.drop_piece(0, '●')
        self.assertIsNone(result)

    # Test check_win() row win condition
    def test_check_win_row(self):
        self.test_board.board[0] = ['●', '●', '●', '●', ' ', ' ', ' ']
        result = self.test_board.check_win('●')
        self.assertTrue(result)

    # Test check_win() column win condition
    def test_check_col_win(self):
        for row in range(4):
            self.test_board.board[row][0] = '●'
        result = self.test_board.check_win('●')
        self.assertTrue(result)

    # Test check_win() diagonal win condition
    def test_check_diag_row(self):
        for i in range(4):
            self.test_board.board[i][i] = '●'
        result = self.test_board.check_win('●')
        self.assertTrue(result)

    # Test check_win() returns False if no win condition is met
    def test_check_no_win(self):
        self.test_board.drop_piece(0, '●')
        result = self.test_board.check_win('●')
        self.assertFalse(result)        

    # Tests that the Board and Player objects are properly created within the Game class
    # Therefore, they should exist
    # Integration test
    def test_game_initalization(self):
        self.assertIsNotNone(self.test_game.board)
        self.assertIsNotNone(self.test_game.player1)
        self.assertIsNotNone(self.test_game.player2)

    # Tests that the Game will properly place the piece on the Board
    # Integration test
    def test_player_move(self):
        self.assertEqual(str(self.test_game.board), str(self.test_board)) # Assert empty
        
        self.test_game.play(0)
        self.test_board.drop_piece(0, '●') # This is what test_game is expected to do

        np.testing.assert_array_equal(self.test_game.board.board, self.test_board.board)

    # Tests that the player cannot make a move in a column that's out of bounds and that the game recognizes this
    def test_out_of_bounds_move(self):
        result = self.test_game.play(8)
        self.assertFalse(result)

    # Tests that the Game class recognizes when a column is full
    def test_game_full_board(self):
        for _ in range(self.test_game.board.cols):
           result = self.test_game.play(0)
        self.assertFalse(result)

    # Tests that the Game sees and properly returns when a win condition is met
    # Integration test
    def test_win_condition(self):
        self.test_game.board.drop_piece(0, '●')
        self.test_game.board.drop_piece(1, '●')
        self.test_game.board.drop_piece(2, '●')
        result = self.test_game.play(3)
        self.assertEqual(result, 'Win')

    # Tests draw condition => the board is full
    # Purposefully overrides the win condition
    # Integration test
    def test_draw_condition(self):
        for col in range(self.test_game.board.cols):
            for _ in range(self.test_game.board.rows):
                self.test_game.play(col)
        result = self.test_game.play(0)
        self.assertEqual(result, 'Draw')

    # Tests that change_player() swaps Player objects
    def test_change_player(self):
        current_player1 = self.test_game.current_player
        self.test_game.change_player()
        current_player2 = self.test_game.current_player
        self.assertNotEqual(current_player1, current_player2)

    # Tests that the Game appropriately swaps players
    # Integration test
    def test_player_switch(self):
        current_player1 = self.test_game.current_player
        self.test_game.play(0)
        current_player2 = self.test_game.current_player
        self.assertNotEqual(current_player1, current_player2)

if __name__ == "__main__":
    unittest.main()