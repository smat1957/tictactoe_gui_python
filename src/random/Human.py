from Params import Params

class Human:
    def __init__(self, name):
        self.name = name

    def put_stone(self, board, pos=(-1,-1)):
        def get_slot(xy):
            x, y = xy[0], xy[1]
            N = 3
            for ypos in range(N):
                y0 = board.SLOTH * ypos
                y1 = board.SLOTH * (ypos + 1)
                for xpos in range(N):
                    x0 = board.SLOTW * xpos
                    x1 = board.SLOTW * (xpos + 1)
                    if y0 < y < y1 and x0 < x < x1:
                        return ypos * N + xpos
            return -1
        vacant = board.vacant()
        if not vacant:
            return False
        n = get_slot(pos)
        if n in vacant:
            board.board[n] = Params.HUMAN_ID
        else:
            return None
        return True

