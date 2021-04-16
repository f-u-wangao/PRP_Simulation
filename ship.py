import pygame


class Ship:

    def __init__(self, screen, is_enemy):
        self.screen = screen

        if is_enemy:
            self.image = pygame.image.load('images/ship_enemy.png')
        else:
            self.image = pygame.image.load('images/ship_self.png')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        if is_enemy:
            self.rect.centerx = self.screen_rect.left + 15
            self.rect.centery = self.screen_rect.top + 15
        else:
            self.rect.centerx = self.screen_rect.right - 15
            self.rect.centery = self.screen_rect.bottom - 15

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def reset(self, is_enemy):
        if is_enemy:
            self.rect.centerx = self.screen_rect.left + 15
            self.rect.centery = self.screen_rect.top + 15
        else:
            self.rect.centerx = self.screen_rect.right - 15
            self.rect.centery = self.screen_rect.bottom - 15
