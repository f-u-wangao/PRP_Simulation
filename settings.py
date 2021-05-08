class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 900
        self.background_color = (230, 230, 230)
        self.text_color = (30, 30, 30)

        self.missile_speed = 30
        self.missile_width = 10
        self.missile_height = 15
        self.missile_self_color = 17, 160, 255
        self.missile_enemy_color = 226, 63, 226
        self.missile_allowed = 4
        self.missile_view = 6

        self.button_color = 0, 200, 0
        self.button_text_color = 255, 255, 255

        self.ship_speed = 30
        self.width_left = 30
        self.cell_width = 30
        self.cell_height = 30
        self.row = 30
        self.col = 30

        # True 为手动控制，False 为调用 Agent 控制
        self.control_flag = False
        self.is_show = True  # 仅在 Agent 控制时有效
        self.count_max = 100  # 用来控制每一个动作显示的时间
