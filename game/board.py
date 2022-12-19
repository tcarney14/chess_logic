from typing import Tuple
import numpy as np
from game.pieces import Pieces
import operator

class Board:

    WHITE = 0
    BLACK = 1

    # map chessboard rank to numpy array represenation index
    rank_to_index = {"1": 0, 
                    "2": 1,
                    "3": 2,
                    "4": 3,
                    "5": 4,
                    "6": 5,
                    "7": 6,
                    "8": 7}

    # map chessboard file_ to numpy array representation index
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
        self.ply = Board.WHITE
        self.setup(config)

    def setup(self, config):
        for piece in config["White"]:
            file_, rank = self.square_str_to_index(piece["square"])
            self.board[rank][file_] = piece["piece"].value
        for piece in config["Black"]:
            file_, rank = self.square_str_to_index(piece["square"])
            self.board[rank][file_] = piece["piece"].value * -1

    def square_str_to_index(self, square: str) -> Tuple:
        """
        
        """
        file_ = Board.file_to_index[square[0]]
        rank = Board.rank_to_index[square[1]]

        return (file_, rank)

    def advance_turn(self):
        if self.ply == Board.WHITE:
            self.ply = Board.BLACK
        else:
            self.ply = Board.WHITE

    def execute_move(self, move: Tuple):
        start_square, dest_square = move
        start_file, start_rank = start_square
        dest_file, dest_rank = dest_square
        
        self.board[dest_file][dest_rank] = self.board[start_file][start_rank]

        self.board[start_file][start_rank] = 0

    def display(self):
        print(self.board)

    def get_pieces(self) -> list:
        pieces = []
        if self.ply == 1:
            comparison = operator.gt
        else:
            comparison = operator.lt
        for i, row in enumerate(self.board):
            for j, square in enumerate(row):
                if comparison(square, 0):
                    piece = {"rank": i, "file": j, "piece": int(abs(square))}
                    pieces.append(piece)

        return pieces




