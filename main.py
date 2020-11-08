from constants import WIDTH, HEIGHT, WINDOW_TITLE
from game import Game
import pygame

pygame.init()

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

game = Game(win)
state = game.start_menu()

while state == Game.PLAY:
    game = Game(win)
    state = game.run()

pygame.quit()
