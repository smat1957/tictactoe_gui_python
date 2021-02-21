import pygame
from Screen import Screen
from Params import State,Params

class Board( Screen ):
    def __init__(self, wh=(300,300), color=(200,200,0), str='Tic-Tac-Toe'):
        super().__init__(wh, color)
        self.caption(str)
        self.board = [Params.EMPTY_ID for _ in range(9)]
        self.state = State.GAME

    def draw(self):
        self.fill()
        N = 3
        RADIUS = int(self.SLOTW*0.2)
        BLACK = (0,0,0)
        for ypos in range(N):
            yc = ypos * self.SLOTH + self.SLOTH // 2
            for xpos in range(N):
                xc = xpos*self.SLOTW + self.SLOTW // 2
                i = ypos * N + xpos
                if self.board[i] == Params.HUMAN_ID:
                    pygame.draw.circle(self.surface, BLACK, (xc,yc), RADIUS, 3)
                elif  self.board[i] == Params.MACHINE_ID:
                    startp = (xc - RADIUS, yc - RADIUS)
                    endp = (xc + RADIUS, yc + RADIUS)
                    pygame.draw.line(self.surface, BLACK, startp, endp, 3)
                    startp = (xc + RADIUS, yc - RADIUS)
                    endp = (xc - RADIUS, yc + RADIUS)
                    pygame.draw.line(self.surface, BLACK, startp, endp, 3)

    def winner(self):
        def scan(n1, n2, n3):
            p = self.board[n1] != 0 and \
                self.board[n1] == self.board[n2] and \
                self.board[n1] == self.board[n3]
            if p:
                if self.board[n1]==Params.HUMAN_ID:
                    self.state = State.HUMAN_WIN
                elif self.board[n1]==Params.MACHINE_ID:
                    self.state = State.MACHINE_WIN
            else:
                if not self.vacant():
                    self.state = State.DRAW
                else:
                    self.state = State.GAME
            return p
        #
        return scan(0, 1, 2) or scan(3, 4, 5) or scan(6, 7, 8) or \
               scan(0, 3, 6) or scan(1, 4, 7) or scan(2, 5, 8) or \
               scan(0, 4, 8) or scan(2, 4, 6)

    def vacant(self):
        empty = []
        for n, slot in enumerate(self.board):
            if slot == Params.EMPTY_ID:
                empty.append(n)
        return empty

    # 以下を追加
    def undo(self, n):
        self.board[n] = Params.EMPTY_ID

    def can_put(self, n):
        if self.board[n]==Params.EMPTY_ID:
            return True
        return False

    # ボードを表示する for Debug
    def debug_board(self, seq, debugstring):
        str0 = '\n('+str(seq)+')'
        tmp = []
        for i in range(9):
            if self.board[i] == Params.EMPTY_ID:
                tmp.append(' ')
            elif self.board[i] == Params.HUMAN_ID:
                tmp.append('o')
            elif self.board[i] == Params.MACHINE_ID:
                tmp.append('x')
        str1 =  '\n{0[0]}|{0[1]}|{0[2]}\t<-----\t0|1|2'\
                '\n{0[3]}|{0[4]}|{0[5]}\t<-----\t3|4|5'\
                '\n{0[6]}|{0[7]}|{0[8]}\t<-----\t6|7|8\n'.format(tmp)
        str2 = str0 + str1 + debugstring + '\n'
        with open('textfile.txt', 'a', encoding='utf-8') as f:
            f.write(str2)

