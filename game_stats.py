class GameStats:

    def __init__(self, settings_vis):
        self.setting_vis = settings_vis
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        pass

    def game_activate(self):
        self.game_active = True
