import pygame

from constants import BLACK


class Button:
    def __init__(self, text: str, color: tuple, command, **kwargs):
        pygame.font.init()

        self.text = text
        self.color = color
        self.command = command

        if 'width' in kwargs:
            self.width = kwargs['width']
        else:
            self.width = 100
        if 'height' in kwargs:
            self.height = kwargs['height']
        else:
            self.height = 25
        if 'xpos' in kwargs:
            self.xpos = kwargs['xpos']
        else:
            self.xpos = self.width // 2
        if 'ypos' in kwargs:
            self.ypos = kwargs['ypos']
        else:
            self.ypos = self.height // 2
        if 'font_size' in kwargs:
            self.font_size = kwargs['font_size']
        else:
            self.font_size = 14
        if 'font' in kwargs:
            self.font = pygame.font.SysFont(kwargs['font'], self.font_size)
        else:
            self.font = pygame.font.SysFont("Arial", self.font_size)
        if 'show_border' in kwargs:
            self.show_border = kwargs['show_border']
        else:
            self.show_border = False
        if 'border' in kwargs:
            self.border = kwargs['border']
        else:
            self.border = 1
        if 'border_color' in kwargs:
            self.border_color = kwargs['border_color']
        else:
            self.border_color = (0, 0, 0)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.xpos
        self.rect.centery = self.ypos

    def callback(self):
        self.command()

    def is_inside(self, x, y):
        if x > self.rect.right:
            return False
        if x < self.rect.left:
            return False
        if y > self.rect.bottom:
            return False
        if y < self.rect.top:
            return False
        return True

    def on_click(self):
        x, y = pygame.mouse.get_pos()
        inside = self.is_inside(x, y)
        if inside:
            self.callback()

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        if self.show_border:
            pygame.draw.rect(win, self.border_color, self.rect, self.border)

        text = self.font.render(self.text, True, BLACK)
        text_rect = text.get_rect()
        text_rect.centerx = self.rect.centerx
        text_rect.centery = self.rect.centery

        win.blit(text, text_rect)
