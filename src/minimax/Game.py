import sys
import pygame
from pygame.locals import QUIT, MOUSEBUTTONUP
from Board import Board
from Human import Human
from Machine import Machine
from Params import State

class Game:
    def __init__(self, turn='human', strategy='random'):
        pygame.init()
        self.board = Board(str=strategy+' is selected!')
        self.human = Human('Taro')
        self.machine = Machine('Computer', strategy)
        self.turn = False if turn=='human' else True
        self.clock = pygame.time.Clock()
        self.FPS = 10

    def change_turn(self):
        self.turn = not self.turn

    def fine(self):
        pygame.quit()
        sys.exit()

    def key_event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.fine()
            elif event.type == MOUSEBUTTONUP:
                if not self.turn:
                    p = self.human.put_stone(self.board, event.pos)
                    if p:
                        self.change_turn()
                    elif p==False:
                        pass    # DRAW
                    else:
                        pass

    def judge(self):
        result = False
        if self.board.winner():
            if self.board.state == State.MACHINE_WIN:
                self.board.caption('Computer won the game!')
            elif self.board.state == State.HUMAN_WIN:
                self.board.caption('You won!')
        else:
            if self.board.state == State.DRAW:
                self.board.caption('Draw!')
            elif self.board.state == State.GAME:
                result = True
        return result

    def start(self):
        while True:
            self.key_event()
            self.board.draw()
            if self.turn:
                if self.machine.put_stone(self.board):
                    self.change_turn()
            self.judge()
            pygame.display.update()
            self.clock.tick(self.FPS)

