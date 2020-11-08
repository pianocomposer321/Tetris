import pygame

from shape import Shape
from constants import ROWS, COLS


class Preview(Shape):
    def __init__(self, shape):
        row = ROWS
        col = COLS - len(shape.shape[0][0])

        super().__init__(shape.color, shape.shape, row, col)

    def draw(self, win: pygame.Surface):
        for piece in self._pieces[self.rotation]:
            piece.draw(win, False)
