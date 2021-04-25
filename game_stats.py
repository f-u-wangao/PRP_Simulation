from settings import Settings


class GameStats:

    def __init__(self):
        # 导入设置
        self.setting_vis = Settings()
        self.reset_stats()

        self.game_active = False
        self.round = 1

    def reset_stats(self):
        self.round = 1

    def next_round(self):
        self.round += 1

    def game_activate(self):
        self.game_active = True
