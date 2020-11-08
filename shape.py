import pygame

from piece import Piece
from constants import (
    SQUARE_SIZE,
    F_SHAPE,
    L_SHAPE,
    Z_SHAPE,
    I_SHAPE,
    O_SHAPE,
    F_COLOR,
    L_COLOR,
    Z_COLOR,
    I_COLOR,
    O_COLOR,
    MOVE_DELAY,
    ROWS,
    COLS
)


class Shape:
    def __init__(self, color, shape, row=0, col=0):
        self.shape = shape
        self.color = color
        self.rotation = 0

        if row:
            self.row = row
        else:
            # for x, row in enumerate(reversed(self.shape[self.rotation])):
            #     if any(row):
            #         self.row = -x
            #         break
            for row in reversed(range(len(self.shape[self.rotation]))):
                if any(self.shape[self.rotation][row]):
                    self.row = -row
                    break

        if col:
            self.col = col
        else:
            self.col = (COLS + 0.5) // 2 - (len(self.shape[0]) + 0.5) // 2

        self.pos = (self.col * SQUARE_SIZE + 1, self.row * SQUARE_SIZE + 1)

        self._pieces = []

        for i, rotation in enumerate(self.shape):
            self._pieces.append([])
            for j, row in enumerate(rotation):
                for k, piece in enumerate(row):
                    if piece == 1:
                        self._pieces[i].append(
                            Piece(color, self.row + j, self.col + k)
                        )

        self.elapsed_time = pygame.time.get_ticks()

        self.not_hit_bottom = True
        self.no_speed_limit = False

    def lowest_row(self):
        # return self.row + len(self.shape[self.rotation])
        for row in reversed(range(len(self.shape[self.rotation]))):
            if any(self.shape[self.rotation][row]):
                return self.row + row

    def check_for_collisions(self, shapes):
        # for piece in self._pieces[self.rotation]:
        #     if piece.check_for_collisions():
        #         return True
        # return False
        pieces = []
        for shape in shapes:
            for piece in shape._pieces[shape.rotation]:
                pieces.append(piece)

        positions = []
        for piece in pieces:
            positions.append((piece.row, piece.col))

        # for pos in positions:
        #     if pos == (self.row, self.col):
        #         return True
        for piece in self._pieces[self.rotation]:
            if (piece.row, piece.col) in positions:
                return True

        return False

    def remove_row(self, row):
        # copy = self._pieces[self.rotation][:]
        # for i, piece in enumerate(copy):
        #     if piece.row == row:
        #         self._pieces[self.rotation].remove(piece)
        filtered = filter(lambda x: x.row != row, self._pieces[self.rotation])
        self._pieces[self.rotation] = list(filtered)

        # for piece in self._pieces[self.rotation]:
        #     if piece.row < row:
        #         # piece.move_down()
        #         while True:
        #             piece.move_down()
        #             if piece.check_for_collisions() or piece.row >= ROWS:
        #                 piece.row += 1
        #                 break

    def rotate(self, shapes):
        if self.not_hit_bottom:
            old_rotation = self.rotation
            self.rotation += 1
            self.rotation %= len(self.shape)

            for piece in self._pieces[self.rotation]:
                if piece.col < 0:
                    self.rotation = old_rotation
                    break
                if piece.col >= COLS:
                    self.rotation = old_rotation
                    break
                if piece.row >= ROWS:
                    self.rotation = old_rotation
                    break

            if self.check_for_collisions(shapes):
                self.rotation = old_rotation

    def move_left(self, shapes=None):
        self.col -= 1
        if self.not_hit_bottom:
            for piece in self._pieces[self.rotation]:
                if piece.col <= 0:
                    self.col += 1
                    return

            for rotation in self._pieces:
                for piece in rotation:
                    piece.move_left()
        else:
            self.col += 1

        if shapes is not None:
            collision = self.check_for_collisions(shapes)
            if collision:
                self.col += 1
                for rotation in self._pieces:
                    for piece in rotation:
                        piece.move_right()

    def move_right(self, shapes=None):
        # for piece in self._pieces[self.rotation]:
        #     piece.move_right()
        self.col += 1
        if self.not_hit_bottom:
            for piece in self._pieces[self.rotation]:
                if piece.col >= COLS - 1:
                    self.col -= 1
                    return

            for rotation in self._pieces:
                for piece in rotation:
                    piece.move_right()
        else:
            self.col -= 1

        if shapes is not None:
            collision = self.check_for_collisions(shapes)
            if collision:
                self.col -= 1
                for rotation in self._pieces:
                    for piece in rotation:
                        piece.move_left()

    def move_down(self, shapes):
        self.row += 1
        if self.lowest_row() < ROWS:
            for rotation in self._pieces:
                for piece in rotation:
                    piece.move_down()
        else:
            self.row -= 1
            self.not_hit_bottom = False
            return

        collision = self.check_for_collisions(shapes)
        if collision:
            self.row -= 1
            for rotation in self._pieces:
                for piece in rotation:
                    piece.move_up()
                    self.not_hit_bottom = False

    def turbo(self):
        self.move_down()

    def update(self, shapes):
        new_elapsed_time = pygame.time.get_ticks()
        delta_time = new_elapsed_time - self.elapsed_time

        spawn = False

        if delta_time >= MOVE_DELAY or self.no_speed_limit:
            # self.update()
            if self.not_hit_bottom:
                self.move_down(shapes)
            else:
                spawn = True
            self.elapsed_time = new_elapsed_time

        return spawn

    def draw(self, win: pygame.Surface):
        for piece in self._pieces[self.rotation]:
            piece.draw(win)


class F(Shape):
    def __init__(self, row=0, col=0):
        super().__init__(F_COLOR, F_SHAPE, row, col)


class L(Shape):
    def __init__(self, row=0, col=0):
        super().__init__(L_COLOR, L_SHAPE, row, col)


class Z(Shape):
    def __init__(self, row=0, col=0):
        super().__init__(Z_COLOR, Z_SHAPE, row, col)


class I(Shape):
    def __init__(self, row=0, col=0):
        super().__init__(I_COLOR, I_SHAPE, row, col)


class O(Shape):
    def __init__(self, row=0, col=0):
        super().__init__(O_COLOR, O_SHAPE, row, col)
