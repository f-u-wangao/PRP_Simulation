import numpy as np


class Agent:

    def __init__(self):
        self.ship_self = {'location': np.array([29, 29], dtype=int), 'missile': 4}
        self.ship_enemy = {'location': np.array([0, 0], dtype=int), 'missile': 4}
        self.missile_location = [{}, {}]
        self.is_win_or_lose = 0  # 0 - 未结束，1 - win，-1 - lose

    def get_ship(self, ship_number):
        ship = self.ship_self
        if ship_number == 1:
            ship = self.ship_self
        elif ship_number == 0:
            ship = self.ship_enemy
        return ship

    def update_ship_location(self, ship_number, ship_location):
        ship = self.get_ship(ship_number)
        ship['location'] = ship_location

    def update_missile_location(self, ship_number, missile_number, missile_location):
        self.missile_location[ship_number][missile_number] = missile_location
        ship = self.get_ship(ship_number)
        if ship['missile'] > 3 - missile_number:
            ship['missile'] = 3 - missile_number

    def update_win_or_lose(self, win_or_lose):
        self.is_win_or_lose = win_or_lose

    def choose_action(self, ship_number):
        """
        :return: 元组(move_direction, fire_flag)，move_direction 为 1-4，fire_flag 为 True 和 False
        """
        move_action = [1, 2, 3, 4]
        if ship_number == 1:
            move_p = [0.4, 0.1, 0.4, 0.1]
        else:
            move_p = [0.1, 0.4, 0.1, 0.4]
        fire_action = [True, False]
        fire_p = [0.1, 0.9]
        action = (np.random.choice(move_action, p=move_p), np.random.choice(fire_action, p=fire_p))
        if action[1] and self.ship_self['missile'] >= 1:
            self.ship_self['missile'] -= 1
        return action
