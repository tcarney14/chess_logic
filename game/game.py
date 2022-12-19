from game.board import Board
from players.player import Player
from game import logic
import time

class Game:

    def __init__(self, board: Board, player1: Player, player2: Player):
        self.board = board
        self.players = [player1, player2]

    def play(self):

        valid_moves = logic.get_valid_moves(self.board)
        mate = logic.check_mates(self.board, valid_moves)

        while not mate:

            import pdb
            pdb.set_trace()

            cur_player = self.players[self.board.ply]

            move = cur_player.play(self.board, valid_moves)
            print(move)

            self.board.execute_move(move)
            self.board.advance_turn()
            
            valid_moves = logic.get_valid_moves(self.board)
            mate = logic.check_mates(self.board, valid_moves)

            self.board.display()
            time.sleep(5)
            
