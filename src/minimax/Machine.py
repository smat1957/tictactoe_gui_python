from random import randint
from Params import Params
from Strategy import Strategy

class Machine( Strategy ):
    def __init__(self, name, strategy):
        super().__init__()
        self.name = name
        self.strategy = strategy

    def put_stone(self, board):
        vacant = board.vacant()
        if not vacant:
            return False
        if self.strategy=='random':
            n = randint(0, len(vacant)-1)
            board.board[ vacant[n] ] = Params.MACHINE_ID
        elif self.strategy=='minimax':
            n = self.bestMove(board, vacant)
            board.board[ n ] = Params.MACHINE_ID
        elif self.strategy=='alphabeta':
            n = self.bestMoveAB(board, vacant)
            board.board[ n ] = Params.MACHINE_ID
        return True

