import pygame

from button import Button
from constants import (
    GREEN,
    RED,
    WIDTH,
    HEIGHT
)


class Menu:
    def __init__(self, parent, buttons: list()):
        self.buttons = buttons
        self.parent = parent

        self.toreturn = None
        self.running = True

        self.draw()

    def quit(self):
        self.toreturn = self.parent.QUIT
        self.running = False

    def on_click(self):
        for button in self.buttons:
            button.on_click()

    def draw(self):
        for button in self.buttons:
            button.draw(self.parent.win)

        pygame.display.update()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.on_click()

        return self.toreturn


class StartupMenu(Menu):
    def __init__(self, parent):
        play_button = Button("Play",
                             GREEN,
                             self.play,
                             xpos=WIDTH // 5,
                             ypos=(HEIGHT * 2) // 3)

        quit_button = Button("Quit",
                             RED,
                             self.quit,
                             xpos=(WIDTH * 4) // 5,
                             ypos=(HEIGHT * 2) // 3)
        super().__init__(parent, buttons=[play_button, quit_button])

    def play(self):
        self.toreturn = self.parent.PLAY
        self.running = False


class PlayAgainMenu(Menu):
    def __init__(self, parent):
        play_again_button = Button("Play Again",
                                   GREEN,
                                   self.play_again,
                                   xpos=WIDTH // 5,
                                   ypos=(HEIGHT * 2) // 3)

        quit_button = Button("Quit",
                             RED,
                             self.quit,
                             xpos=(WIDTH * 4) // 5,
                             ypos=(HEIGHT * 2) // 3)

        super().__init__(parent, buttons=[play_again_button, quit_button])

    def play_again(self):
        self.toreturn = self.parent.PLAY
        self.running = False
