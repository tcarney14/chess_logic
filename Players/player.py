import abc

class Player(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def play(self, board: Board, valid_moves: List):
		pass
