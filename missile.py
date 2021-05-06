import pygame
from pygame.sprite import Sprite
from settings import Settings


class Missile(Sprite):

    def __init__(self, screen, ship):
        super().__init__()
        self.screen = screen
        self.settings_vis = Settings()

        self.rect = pygame.Rect(0, 0, self.settings_vis.missile_width, self.settings_vis.missile_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.centery = ship.rect.centery

        self.color = self.settings_vis.missile_self_color
        self.speed = self.settings_vis.missile_speed

        self.is_show = True

    def update(self, action):
        if action == [0, 0]:
            self.is_show = False
        for i in range(2):
            if action[i] == 1:
                self.rect.y -= self.speed
            elif action[i] == 2:
                self.rect.y += self.speed
            elif action[i] == 3:
                self.rect.x -= self.speed
            elif action[i] == 4:
                self.rect.x += self.speed

    def draw_missile(self, ship_number):
        if ship_number:
            self.color = self.settings_vis.missile_self_color
        elif not ship_number:
            self.color = self.settings_vis.missile_enemy_color
        pygame.draw.rect(self.screen, self.color, self.rect)
