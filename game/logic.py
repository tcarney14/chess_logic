from typing import List
from copy import deepcopy
from collections import namedtuple
from game.board import Board
from game.pieces import Pieces

Move = namedtuple("Move", ["start", "dest"])

def check_mates(board: Board, valid_moves: list):
    if len(valid_moves) == 0:
        return True
    else:
        return False

def in_check(board: Board):
    look_ahead_board = deepcopy(board)
    look_ahead_board.advance_turn()
    opponent_moves = _get_all_moves(look_ahead_board)

    for move in opponent_moves:
        _, dest = move
        dest_file, dest_rank = dest
        if int(abs(look_ahead_board.board[dest_file][dest_rank])) == Pieces.KING.value:
            return True

    return False

def pawn_moves(file_: int, rank: int, board: Board) -> List:
    
    moves = []

    if _on_board(file_, rank + 1) and not board.square_occupied(file_, rank + 1):
        moves.append((file_, rank + 1))
    #moves.append((file_, rank + 2)) ignore 2 square move for now
    
    #attacking moves
    if _on_board(file_ + 1, rank + 1) and board.square_occupied_opponent(file_ + 1, rank + 1):
        moves.append((file_ + 1, rank + 1))
    if _on_board(file_ - 1, rank + 1) and board.square_occupied_opponent(file_ - 1, rank + 1):
        moves.append((file_ - 1, rank + 1))

    return moves


def _king_moves(file_: int, rank: int, board: Board) -> List:
    moves = []

    moves.append((file_, rank + 1))
    moves.append((file_, rank - 1))
    moves.append((file_ + 1, rank))
    moves.append((file_ - 1, rank))
    moves.append((file_ + 1, rank + 1))
    moves.append((file_ - 1, rank + 1))
    moves.append((file_ + 1, rank - 1))
    moves.append((file_ - 1, rank - 1))

    valid_moves = []
    for move in moves:
        if _on_board(move[0], move[1]) and not board.square_occupied_self(move[0], move[1]):
            valid_moves.append(move)

    return valid_moves


def _bishop_moves(file_: int, rank: int, board: Board) -> List:
    moves = []

    cur_rank = rank
    cur_file_ = file_
    cur_rank +=1
    cur_file_ +=1
    while _on_board(cur_file_, cur_rank) and not board.square_occupied_self(cur_file_, cur_rank):
        moves.append((cur_file_, cur_rank))

        if board.square_occupied_opponent(cur_file_, cur_rank):
            break
        cur_rank += 1
        cur_file_ += 1

    cur_rank = rank
    cur_file_ = file_
    cur_rank +=1
    cur_file_ -=1
    while _on_board(cur_file_, cur_rank) and not board.square_occupied_self(cur_file_, cur_rank):
        moves.append((cur_file_, cur_rank))

        if board.square_occupied_opponent(cur_file_, cur_rank):
            break
        cur_rank += 1
        cur_file_ -= 1

    cur_rank = rank
    cur_file_ = file_
    cur_rank -=1
    cur_file_ -=1
    while _on_board(cur_file_, cur_rank) and not board.square_occupied_self(cur_file_, cur_rank):
        moves.append((cur_file_, cur_rank))

        if board.square_occupied_opponent(cur_file_, cur_rank):
            break
        cur_rank -= 1
        cur_file_ -= 1
    
    cur_rank = rank
    cur_file_ = file_
    cur_rank -=1
    cur_file_ +=1
    while _on_board(cur_file_, cur_rank) and not board.square_occupied_self(cur_file_, cur_rank):
        moves.append((cur_file_, cur_rank))

        if board.square_occupied_opponent(cur_file_, cur_rank):
            break
        cur_rank -= 1
        cur_file_ += 1

    return moves


def _rook_moves(file_: int, rank: int, board: Board) -> List:
    moves = []

    cur_rank = rank
    cur_file_ = file_
    cur_rank +=1
    while _on_board(cur_file_, cur_rank) and not board.square_occupied_self(cur_file_, cur_rank):
        moves.append((cur_file_, cur_rank))

        if board.square_occupied_opponent(cur_file_, cur_rank):
            break
        cur_rank += 1
    
    cur_rank = rank
    cur_file_ = file_
    cur_rank -=1
    while _on_board(cur_file_, cur_rank) and not board.square_occupied_self(cur_file_, cur_rank):
        moves.append((cur_file_, cur_rank))

        if board.square_occupied_opponent(cur_file_, cur_rank):
            break
        cur_rank -= 1

    cur_rank = rank
    cur_file_ = file_
    cur_file_ +=1
    while _on_board(cur_file_, cur_rank) and not board.square_occupied_self(cur_file_, cur_rank):
        moves.append((cur_file_, cur_rank))

        if board.square_occupied_opponent(cur_file_, cur_rank):
            break
        cur_file_ += 1
    
    cur_rank = rank
    cur_file_ = file_
    cur_file_ -=1
    while _on_board(cur_file_, cur_rank) and not board.square_occupied_self(cur_file_, cur_rank):
        moves.append((cur_file_, cur_rank))

        if board.square_occupied_opponent(cur_file_, cur_rank):
            break
        cur_file_ -= 1

    return moves

def _queen_moves(file_: int, rank: int, board: Board) -> List:
    return _bishop_moves(file_, rank, board) + _rook_moves(file_, rank, board)

def _knight_moves(file_: int, rank: int, board: Board) -> List:
    moves = []

    moves.append((file_ - 1, rank + 2))
    moves.append((file_ + 1, rank + 2))
    moves.append((file_ - 2, rank + 1))
    moves.append((file_ + 2, rank + 1))
    moves.append((file_ - 2, rank - 1))
    moves.append((file_ + 2, rank - 1))
    moves.append((file_ - 1, rank - 2))
    moves.append((file_ + 1, rank - 2))

    valid_moves = []
    for move in moves:
        if _on_board(move[0], move[1]) and not board.square_occupied_self(move[0], move[1]):
            valid_moves.append(move)
    return valid_moves

        
def _on_board(file_: int, rank: int) -> bool:
    if rank < 0 or rank > 7:
        return False
    if file_ < 0 or file_ > 7:
        return False
    return True


def get_valid_moves(board: Board) -> List:
    valid_moves = []
    moves = _get_all_moves(board)
    for move in moves:
        look_ahead_board = deepcopy(board)
        look_ahead_board.execute_move(move)
        if not in_check(look_ahead_board):
            valid_moves.append(move)

    print(f"valid moves: {len(valid_moves)}")
    print(f"all moves: {len(moves)}")
    return valid_moves

def _get_all_moves(board: Board):
    """Gets all moves without verifying if we are check or not"""
    moves = []
    pieces = board.get_pieces()
    for piece in pieces:
        file_, rank = piece["file"], piece["rank"]
        start = (file_, rank)
        destinations = move_function[piece["piece"]](file_, rank, board)
        for dest in destinations:
            move = Move(start, dest)
            moves.append(move)

    return moves

move_function = {
    Pieces.PAWN.value: pawn_moves,
    Pieces.KING.value: _king_moves,
    Pieces.BISHOP.value: _bishop_moves,
    Pieces.KNIGHT.value: _knight_moves,
    Pieces.ROOK.value: _rook_moves,
    Pieces.QUEEN.value: _queen_moves
}