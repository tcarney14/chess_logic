from game.game import Game
from game.board import Board
from players import RandomPlayer, GreedyPlayer

board = Board()

game = Game(board, player1=GreedyPlayer(), player2=RandomPlayer())

game.play()

game.board.display()

