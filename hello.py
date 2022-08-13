import os
import time
from colorama import Fore, Back, Style, init, deinit
deinit()

class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def tocaParede(self, point):
        return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y

    def definirPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '*'
        self.mark = '.'
        self.framerate = 0.1
        self.pos = [0, 0]

    def cima(self):
        pos = [self.pos[0], self.pos[1]-1]
        if not self.canvas.tocaParede(pos):
            self.draw(pos)

    def baixo(self):
        pos = [self.pos[0], self.pos[1]+1]
        if not self.canvas.tocaParede(pos):
            self.draw(pos)

    def direita(self):
        pos = [self.pos[0]+1, self.pos[1]]
        if not self.canvas.tocaParede(pos):
            self.draw(pos)

    def esquerda(self):
        pos = [self.pos[0]-1, self.pos[1]]
        if not self.canvas.tocaParede(pos):
            self.draw(pos)

    def draw(self, pos):
        self.canvas.definirPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.definirPos(self.pos, Fore.BLUE)
        self.canvas.print()
        time.sleep(self.framerate)

canvas = Canvas(40, 20)
scribe = TerminalScribe(canvas)

#canvas = Canvas(20, 30)
#scribe = TerminalScribe(canvas)


scribe.direita()
scribe.direita()
scribe.direita()
scribe.direita()
scribe.baixo()
scribe.baixo()
scribe.baixo()
scribe.baixo()
scribe.esquerda()
scribe.esquerda()
scribe.esquerda()
scribe.esquerda()
scribe.cima()
scribe.cima()
scribe.cima()
scribe.cima()

