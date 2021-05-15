import sys
import pygame
from missile import Missile
from ship import Ship


def check_keydown_events(event, screen, settings_vis, stats, ship_self, ship_enemy, missiles_self, missiles_enemy,
                         game_logic):
    ship_speed = settings_vis.ship_speed
    if stats.operation == 1:
        if event.key == pygame.K_LEFT:
            if game_logic.move(1, 3):
                ship_self.rect.centerx -= ship_speed
        elif event.key == pygame.K_RIGHT:
            if game_logic.move(1, 4):
                ship_self.rect.centerx += ship_speed
        elif event.key == pygame.K_UP:
            if game_logic.move(1, 1):
                ship_self.rect.centery -= ship_speed
        elif event.key == pygame.K_DOWN:
            if game_logic.move(1, 2):
                ship_self.rect.centery += ship_speed
    elif stats.operation == 2:
        if event.key == pygame.K_LEFT:
            if game_logic.move(0, 3):
                ship_enemy.rect.centerx -= ship_speed
        elif event.key == pygame.K_RIGHT:
            if game_logic.move(0, 4):
                ship_enemy.rect.centerx += ship_speed
        elif event.key == pygame.K_UP:
            if game_logic.move(0, 1):
                ship_enemy.rect.centery -= ship_speed
        elif event.key == pygame.K_DOWN:
            if game_logic.move(0, 2):
                ship_enemy.rect.centery += ship_speed
    elif stats.operation == 3:
        if event.key == pygame.K_SPACE:
            fire_missile(settings_vis, screen, ship_self, missiles_self)
            game_logic.launch(1)
        elif event.key == pygame.K_n:
            stats.next_operation()
    elif stats.operation == 4:
        for missile_number in range(settings_vis.missile_allowed - game_logic.ship_self['missile']):
            if not missiles_self[missile_number].is_show:
                continue
            game_over, action = game_logic.trace(1, missile_number)
            if game_over:
                reset_all(stats, ship_self, ship_enemy, missiles_self, missiles_enemy, game_logic)
                return
            missiles_self[missile_number].update(action)
        stats.next_operation()
    elif stats.operation == 5:
        if event.key == pygame.K_SPACE:
            fire_missile(settings_vis, screen, ship_enemy, missiles_enemy)
            game_logic.launch(0)
        elif event.key == pygame.K_n:
            stats.next_operation()
    elif stats.operation == 6:
        for missile_number in range(settings_vis.missile_allowed - game_logic.ship_enemy['missile']):
            if not missiles_enemy[missile_number].is_show:
                continue
            game_over, action = game_logic.trace(0, missile_number)
            if game_over:
                reset_all(stats, ship_self, ship_enemy, missiles_self, missiles_enemy, game_logic)
                return
            missiles_enemy[missile_number].update(action)
        stats.next_operation()

    check_draw(stats, ship_self, ship_enemy, missiles_self, missiles_enemy, game_logic)


