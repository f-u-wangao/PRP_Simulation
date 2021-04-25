from settings import Settings
import numpy as np
import win32api
import win32con


class GameLogic:

    def __init__(self):
        self.chessboard = np.zeros([30, 30], dtype=int)
        self.ship_self = {'location': np.array([29, 29], dtype=int), 'missile': 4}
        self.ship_enemy = {'location': np.array([0, 0], dtype=int), 'missile': 4}

    def get_ship(self, ship_number):
        if ship_number == 1:
            ship = self.ship_self
        elif ship_number == 0:
            ship = self.ship_enemy
        else:
            win32api.MessageBox(0, "输入的 ship_number 无效，可能影响程序运行！", "警告", win32con.MB_ICONWARNING)
            ship = self.ship_self
        return ship

    # 返回移动是否成功
    def move(self, ship_number, direction):
        """
        :param ship_number: 0 代表对敌机操作，1 代表对己方飞机操作
        :param direction: 1, 2, 3, 4 分别对应 上，下，左，右
        :return: move 操作是否成功
        """

        ship = self.get_ship(ship_number)
        flag_is_moved = False

        if direction == 1:
            if ship['location'][1] >= 1:
                ship['location'][1] -= 1
                flag_is_moved = True
        elif direction == 2:
            if ship['location'][1] <= 28:
                ship['location'][1] += 1
                flag_is_moved = True
        elif direction == 3:
            if ship['location'][0] >= 1:
                ship['location'][0] -= 1
                flag_is_moved = True
        elif direction == 4:
            if ship['location'][0] <= 28:
                ship['location'][0] += 1
                flag_is_moved = True
        else:
            win32api.MessageBox(0, "输入的 direction 无效，可能影响程序运行！", "警告", win32con.MB_ICONWARNING)
        return flag_is_moved

    def launch(self, ship_number):
        ship = self.get_ship(ship_number)

    def show(self):
        print("chessboard:\n", self.chessboard)
        print("ship_self: location: ", self.ship_self['location'], "\tmissile:", self.ship_self['missile'])
        print("ship_enemy: location: ", self.ship_enemy['location'], "\tmissile:", self.ship_enemy['missile'])
