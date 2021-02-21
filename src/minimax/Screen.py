import pygame

class Screen:
    def __init__(self, wh=(600,600), bgcolor=(0,0,0)):
        self.WIDTH = wh[0]
        self.HEIGHT = wh[1]
        self.COLOR = bgcolor
        self.SIZE = (self.WIDTH, self.HEIGHT)
        self.surface = pygame.display.set_mode(self.SIZE)
        self.SLOTW = self.WIDTH//3
        self.SLOTH = self.HEIGHT//3

    def fill(self):
        self.surface.fill(self.COLOR)
        BLACK = (0,0,0)
        for i in range(1,3):
            startp = (0, self.SLOTH*i)
            endp = (self.WIDTH, self.SLOTH*i)
            pygame.draw.line(self.surface, BLACK, startp, endp)
            startp = (self.SLOTW*i, 0)
            endp = (self.SLOTW*i, self.HEIGHT)
            pygame.draw.line(self.surface, BLACK, startp, endp)

    def caption(self, str):
        pygame.display.set_caption(str)

