from typing import List
from collections import namedtuple
from game.board import Board
from game.pieces import Pieces

Move = namedtuple("Move", ["start", "dest"])

def get_valid_moves(board: Board) -> List:
    valid_moves = []
    
    pieces = board.get_pieces()

    for piece in pieces:
        file_, rank = piece["file"], piece["rank"]
        start = (file_, rank)
        destinations = move_function[piece["piece"]](file_, rank)
        for dest in destinations:
            if _on_board(dest[0], dest[1]):
                valid_moves.append(Move(start, dest))

    return valid_moves

def check_mates(board: Board):
    return False

def pawn_moves(file_: int, rank: int) -> List:
    
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
    while _on_board(cur_file_, cur_rank):
        moves.append((cur_file_, cur_rank))
        cur_rank += 1
        cur_file_ += 1
    
    cur_rank = rank
    cur_file_ = file_
    cur_rank +=1
    cur_file_ -=1
    while _on_board(cur_file_, cur_rank):
        moves.append((cur_file_, cur_rank))
        cur_rank += 1
        cur_file_ -= 1

    cur_rank = rank
    cur_file_ = file_
    cur_rank -=1
    cur_file_ -=1
    while _on_board(cur_file_, cur_rank):
        moves.append((cur_file_, cur_rank))
        cur_rank -= 1
        cur_file_ -= 1
    
    cur_rank = rank
    cur_file_ = file_
    cur_rank -=1
    cur_file_ +=1
    while _on_board(cur_file_, cur_rank):
        moves.append((cur_file_, cur_rank))
        cur_rank -= 1
        cur_file_ += 1

    return moves


def _rook_moves(file_: int, rank: int) -> List:
    moves = []

    cur_rank = rank
    cur_file_ = file_
    cur_rank +=1
    while _on_board(cur_file_, cur_rank):
        moves.append((cur_file_, cur_rank))
        cur_rank += 1
    
    cur_rank = rank
    cur_file_ = file_
    cur_rank -=1
    while _on_board(cur_file_, cur_rank):
        moves.append((cur_file_, cur_rank))
        cur_rank -= 1

    cur_rank = rank
    cur_file_ = file_
    cur_file_ +=1
    while _on_board(cur_file_, cur_rank):
        moves.append((cur_file_, cur_rank))
        cur_file_ += 1
    
    cur_rank = rank
    cur_file_ = file_
    cur_file_ -=1
    while _on_board(cur_file_, cur_rank):
        moves.append((cur_file_, cur_rank))
        cur_file_ -= 1

    return moves

def _queen_moves(file_: int, rank: int) -> List:
    return _bishop_moves(file_, rank) + _rook_moves(file_, rank)

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

        
def _on_board(file_: int, rank: int) -> bool:
    if rank < 0 or rank > 7:
        return False
    if file_ < 0 or file_ > 7:
        return False
    return True

move_function = {
    Pieces.PAWN.value: pawn_moves,
    Pieces.KING.value: _king_moves,
    Pieces.BISHOP.value: _bishop_moves,
    Pieces.KNIGHT.value: _knight_moves,
    Pieces.ROOK.value: _rook_moves,
    Pieces.QUEEN.value: _queen_moves
}