from game import Game
from board import Board
from Players.random_player import RandomPlayer

board = Board()

game = Game(board, player1=RandomPlayer(board), player2=RandomPlayer(board))

game.board.display()

