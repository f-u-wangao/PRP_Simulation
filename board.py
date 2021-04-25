import pygame.font
from settings import Settings

operation_detail = {1: "己方（蓝）移动", 2: "敌方（红）移动", 3: "己方发射导弹", 4: "己方导弹追踪", 5: "敌方发射导弹", 6: "敌方导弹追踪"}


class Board:

    def __init__(self, screen, stats, game_logic):
        # 导入设置
        self.settings_vis = Settings()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.game_logic = game_logic

        # 字体设置
        self.text_color = self.settings_vis.text_color
        self.font_round = pygame.font.SysFont('Consolas', 48)
        self.font_missile = pygame.font.SysFont('Consolas', 26)
        self.font_hint = pygame.font.SysFont('Consolas', 26)
        self.font_detail = pygame.font.SysFont('Consolas-with-Yahei', 20)

        # 初始图像
        self.prep()

    def prep(self):
        round_str = "Round " + str(self.stats.round)
        self.round_image = self.font_round.render(round_str, True, self.text_color, self.settings_vis.background_color)
        missile_str = "Missile remained"
        self.missile_image = self.font_missile.render(missile_str, True, self.text_color,
                                                      self.settings_vis.background_color)
        missile_self_str = "Self:  " + str(self.game_logic.ship_self['missile'])
        self.missile_self_image = self.font_missile.render(missile_self_str, True, self.text_color,
                                                           self.settings_vis.background_color)
        missile_enemy_str = "Enemy: " + str(self.game_logic.ship_enemy['missile'])
        self.missile_enemy_image = self.font_missile.render(missile_enemy_str, True, self.text_color,
                                                            self.settings_vis.background_color)
        hint_str = "In operation " + str(self.stats.operation)
        self.hint_image = self.font_hint.render(hint_str, True, self.text_color,
                                                self.settings_vis.background_color)
        detail_str = operation_detail[self.stats.operation]
        self.detail_image = self.font_detail.render(detail_str, True, self.text_color,
                                                    self.settings_vis.background_color)

        # 在右侧显示信息
        self.round_rect = self.round_image.get_rect()
        self.round_rect.centerx = (self.settings_vis.col * self.settings_vis.cell_width + self.settings_vis.width_left +
                                   self.screen_rect.right) / 2
        self.round_rect.centery = self.screen_rect.centery - 250

        self.missile_rect = self.missile_image.get_rect()
        self.missile_rect.centerx = self.round_rect.centerx
        self.missile_rect.centery = self.screen_rect.centery - 60

        self.missile_self_rect = self.missile_self_image.get_rect()
        self.missile_self_rect.centerx = self.missile_rect.centerx
        self.missile_self_rect.centery = self.screen_rect.centery

        self.missile_enemy_rect = self.missile_enemy_image.get_rect()
        self.missile_enemy_rect.centerx = self.missile_self_rect.centerx
        self.missile_enemy_rect.centery = self.screen_rect.centery + 40

        self.hint_rect = self.hint_image.get_rect()
        self.hint_rect.centerx = (self.settings_vis.col * self.settings_vis.cell_width + self.settings_vis.width_left +
                                  self.screen_rect.right) / 2
        self.hint_rect.centery = self.screen_rect.centery + 200

        self.detail_rect = self.detail_image.get_rect()
        self.detail_rect.centerx = (self.settings_vis.col * self.settings_vis.cell_width + self.settings_vis.width_left
                                    + self.screen_rect.right) / 2
        self.detail_rect.centery = self.screen_rect.centery + 240

    def show(self):
        self.screen.blit(self.round_image, self.round_rect)
        self.screen.blit(self.missile_image, self.missile_rect)
        self.screen.blit(self.missile_self_image, self.missile_self_rect)
        self.screen.blit(self.missile_enemy_image, self.missile_enemy_rect)
        self.screen.blit(self.hint_image, self.hint_rect)
        self.screen.blit(self.detail_image, self.detail_rect)
