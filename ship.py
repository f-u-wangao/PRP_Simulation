import pygame
from settings import Settings


class Ship:

    def __init__(self, screen, is_enemy):
        # 导入设置
        self.settings_vis = Settings()
        self.screen = screen
        self.ship_speed = self.settings_vis.ship_speed
        self.width_left = self.settings_vis.width_left

        if is_enemy:
            self.image = pygame.image.load('images/ship_enemy.png')
        else:
            self.image = pygame.image.load('images/ship_self.png')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        if is_enemy:
            self.rect.centerx = self.screen_rect.left + self.ship_speed / 2 + self.width_left
            self.rect.centery = self.screen_rect.top + self.ship_speed / 2
        else:
            self.rect.centerx = self.screen_rect.left + self.ship_speed * 29.5 + self.width_left
            self.rect.centery = self.screen_rect.bottom - self.ship_speed / 2

    def blitme(self, flag):
        if not flag:
            self.image.set_alpha(50)
        else:
            self.image.set_alpha(255)
        self.screen.blit(self.image, self.rect)

    def reset(self, is_enemy):
        if is_enemy:
            self.rect.centerx = self.screen_rect.left + self.ship_speed / 2 + self.width_left
            self.rect.centery = self.screen_rect.top + self.ship_speed / 2
        else:
            self.rect.centerx = self.screen_rect.left + self.ship_speed * 29.5 + self.width_left
            self.rect.centery = self.screen_rect.bottom - self.ship_speed / 2
