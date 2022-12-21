from players.player import Player
from game.board import Board
import numpy as np
from copy import deepcopy
import random

class GreedyPlayer(Player):

    def play(self, board: Board, valid_moves: list) -> str:
        # choose random move to start
        lookahead_board = deepcopy(board)
        best_move = random.choice(valid_moves)
        lookahead_board.execute_move(best_move)
        best_score = lookahead_board.material_difference()

        for move in valid_moves:
            lookahead_board = deepcopy(board)
            lookahead_board.execute_move(move)
            score = lookahead_board.material_difference()
            if score > best_score:
                best_move = move
                best_score = score
        
        return best_move