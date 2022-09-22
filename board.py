from typing import Tuple
import numpy as np
from pieces import Pieces
from enum import Enum

class Board:

    # map chessboard rank to numpy array represenation index
    rank_to_index = {"1": 0, 
                    "2": 1,
                    "3": 2,
                    "4": 3,
                    "5": 4,
                    "6": 5,
                    "7": 6,
                    "8": 7}

    # map chessboard file to numpy array representation index
    file_to_index = {"a": 0,
                    "b": 1,
                    "c": 2,
                    "d": 3,
                    "e": 4,
                    "f": 5,
                    "g": 6,
                    "h": 7}

    # initial chessboard setup
    default_config = {
        "White": [
            {"square": "a1", "piece": Pieces.ROOK},
            {"square": "b1", "piece": Pieces.KNIGHT},
            {"square": "c1", "piece": Pieces.BISHOP},
            {"square": "d1", "piece": Pieces.QUEEN},
            {"square": "e1", "piece": Pieces.KING},
            {"square": "f1", "piece": Pieces.BISHOP},
            {"square": "g1", "piece": Pieces.KNIGHT},
            {"square": "h1", "piece": Pieces.ROOK},
            {"square": "a2", "piece": Pieces.PAWN},
            {"square": "b2", "piece": Pieces.PAWN},
            {"square": "c2", "piece": Pieces.PAWN},
            {"square": "d2", "piece": Pieces.PAWN},
            {"square": "e2", "piece": Pieces.PAWN},
            {"square": "f2", "piece": Pieces.PAWN},
            {"square": "g2", "piece": Pieces.PAWN},
            {"square": "h2", "piece": Pieces.PAWN},
            ],
        "Black": [
            {"square": "a8", "piece": Pieces.ROOK},
            {"square": "b8", "piece": Pieces.KNIGHT},
            {"square": "c8", "piece": Pieces.BISHOP},
            {"square": "d8", "piece": Pieces.QUEEN},
            {"square": "e8", "piece": Pieces.KING},
            {"square": "f8", "piece": Pieces.BISHOP},
            {"square": "g8", "piece": Pieces.KNIGHT},
            {"square": "h8", "piece": Pieces.ROOK},
            {"square": "a7", "piece": Pieces.PAWN},
            {"square": "b7", "piece": Pieces.PAWN},
            {"square": "c7", "piece": Pieces.PAWN},
            {"square": "d7", "piece": Pieces.PAWN},
            {"square": "e7", "piece": Pieces.PAWN},
            {"square": "f7", "piece": Pieces.PAWN},
            {"square": "g7", "piece": Pieces.PAWN},
            {"square": "h7", "piece": Pieces.PAWN},
        ]
    }

    def __init__(self, config=default_config):
        self.board = np.zeros((8,8))
        self.ply = "White"
        self.setup(config)

    def setup(self, config):
        for piece in config["White"]:
            file, rank = self.square_str_to_index(piece["square"])
            self.board[rank][file] = piece["piece"].value
        for piece in config["Black"]:
            file, rank = self.square_str_to_index(piece["square"])
            self.board[rank][file] = piece["piece"].value * -1

    def square_str_to_index(self, square: str) -> Tuple:
        """
        
        """
        file = Board.file_to_index[square[0]]
        rank = Board.rank_to_index[square[1]]

        return (file, rank)

    def advance_turn(self):
        if self.ply == "White":
            self.ply = "Black"
        else:
            self.ply = "White"
        

    def display(self):
        print(self.board)