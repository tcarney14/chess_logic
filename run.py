from game.game import Game
from game.board import Board
from players import RandomPlayer, GreedyPlayer

board = Board()

game = Game(board, player1=RandomPlayer(), player2=GreedyPlayer())

game.play()

game.board.display()

