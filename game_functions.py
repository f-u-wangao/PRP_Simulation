import sys
import pygame
from missile import Missile


def check_keydown_events(event, screen, settings_vis, stats, ship_self, ship_enemy, missiles, game_logic):
    ship_speed = settings_vis.ship_speed
    if stats.operation == 1:
        if event.key == pygame.K_LEFT and ship_self.rect.left >= ship_speed:
            ship_self.rect.centerx -= ship_speed
            game_logic.move(1, 3)
        elif event.key == pygame.K_RIGHT and ship_self.rect.right <= settings_vis.screen_width - ship_speed:
            ship_self.rect.centerx += ship_speed
            game_logic.move(1, 4)
        elif event.key == pygame.K_UP and ship_self.rect.top >= ship_speed:
            ship_self.rect.centery -= ship_speed
            game_logic.move(1, 1)
        elif event.key == pygame.K_DOWN and ship_self.rect.bottom <= settings_vis.screen_height - ship_speed:
            ship_self.rect.centery += ship_speed
            game_logic.move(1, 2)
    elif stats.operation == 2:
        if event.key == pygame.K_LEFT and ship_enemy.rect.left >= ship_speed:
            ship_enemy.rect.centerx -= ship_speed
            game_logic.move(0, 3)
        elif event.key == pygame.K_RIGHT and ship_enemy.rect.right <= settings_vis.screen_width - ship_speed:
            ship_enemy.rect.centerx += ship_speed
            game_logic.move(0, 4)
        elif event.key == pygame.K_UP and ship_enemy.rect.top >= ship_speed:
            ship_enemy.rect.centery -= ship_speed
            game_logic.move(0, 1)
        elif event.key == pygame.K_DOWN and ship_enemy.rect.bottom <= settings_vis.screen_height - ship_speed:
            ship_enemy.rect.centery += ship_speed
            game_logic.move(0, 2)
    elif stats.operation == 3:
        if event.key == pygame.K_SPACE:
            fire_missile(settings_vis, screen, ship_self, missiles)
            game_logic.launch(1)
        elif event.key == pygame.K_n:
            stats.next_operation()
    elif stats.operation == 4:
        for missile_number in range(settings_vis.missile_allowed - game_logic.ship_self['missile']):
            if game_logic.trace(1, missile_number):
                stats.reset_stats()
        stats.next_operation()
    elif stats.operation == 5:
        if event.key == pygame.K_SPACE:
            fire_missile(settings_vis, screen, ship_self, missiles)
            game_logic.launch(0)
        elif event.key == pygame.K_n:
            stats.next_operation()
    elif stats.operation == 6:
        for missile_number in range(settings_vis.missile_allowed - game_logic.ship_enemy['missile']):
            if game_logic.trace(0, missile_number):
                stats.reset_stats()
        stats.next_operation()

    if event.key == pygame.K_q:
        sys.exit()


def check_events(settings_vis, screen, stats, play_button, ship_self, ship_enemy, missiles, game_logic):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif stats.game_active and event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, settings_vis, stats, ship_self, ship_enemy, missiles, game_logic)

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, ship_self, missiles)


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
        board.prep()
        board.show()
    pygame.display.flip()


def fire_missile(settings_vis, screen, ship, missiles):
    if len(missiles) < settings_vis.missile_allowed:
        new_missile = Missile(settings_vis, screen, ship)
        missiles.add(new_missile)
