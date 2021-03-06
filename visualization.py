import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from background import Background
from game_stats import GameStats
from button import Button
from board import Board
from game_logic import GameLogic


def run_game():
    pygame.init()

    # 导入设置
    settings_vis = Settings()

    # 初始化设置
    screen = pygame.display.set_mode([settings_vis.screen_width, settings_vis.screen_height])
    screen.fill(settings_vis.background_color)
    pygame.display.set_caption("Aircraft Battle")

    # 画背景网格
    background = Background(screen, settings_vis.screen_width, settings_vis.screen_height)

    # 创建Play按钮
    play_button = Button(settings_vis, screen, "Play")

    # 导入双方飞船
    ship_self = Ship(screen, 0)
    ship_enemy = Ship(screen, 1)

    # 创建双方飞船导弹组
    missiles_self = []
    missiles_enemy = []

    # 创建存储统计信息的实例，导入游戏逻辑，并在右侧显示
    stats = GameStats()
    game_logic = GameLogic(stats)
    board = Board(screen, stats, game_logic)

    if not settings_vis.control_flag and not settings_vis.is_show:
        pygame.display.iconify()

    # 游戏主循环
    while True:
        gf.check_events(settings_vis, screen, stats, play_button, ship_self, ship_enemy, missiles_self, missiles_enemy,
                        game_logic)
        gf.update_screen(settings_vis, screen, stats, board, ship_self, ship_enemy, missiles_self, missiles_enemy,
                         play_button, background)


run_game()
