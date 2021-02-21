from Params import Params, State

class Strategy:
    INFINITY = 10000
    def __init__(self):
        pass

    def bestMove(self, board, vacant):
        bestEval = -Strategy.INFINITY
        bestMove = -1
        self.debug_seq = 0
        for n in vacant:
            board.board[n] = Params.MACHINE_ID
            eval = self.minimax(board, 0, False)
            if bestEval<eval:
                bestEval = eval
                bestMove = n
            board.undo(n)
        return bestMove

    def minimax(self, board, depth, isMaximizingPlayer):
        def evaluate(depth):
            if board.state == State.MACHINE_WIN:
                board.state = State.GAME
                return 10-depth     #return 10
            elif board.state == State.HUMAN_WIN:
                board.state = State.GAME
                return depth-10     #return -10
            else:
                self.state = State.GAME
                return 0

        board.winner()
        if board.state != State.GAME:
            return evaluate(depth)
        bestVal = -Strategy.INFINITY if isMaximizingPlayer else +Strategy.INFINITY
        for n in range(9):
            if board.can_put(n):
                board.board[n] = Params.MACHINE_ID if isMaximizingPlayer else Params.HUMAN_ID
                value = self.minimax(board, depth + 1, not isMaximizingPlayer)
                bestVal = max(value, bestVal) if isMaximizingPlayer else min(value, bestVal)
                board.undo(n)
        return bestVal

    def bestMoveAB(self, board, vacant):
        bestEval = -Strategy.INFINITY
        bestMove = -1
        for n in vacant:
            board.board[n] = Params.MACHINE_ID
            eval = self.minimaxab(board, 0, 0, False, -Strategy.INFINITY, +Strategy.INFINITY)
            if bestEval<eval:
                bestEval = eval
                bestMove = n
            board.undo(n)
        return bestMove

    def minimaxab(self, board, node, depth, isMaximizingPlayer, alpha, beta):
        def evaluate(depth):
            if board.state == State.MACHINE_WIN:
                board.state = State.GAME
                return 10-depth     #return 10
            elif board.state == State.HUMAN_WIN:
                board.state = State.GAME
                return depth-10     #return -10
            else:
                self.state = State.GAME
                return 0

        board.winner()
        if board.state != State.GAME:
            return evaluate(depth)

        bestVal = -Strategy.INFINITY if isMaximizingPlayer else +Strategy.INFINITY
        for n in range(9):
            if board.can_put(n):
                board.board[n] = Params.MACHINE_ID if isMaximizingPlayer else Params.HUMAN_ID
                value = self.minimaxab(board, node+1, depth+1, not isMaximizingPlayer, alpha, beta)
                board.undo(n)
                if isMaximizingPlayer:
                    bestVal = max(value, bestVal)
                    alpha = max(alpha, bestVal)
                else:
                    bestVal = min(value, bestVal)
                    beta = min(beta, bestVal)
                if beta<=alpha:
                    #print('depth=',depth)
                    break
        return bestVal