def check_agent_actions(settings_vis, screen, stats, ship_self, ship_enemy, missiles_self, missiles_enemy, game_logic):
    ship_speed = settings_vis.ship_speed
    action_self = game_logic.agent[1].choose_action(1)
    action_enemy = game_logic.agent[0].choose_action(0)
    is_show = settings_vis.is_show

    if stats.operation == 1:
        if action_self[0] == 1:
            if game_logic.move(1, 1) and is_show:
                ship_self.rect.centery -= ship_speed
        elif action_self[0] == 2:
            if game_logic.move(1, 2) and is_show:
                ship_self.rect.centery += ship_speed
        elif action_self[0] == 3:
            if game_logic.move(1, 3) and is_show:
                ship_self.rect.centerx -= ship_speed
        elif action_self[0] == 4:
            if game_logic.move(1, 4) and is_show:
                ship_self.rect.centerx += ship_speed

    elif stats.operation == 2:
        if action_enemy[0] == 1:
            if game_logic.move(0, 1) and is_show:
                ship_enemy.rect.centery -= ship_speed
        elif action_enemy[0] == 2:
            if game_logic.move(0, 2) and is_show:
                ship_enemy.rect.centery += ship_speed
        elif action_enemy[0] == 3:
            if game_logic.move(0, 3) and is_show:
                ship_enemy.rect.centerx -= ship_speed
        elif action_enemy[0] == 4:
            if game_logic.move(0, 4) and is_show:
                ship_enemy.rect.centerx += ship_speed

    elif stats.operation == 3:
        if action_self[1]:
            fire_missile(settings_vis, screen, ship_self, missiles_self)
            game_logic.launch(1)
        else:
            stats.next_operation()

    elif stats.operation == 4:
        for missile_number in range(settings_vis.missile_allowed - game_logic.ship_self['missile']):
            if not game_logic.missile_is_show[1][missile_number]:
                continue
            game_over, action = game_logic.trace(1, missile_number)
            if game_over:
                reset_all(stats, ship_self, ship_enemy, missiles_self, missiles_enemy, game_logic)
                return
            missiles_self[missile_number].update(action)
        stats.next_operation()

    elif stats.operation == 5:
        if action_enemy[1]:
            fire_missile(settings_vis, screen, ship_enemy, missiles_enemy)
            game_logic.launch(0)
        else:
            stats.next_operation()

    elif stats.operation == 6:
        for missile_number in range(settings_vis.missile_allowed - game_logic.ship_enemy['missile']):
            if not game_logic.missile_is_show[0][missile_number]:
                continue
            game_over, action = game_logic.trace(0, missile_number)
            if game_over:
                reset_all(stats, ship_self, ship_enemy, missiles_self, missiles_enemy, game_logic)
                return
            missiles_enemy[missile_number].update(action)
        stats.next_operation()

    check_draw(stats, ship_self, ship_enemy, missiles_self, missiles_enemy, game_logic)


def check_events(settings_vis, screen, stats, play_button, ship_self, ship_enemy, missiles_self, missiles_enemy,
                 game_logic):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

        elif settings_vis.control_flag and stats.game_active and event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, settings_vis, stats, ship_self, ship_enemy, missiles_self,
                                 missiles_enemy, game_logic)

        elif settings_vis.control_flag and event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, ship_self, missiles_self, missiles_enemy)

    # 调用 Agent 控制
    if not settings_vis.control_flag:
        if not settings_vis.is_show:
            check_agent_actions(settings_vis, screen, stats, ship_self, ship_enemy, missiles_self, missiles_enemy,
                                game_logic)
        elif stats.count == settings_vis.count_max:
            stats.count = 0
            check_agent_actions(settings_vis, screen, stats, ship_self, ship_enemy, missiles_self, missiles_enemy,
                                game_logic)
        else:
            stats.count += 1


def check_play_button(stats, play_button, mouse_x, mouse_y, ship, missiles_self, missiles_enemy):
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        stats.reset_stats()
        stats.game_active = True

        # 设置鼠标不可见，游戏结束时需设置为可见
        pygame.mouse.set_visible(False)

        # 飞船回位，导弹数量清零
        ship.reset(0)
        missiles_self.clear()
        missiles_enemy.clear()


def update_screen(settings_vis, screen, stats, board, ship_self, ship_enemy, missiles_self, missiles_enemy, play_button,
                  background):
    screen.fill(settings_vis.background_color)
    for missile in missiles_self:
        if missile.is_show:
            missile.draw_missile(1)
    for missile in missiles_enemy:
        if missile.is_show:
            missile.draw_missile(0)

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
        new_missile = Missile(screen, ship)
        missiles.append(new_missile)


# 如果导弹都用完且场上没有导弹存在，平局
def check_draw(stats, ship_self, ship_enemy, missiles_self, missiles_enemy, game_logic):
    if not game_logic.ship_self['missile'] and not game_logic.ship_enemy['missile']:
        draw_flag = 1
        for missile in missiles_self:
            if missile.is_show:
                draw_flag = 0
        for missile in missiles_enemy:
            if missile.is_show:
                draw_flag = 0
        if draw_flag == 1:
            print("Draw!")
            reset_all(stats, ship_self, ship_enemy, missiles_self, missiles_enemy, game_logic)


def reset_all(stats, ship_self, ship_enemy, missiles_self, missiles_enemy, game_logic):
    stats.reset_stats()

    # 重置双方飞船
    ship_self.reset(1)
    ship_enemy.reset(0)

    # 重置双方飞船导弹组
    missiles_self = []
    missiles_enemy = []

    # 重置游戏逻辑
    game_logic.reset()
