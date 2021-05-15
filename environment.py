from game_logic import GameLogic
from game_stats import GameStats
import time

if __name__ == "__main__":
    stats = GameStats()
    game_logic = GameLogic(stats)
    train_count = 0
    train_count_max = 1000
    time_begin = time.time()
    win_count = 0
    draw_count = 0
    lose_count = 0

    for i in range(train_count_max):
        while True:
            action_self = game_logic.agent[1].choose_action(1)
            action_enemy = game_logic.agent[0].choose_action(0)
            if stats.operation == 1:
                if action_self[0] == 1:
                    game_logic.move(1, 1)
                elif action_self[0] == 2:
                    game_logic.move(1, 2)
                elif action_self[0] == 3:
                    game_logic.move(1, 3)
                elif action_self[0] == 4:
                    game_logic.move(1, 4)

            elif stats.operation == 2:
                if action_enemy[0] == 1:
                    game_logic.move(0, 1)
                elif action_enemy[0] == 2:
                    game_logic.move(0, 2)
                elif action_enemy[0] == 3:
                    game_logic.move(0, 3)
                elif action_enemy[0] == 4:
                    game_logic.move(0, 4)

            elif stats.operation == 3:
                if action_self[1]:
                    game_logic.launch(1)
                else:
                    stats.next_operation()

            elif stats.operation == 4:
                flag_break = False
                for missile_number in range(game_logic.settings_vis.missile_allowed - game_logic.ship_self['missile']):
                    if not game_logic.missile_is_show[1][missile_number]:
                        continue
                    game_over, action = game_logic.trace(1, missile_number)
                    if game_over:
                        win_count += 1
                        game_logic.agent[1].update_win_or_lose(1)
                        game_logic.agent[0].update_win_or_lose(-1)
                        game_logic.reset()
                        stats.reset_stats()
                        flag_break = True
                        break
                if flag_break:
                    break
                stats.next_operation()

            elif stats.operation == 5:
                if action_enemy[1]:
                    game_logic.launch(0)
                else:
                    stats.next_operation()

            elif stats.operation == 6:
                flag_break = False
                for missile_number in range(game_logic.settings_vis.missile_allowed - game_logic.ship_enemy['missile']):
                    if not game_logic.missile_is_show[0][missile_number]:
                        continue
                    game_over, action = game_logic.trace(0, missile_number)
                    if game_over:
                        lose_count += 1
                        game_logic.agent[0].update_win_or_lose(1)
                        game_logic.agent[1].update_win_or_lose(-1)
                        game_logic.reset()
                        stats.reset_stats()
                        flag_break = True
                        break
                if flag_break:
                    break
                stats.next_operation()

            if not game_logic.ship_self['missile'] and not game_logic.ship_enemy['missile']:
                draw_flag = 1
                for k in range(4):
                    if game_logic.missile_is_show[0][k]:
                        draw_flag = 0
                    if game_logic.missile_is_show[1][k]:
                        draw_flag = 0
                if draw_flag == 1:
                    draw_count += 1
                    game_logic.agent[0].update_win_or_lose(0)
                    game_logic.agent[1].update_win_or_lose(0)
                    game_logic.reset()
                    stats.reset_stats()
                    break

        train_count += 1
        if train_count % 100 == 0:
            print("Train count:", train_count)
            print("\tWin rate:", win_count / train_count)
            print("\tDraw rate:", draw_count / train_count)
            print("\tLose rate:", lose_count / train_count)
    time_end = time.time()
    print("Time used:", time_end - time_begin)
