from game.board import Board
from players.player import Player
from game import logic
import time

class Game:

    def __init__(self, board: Board, player1: Player, player2: Player):
        self.board = board
        self.players = [player1, player2]

    def play(self):

        mate = logic.check_mates(self.board)

        while not mate:

            cur_player = self.players[self.board.ply]

            valid_moves = logic.get_valid_moves(self.board)

            move = cur_player.play(self.board, valid_moves)
            print(move)

            self.board.execute_move(move)

            mate = logic.check_mates(self.board)

            self.board.display()
            time.sleep(5)
            self.board.advance_turn()
