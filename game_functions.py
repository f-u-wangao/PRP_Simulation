import sys
import pygame
from missile import Missile


def check_keydown_events(event, screen, settings_vis, ship, missiles):
    ship_speed = settings_vis.ship_speed
    if event.key == pygame.K_LEFT and ship.rect.left >= ship_speed:
        ship.rect.centerx -= ship_speed
    elif event.key == pygame.K_RIGHT and ship.rect.right <= settings_vis.screen_width - ship_speed:
        ship.rect.centerx += ship_speed
    elif event.key == pygame.K_UP and ship.rect.top >= ship_speed:
        ship.rect.centery -= ship_speed
    elif event.key == pygame.K_DOWN and ship.rect.bottom <= settings_vis.screen_height - ship_speed:
        ship.rect.centery += ship_speed

    elif event.key == pygame.K_SPACE:
        fire_missile(settings_vis, screen, ship, missiles)

    elif event.key == pygame.K_q:
        sys.exit()


def check_events(settings_vis, screen, stats, play_button, ship, missiles):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif stats.game_active and event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, settings_vis, ship, missiles)

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, ship, missiles)


def check_play_button(stats, play_button, mouse_x, mouse_y, ship, missiles):
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        stats.reset_stats()
        stats.game_active = True

        # 设置鼠标不可见，游戏结束时需设置为可见
        pygame.mouse.set_visible(False)

        # 飞船回位，导弹数量清零
        ship.reset(0)
        missiles.empty()


def update_screen(settings_vis, screen, stats, board, ship_self, ship_enemy, missiles_self, missiles_enemy, play_button,
                  background):
    screen.fill(settings_vis.background_color)
    for missile in missiles_self.sprites():
        missile.draw_missile()
    for missile in missiles_enemy.sprites():
        missile.draw_missile()

    if not stats.game_active:
        background.draw_grid(0)
        play_button.draw_button()
        ship_self.blitme(0)
        ship_enemy.blitme(0)
    else:
        background.draw_grid(1)
        ship_self.blitme(1)
        ship_enemy.blitme(1)
        board.show()
    pygame.display.flip()


def fire_missile(settings_vis, screen, ship, missiles):
    if len(missiles) < settings_vis.missile_allowed:
        new_missile = Missile(settings_vis, screen, ship)
        missiles.add(new_missile)
