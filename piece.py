import pygame

from constants import SQUARE_SIZE


class Piece:
    def __init__(self, color, row=0, col=0):
        self.color = color

        self.row, self.col = row, col

        self.update_pos()

    def update_pos(self):
        self.pos = (self.col * SQUARE_SIZE + 1, self.row * SQUARE_SIZE + 1)

    def check_for_collisions(self, pieces):
        for piece in pieces:
            if piece.row == self.row and piece.col == self.col:
                return True
        return False

    def move_down(self):
        self.row += 1
        self.update_pos()

    def move_up(self):
        self.row -= 1
        self.update_pos()

    def move_left(self):
        self.col -= 1
        self.update_pos()

    def move_right(self):
        self.col += 1
        self.update_pos()

    def draw(self, win: pygame.Surface, subtract_one=True):
        if subtract_one:
            rect = pygame.Rect(*self.pos, SQUARE_SIZE - 1, SQUARE_SIZE - 1)
        else:
            rect = pygame.Rect(*self.pos, SQUARE_SIZE, SQUARE_SIZE)
        pygame.draw.rect(win, self.color, rect)
