from Game import Game
from Params import Params

if __name__ == '__main__':
    sente = 'human'           # 'machine' or 'human'
    senryaku = 'alphabeta'        # 'random', 'minimax' or 'alphabeta'
    game = Game( turn=sente, strategy=senryaku )
    game.start()
