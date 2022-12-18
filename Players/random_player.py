import random
from players.player import Player
from game.board import Board

class RandomPlayer(Player):

    def play(self, board: Board, valid_moves: list) -> str:
        move = random.choice(valid_moves)
        return move
