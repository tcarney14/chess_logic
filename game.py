from board import Board
from Players.player import Player
from logic import ChessLogic

class Game:

    def __init__(self, board: Board, player1: Player, player2: Player):
        self.board = board
        self.players = [player1, player2]

    def play(self):

        mate = False

        while not mate:

            cur_player = self.players[self.board.ply]

            valid_moves = ChessLogic.get_valid_moves(self.board)

            move = cur_player.play(self.board, valid_moves)

            self.board.execute_move(move)

            mate = ChessLogic.check_mates(self.board)

            self.board.advance_turn()
