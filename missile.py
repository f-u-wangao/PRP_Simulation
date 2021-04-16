import pygame
from pygame.sprite import Sprite


class Missile(Sprite):

    def __init__(self, settings_vis, screen, ship):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings_vis.missile_width, settings_vis.missile_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.color = settings_vis.missile_color
        self.speed = settings_vis.missile_speed

    def update(self):
        self.rect.y -= self.speed

    def draw_missile(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
