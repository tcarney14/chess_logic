import abc
from game.board import Board

class Player(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def play(self, board: Board, valid_moves: list):
		pass
