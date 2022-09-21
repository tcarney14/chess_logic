import numpy as np
from pieces import Pieces
from enum import Enum

class Board:

    class Ranks(Enum):
        FIRST = 0
        SECOND = 1
        THIRD = 2
        FOURTH = 3
        FIFTH = 4
        SIXTH = 5
        SEVENTH = 6
        EIGHTH = 7

    class Files(Enum):
        A = 0
        B = 1
        C = 2
        D = 3
        E = 4
        F = 5
        G = 6
        H = 7

    default_config = [{"rank": Ranks.SECOND, "file": Files.C, "piece": Pieces.KNIGHT},
                        {"rank": Ranks.FIFTH, "file": Files.E, "piece": Pieces.BISHOP}]

    def __init__(self, config=default_config):
        self.board = np.zeros((8,8))

        self.setup(config)

    def setup(self, config):
        for piece in config:
            self.board[piece["rank"].value][piece["file"].value] = piece["piece"].value


    def display(self):
        print(self.board)