from board import Board

class Game:

    def __init__(self, board: Board, player1: Player, player2: Player):
        self.board = board
        self.players = [player1, player2]

    def play():

        mate = False

        while not mate:

            cur_player = players[self.board.ply]

            move = cur_player.play(self.board)

            self.board.execute_move(move)

            mate = ChessLogic.check_mates(self.board)

            self.board.advance_turn()
