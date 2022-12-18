import random
from players.player import Player
from game.board import Board

class RandomPlayer(Player):

    def play(board: Board, valid_moves: list) -> str:
        move = random.choice(valid_moves)
        return move
