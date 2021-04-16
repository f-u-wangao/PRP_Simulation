import pygame


class Background:

    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

    def draw_grid(self, flag):
        cell_width = 30
        cell_height = 30
        row = 30
        col = 30
        if not flag:
            color = (220, 220, 220)
        else:
            color = (119, 136, 153)
        for r in range(row):
            pygame.draw.line(self.screen, color, (0, r * cell_height), (self.width, r * cell_height))
        for c in range(col):
            pygame.draw.line(self.screen, color, (c * cell_width, 0), (c * cell_width, self.height))
