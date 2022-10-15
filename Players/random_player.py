import random
from player import Player

class RandomPlayer(Player):

    def play(board: Board, valid_moves: List) -> str:
        move = random.choice(valid_moves)
        return move
