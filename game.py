import pygame

from board import Board

from menu import StartupMenu, PlayAgainMenu
from constants import BLACK, WHITE, SQUARE_SIZE, HEIGHT, PREVIEW_HEIGHT


class Game:
    PLAY = 0
    QUIT = 1

    def __init__(self, win: pygame.Surface):
        self.win = win

        self.board = Board()
        self.running = True
        self.toreturn = None
        self.elapsed_time = pygame.time.get_ticks()
        self.font = pygame.font.SysFont("Arial", 14)
        self.points = 0

        pygame.key.set_repeat(100, 100)

    def update(self):
        game_over = self.board.update(self)
        if game_over:
            self.running = False

    def draw(self):
        self.win.fill(BLACK)

        self.board.draw(self.win)

        points = "Points: " + str(self.points)
        point_text = self.font.render(points, True, WHITE)
        point_text_rect = point_text.get_rect()
        point_text_rect.x = SQUARE_SIZE
        point_text_rect.centery = HEIGHT - PREVIEW_HEIGHT // 2
        self.win.blit(point_text, point_text_rect)

        pygame.display.update()

    def start_menu(self):
        menu = StartupMenu(self)
        return menu.run()

    def run(self):
        clock = pygame.time.Clock()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return self.QUIT

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.board.rotate()
                    if event.key == pygame.K_LEFT:
                        shapes_copy = self.board._shapes[:]
                        shapes_copy.remove(self.board.cur_shape)
                        self.board.cur_shape.move_left(shapes_copy)
                    if event.key == pygame.K_RIGHT:
                        shapes_copy = self.board._shapes[:]
                        shapes_copy.remove(self.board.cur_shape)
                        self.board.cur_shape.move_right(shapes_copy)
                    if event.key == pygame.K_DOWN and self.board.can_turbo:
                        self.board.cur_shape.no_speed_limit = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.board.cur_shape.no_speed_limit = False
                        self.board.can_turbo = True

            clock.tick(30)

            self.update()
            self.draw()

        menu = PlayAgainMenu(self)
        return menu.run()
