from typing import List
from board import Board

class ChessLogic:

    def get_valid_moves(board: Board, int: ply) -> List:
        moves = []
        for 

    def _pawn_moves(rank: int, file: int) -> List:
        
        moves = []
        moves.append((rank + 1, file))
        moves.append((rank + 2, file))
        moves.append((rank + 1, file + 1))
        moves.append((rank + 1, file -1))
        
        return moves

    def _king_moves(rank: int, file: int) -> List:
        moves = []

        moves.append((rank + 1, file))
        moves.append((rank - 1, file))
        moves.append((rank, file + 1))
        moves.append((rank, file - 1))
        moves.append((rank + 1, file + 1))
        moves.append((rank + 1, file - 1))
        moves.append((rank - 1, file + 1))
        moves.append((rank - 1, file - 1))

        return moves

    def _bishop_moves(rank: int, file: int) -> List:
        moves = []

        cur_rank = rank
        cur_file = file
        cur_rank +=1
        cur_file +=1
        while ChessLogic._on_board(cur_rank, cur_file):
            moves.append((cur_rank, cur_file))
            cur_rank += 1
            cur_file += 1
        
        cur_rank = rank
        cur_file = file
        cur_rank +=1
        cur_file -=1
        while ChessLogic._on_board(cur_rank, cur_file):
            moves.append((cur_rank, cur_file))
            cur_rank += 1
            cur_file -= 1

        cur_rank = rank
        cur_file = file
        cur_rank -=1
        cur_file -=1
        while ChessLogic._on_board(cur_rank, cur_file):
            moves.append((cur_rank, cur_file))
            cur_rank -= 1
            cur_file -= 1
        
        cur_rank = rank
        cur_file = file
        cur_rank -=1
        cur_file +=1
        while ChessLogic._on_board(cur_rank, cur_file):
            moves.append((cur_rank, cur_file))
            cur_rank -= 1
            cur_file += 1

        return moves

    def _rook_moves(rank: int, file: int) -> List:
        moves = []

        cur_rank = rank
        cur_file = file
        cur_rank +=1
        while ChessLogic._on_board(cur_rank, cur_file):
            moves.append((cur_rank, cur_file))
            cur_rank += 1
        
        cur_rank = rank
        cur_file = file
        cur_rank -=1
        while ChessLogic._on_board(cur_rank, cur_file):
            moves.append((cur_rank, cur_file))
            cur_rank -= 1

        cur_rank = rank
        cur_file = file
        cur_file +=1
        while ChessLogic._on_board(cur_rank, cur_file):
            moves.append((cur_rank, cur_file))
            cur_file += 1
        
        cur_rank = rank
        cur_file = file
        cur_file -=1
        while ChessLogic._on_board(cur_rank, cur_file):
            moves.append((cur_rank, cur_file))
            cur_file -= 1

        return moves

    def _queen_moves(rank: int, file: int) -> List:
        return _bishop_moves + _rook_moves
    
    def _knight_moves(rank: int, file: int) -> List:
        moves = []

        moves.append((rank + 2, file - 1))
        moves.append((rank + 2, file + 1))
        moves.append((rank + 1, file - 2))
        moves.append((rank + 1, file + 2))
        moves.append((rank - 1, file - 2))
        moves.append((rank - 1, file + 2))
        moves.append((rank - 2, file - 1))
        moves.append((rank - 2, file + 1))

        return moves

            
    @staticmethod
    def _on_board(rank: int, file: int) -> bool:
        if rank < 0 or rank > 7:
            return False
        if file < 0 or file > 7:
            return False
        return True

