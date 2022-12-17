from typing import List
from board import Board

class ChessLogic:

    def get_valid_moves(board: Board, int: ply) -> List:
        moves = []
        for 

    def _pawn_moves(file_: int, rank: int) -> List:
        
        moves = []
        moves.append((file_, rank + 1))
        moves.append((file_, rank + 2))
        moves.append((file_ + 1, rank + 1))
        moves.append((file_ - 1, rank + 1))
        
        return moves

    def _king_moves(file_: int, rank: int) -> List:
        moves = []

        moves.append((file_, rank + 1))
        moves.append((file_, rank - 1))
        moves.append((file_ + 1, rank))
        moves.append((file_ - 1, rank))
        moves.append((file_ + 1, rank + 1))
        moves.append((file_ - 1, rank + 1))
        moves.append((file_ + 1, rank - 1))
        moves.append((file_ - 1, rank - 1))

        return moves

    def _bishop_moves(file_: int, rank: int) -> List:
        moves = []

        cur_rank = rank
        cur_file_ = file_
        cur_rank +=1
        cur_file_ +=1
        while ChessLogic._on_board(cur_file_, cur_rank):
            moves.append((cur_file_, cur_rank))
            cur_rank += 1
            cur_file_ += 1
        
        cur_rank = rank
        cur_file_ = file_
        cur_rank +=1
        cur_file_ -=1
        while ChessLogic._on_board(cur_file_, cur_rank):
            moves.append((cur_file_, cur_rank))
            cur_rank += 1
            cur_file_ -= 1

        cur_rank = rank
        cur_file_ = file_
        cur_rank -=1
        cur_file_ -=1
        while ChessLogic._on_board(cur_file_, cur_rank):
            moves.append((cur_file_, cur_rank))
            cur_rank -= 1
            cur_file_ -= 1
        
        cur_rank = rank
        cur_file_ = file_
        cur_rank -=1
        cur_file_ +=1
        while ChessLogic._on_board(cur_file_, cur_rank):
            moves.append((cur_file_, cur_rank))
            cur_rank -= 1
            cur_file_ += 1

        return moves

    def _rook_moves(file_: int, rank: int) -> List:
        moves = []

        cur_rank = rank
        cur_file_ = file_
        cur_rank +=1
        while ChessLogic._on_board(cur_file_, cur_rank):
            moves.append((cur_file_, cur_rank))
            cur_rank += 1
        
        cur_rank = rank
        cur_file_ = file_
        cur_rank -=1
        while ChessLogic._on_board(cur_file_, cur_rank):
            moves.append((cur_file_, cur_rank))
            cur_rank -= 1

        cur_rank = rank
        cur_file_ = file_
        cur_file_ +=1
        while ChessLogic._on_board(cur_file_, cur_rank):
            moves.append((cur_file_, cur_rank))
            cur_file_ += 1
        
        cur_rank = rank
        cur_file_ = file_
        cur_file_ -=1
        while ChessLogic._on_board(cur_file_, cur_rank):
            moves.append((cur_file_, cur_rank))
            cur_file_ -= 1

        return moves

    def _queen_moves(file_: int, rank: int) -> List:
        return _bishop_moves + _rook_moves
    
    def _knight_moves(file_: int, rank: int) -> List:
        moves = []

        moves.append((file_ - 1, rank + 2))
        moves.append((file_ + 1, rank + 2))
        moves.append((file_ - 2, rank + 1))
        moves.append((file_ + 2, rank + 1))
        moves.append((file_ - 2, rank - 1))
        moves.append((file_ + 2, rank - 1))
        moves.append((file_ - 1, rank - 2))
        moves.append((file_ + 1, rank - 2))

        return moves

            
    @staticmethod
    def _on_board(file_: int, rank: int) -> bool:
        if rank < 0 or rank > 7:
            return False
        if file_ < 0 or file_ > 7:
            return False
        return True