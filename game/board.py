from typing import Tuple
import numpy as np
from game.pieces import Pieces
import operator
from texttable import Texttable

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
        self.board = np.zeros((8,8), dtype=int)
        self.ply = Board.WHITE
        self.setup(config)

    def setup(self, config):
        for piece in config["White"]:
            file_, rank = self.square_str_to_index(piece["square"])
            self.board[file_][rank] = piece["piece"].value
        for piece in config["Black"]:
            file_, rank = self.square_str_to_index(piece["square"])
            self.board[file_][rank] = piece["piece"].value * -1

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
        
        self.board = np.flip(self.board, 0)

    def execute_move(self, move: Tuple):
        start_square, dest_square = move
        start_file, start_rank = start_square
        dest_file, dest_rank = dest_square
        
        self.board[dest_file][dest_rank] = self.board[start_file][start_rank]

        self.board[start_file][start_rank] = 0

    def square_occupied(self, file_: int, rank: int):
        """Check if any piece occupies given square"""
        return self.square_occupied_self(file_, rank) or self.square_occupied_opponent(file_, rank)

    def square_occupied_self(self, file_: int, rank: int):
        """Check whether current player has a piece on the given square."""
        comparison = self._get_focus("cur")

        square = self.board[file_][rank]
        if comparison(square, 0):
            return True
        else:
            return False

    def square_occupied_opponent(self, file_: int, rank: int):
        """Check whether opponent has a piece on the given square."""
        comparison = self._get_focus("opp")

        square = self.board[file_][rank]
        if comparison(square, 0):
            return True
        else:
            return False
    
    def _get_focus(self, focus: str):
        """
        Get comparison operator which tells us if given player's pieces 
        are represented by positive or negative integers on board

        parameters:
            focus: str - either "cur" or "opp"
        returns:
            comparison - gt or lt operator
        """

        if focus == "cur":
            #if it's white's turn, we care about positive valued pieces
            if self.ply == 0:
                comparison = operator.gt
            else:
                comparison = operator.lt
        elif focus == "opp":
            #if it's white's turn, we care about negative valued pieces
            if self.ply == 0:
                comparison = operator.lt
            else:
                comparison = operator.gt

        return comparison

    def get_pieces(self) -> list:
        """Gets the current player's pieces"""
        pieces = []
        comparison = self._get_focus("cur")
        for i, row in enumerate(self.board):
            for j, square in enumerate(row):
                if comparison(square, 0):
                    piece = {"file": i, "rank": j, "piece": int(abs(square))}
                    pieces.append(piece)

        return pieces

    def display(self):
        char_board = self.to_char_matrix()
        table = Texttable()
        table.add_rows(char_board, header=False)
        print(table.draw())




    def to_char_matrix(self):
        """Converts integer board matrix into chars"""

        mapping = {
            Pieces.KING.value: "K",
            Pieces.QUEEN.value: "Q",
            Pieces.BISHOP.value: "B",
            Pieces.KNIGHT.value: "N",
            Pieces.ROOK.value: "R",
            Pieces.PAWN.value: "P",
            0: "  "
        }

        rows = []
        for row in self.board:
            char_row = []
            for square in row:
                char_row.append(mapping[int(abs(square))])
            rows.append(char_row)
        
        return rows