# %%
a = {'a': 1, 'b': 2}
b = a
b['a'] = 3
print(a)

# %%
import numpy as np

a = {1: np.zeros((2, 2), dtype=int)}
print("a", a[1])

# %%
import numpy as np
from game_logic import GameLogic

game = GameLogic()
game.move(0, 1)
game.show()
