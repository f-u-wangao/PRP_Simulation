from settings import Settings


class GameStats:

    def __init__(self):
        # 导入设置
        self.setting_vis = Settings()
        self.game_active = False
        self.reset_stats()

        self.round = 1
        # 对应操作顺序：1-己方移动, 2-敌方移动, 3-己方发射导弹, 4-己方导弹追踪, 5-敌方发射导弹, 6-敌方导弹追踪
        self.operation = 1

        # 用于在 game_function 中控制调用 Agent 的频率
        self.count = 1

    def reset_stats(self):
        self.round = 1
        self.operation = 1
        self.count = 1
        if self.setting_vis.control_flag:
            self.game_active = False
        else:
            self.game_active = True

    def next_operation(self):
        if self.operation <= 5:
            self.operation += 1
        else:
            self.next_round()

    def next_round(self):
        self.round += 1
        self.operation = 1

    def game_activate(self):
        self.game_active = True
