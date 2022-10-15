from board import Board

class Game:

    def __init__(self, board: Board):
        self.board = board


    def play():

        mate = False

        while not mate:

            cur_player = players[self.board.ply]

            move = cur_player.play(self.board)

            self.board.execute_move(move)

            mate = ChessLogic.check_mates(self.board)

            self.board.advance_turn()
