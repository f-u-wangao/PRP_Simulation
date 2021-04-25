from settings import Settings


class GameStats:

    def __init__(self):
        # 导入设置
        self.setting_vis = Settings()
        self.reset_stats()

        self.game_active = False
        self.round = 1

        # 对应操作顺序：1-己方移动, 2-敌方移动, 3-己方发射导弹, 4-己方导弹追踪, 5-敌方发射导弹, 6-敌方导弹追踪
        self.operation = 1

    def reset_stats(self):
        self.round = 1
        self.operation = 1
        self.game_active = False

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
