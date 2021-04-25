import pygame.font
from settings import Settings


class Board:

    def __init__(self, screen, stats):
        # 导入设置
        self.settings_vis = Settings()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats

        # 字体设置
        self.text_color = self.settings_vis.text_color
        self.font_round = pygame.font.SysFont('Consolas', 48)
        self.font_missile = pygame.font.SysFont('Consolas', 26)

        # 初始图像
        self.prep()

    def prep(self):
        round_str = "Round " + str(self.stats.round)
        self.round_image = self.font_round.render(round_str, True, self.text_color, self.settings_vis.background_color)
        missile_str = "Missile remained"
        self.missile_image = self.font_missile.render(missile_str, True, self.text_color,
                                                      self.settings_vis.background_color)
        missile_self_str = "Self: "
        self.missile_self_image = self.font_missile.render(missile_self_str, True, self.text_color,
                                                           self.settings_vis.background_color)
        missile_enemy_str = "Enemy: "
        self.missile_enemy_image = self.font_missile.render(missile_enemy_str, True, self.text_color,
                                                            self.settings_vis.background_color)

        # 在右侧显示信息
        self.round_rect = self.round_image.get_rect()
        self.round_rect.centerx = (self.settings_vis.col * self.settings_vis.cell_width + self.settings_vis.width_left +
                                   self.screen_rect.right) / 2
        self.round_rect.centery = self.screen_rect.centery - 250

        self.missile_rect = self.missile_image.get_rect()
        self.missile_rect.centerx = (self.settings_vis.col * self.settings_vis.cell_width + self.settings_vis.width_left
                                     + self.screen_rect.right) / 2
        self.missile_rect.centery = self.screen_rect.centery - 60

        self.missile_self_rect = self.missile_self_image.get_rect()
        self.missile_self_rect.left = self.missile_rect.left
        self.missile_self_rect.centery = self.screen_rect.centery

        self.missile_enemy_rect = self.missile_enemy_image.get_rect()
        self.missile_enemy_rect.left = self.missile_rect.left
        self.missile_enemy_rect.centery = self.screen_rect.centery + 40

    def show(self):
        self.screen.blit(self.round_image, self.round_rect)
        self.screen.blit(self.missile_image, self.missile_rect)
        self.screen.blit(self.missile_self_image, self.missile_self_rect)
        self.screen.blit(self.missile_enemy_image, self.missile_enemy_rect)
