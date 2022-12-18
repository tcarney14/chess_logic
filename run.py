from game.game import Game
from game.board import Board
from players.random_player import RandomPlayer

board = Board()

game = Game(board, player1=RandomPlayer(), player2=RandomPlayer())

game.play()

game.board.display()

