import pygame
from settings import Settings


class Background:

    def __init__(self, screen, width, height):
        # 导入设置
        self.settings_vis = Settings()
        self.screen = screen
        self.width = width
        self.height = height

    def draw_grid(self, flag):
        cell_width = self.settings_vis.cell_width
        cell_height = self.settings_vis.cell_height
        width_left = self.settings_vis.width_left
        row = self.settings_vis.row
        col = self.settings_vis.col
        if not flag:
            color = (220, 220, 220)
        else:
            color = (119, 136, 153)
        for r in range(row + 1):
            pygame.draw.line(self.screen, color, (width_left, r * cell_height),
                             (col * cell_width + width_left, r * cell_height))
        for c in range(col + 1):
            pygame.draw.line(self.screen, color, (c * cell_width + width_left, 0),
                             (c * cell_width + width_left, row * cell_height))
