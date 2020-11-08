import pygame
import random

from shape import (
    F,
    L,
    Z,
    I,
    O
)
from preview import Preview
from constants import (
    ROWS,
    COLS,
    WIDTH,
    HEIGHT,
    PREVIEW_HEIGHT,
    SQUARE_SIZE,
    WHITE
)


class Board:
    def __init__(self):
        self._shapes = []
        self.next_shape = random.choice([F, L, Z, I, O])()
        self.spawn_shape()

        # self.cur_shape = self._shapes[0]
        self.can_turbo = True

    def check_for_collisions(self):
        # for shape in self._shapes:
        #     if shape.check_for_collisions():
        #         return True
        # return False
        pieces = []
        for shape in self._shapes:
            for piece in shape[shape.rotation]:
                if piece:
                    pieces.append(piece)
        pieces.remove(self.cur_shape)

        positions = []
        for piece in pieces:
            positions.append((piece.row, piece.col))

        for pos in positions:
            for piece in self.cur_shape:
                if pos == (piece.row, piece.col):
                    return True
        return False

    def check_for_full_row(self, row):
        # return False
        pieces = []
        for shape in self._shapes:
            for piece in shape._pieces[shape.rotation]:
                if piece.row == row:
                    pieces.append(piece)

        for col in range(COLS):
            for piece in pieces:
                if piece.col == col:
                    break
            else:
                return False
        return True

    def remove_row(self, row):
        for shape in self._shapes:
            for piece in shape._pieces[shape.rotation]:
                if piece.row == row:
                    shape.remove_row(row)
                    break

        pieces = []
        for shape in self._shapes:
            if shape == self.cur_shape:
                continue
            for piece in shape._pieces[shape.rotation]:
                pieces.append(piece)

        filtered = filter(lambda x: x.row < row, pieces)
        for piece in filtered:
            piece.move_down()

    def update(self, parent):
        shapes_copy = self._shapes[:]
        shapes_copy.remove(self.cur_shape)
        spawn = self.cur_shape.update(shapes_copy)
        if spawn:
            self.spawn_shape()
            self.cur_shape.no_speed_limit = False

            for row in range(ROWS):
                full = self.check_for_full_row(row)
                if full:
                    self.remove_row(row)
                    parent.points += COLS

        pieces = []
        for shape in self._shapes:
            for piece in shape._pieces[shape.rotation]:
                if not shape.not_hit_bottom:  # If shape has stopped falling
                    pieces.append(piece)

        top_row = filter(lambda x: x.row <= 0, pieces)
        if any(top_row):
            return True

        return False

        # full_row = self.check_for_full_row()
        # if full_row:
        #     self.remove_row(full_row)

    def rotate(self):
        shapes_copy = self._shapes[:]
        shapes_copy.remove(self.cur_shape)
        self.cur_shape.rotate(shapes_copy)

    def draw(self, win: pygame.Surface):
        # draw columns
        for x in range(1, COLS):
            start_pos = (x * SQUARE_SIZE, 0)
            end_pos = (x * SQUARE_SIZE, HEIGHT - PREVIEW_HEIGHT)

            pygame.draw.line(win, WHITE, start_pos, end_pos)

        # draw rows
        for y in range(1, ROWS + 1):
            start_pos = (0, y * SQUARE_SIZE)
            end_pos = (WIDTH, y * SQUARE_SIZE)

            pygame.draw.line(win, WHITE, start_pos, end_pos)

        # draw shapes
        for shape in self._shapes:
            shape.draw(win)

        # draw preview
        self.preview.draw(win)

    def spawn_shape(self):
        # new_shape = random.choice([F, L, Z, I, O])()
        self._shapes.append(self.next_shape)
        self.cur_shape = self.next_shape
        self.can_turbo = False
        self.next_shape = random.choice([F, L, Z, I, O])()
        self.preview = Preview(self.next_shape)
