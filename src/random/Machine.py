from random import randint
from Params import Params

class Machine():
    def __init__(self, name):
        self.name = name

    def put_stone(self, board):
        vacant = board.vacant()
        if not vacant:
            return False
        n = randint(0, len(vacant)-1)
        board.board[ vacant[n] ] = Params.MACHINE_ID
        return True
