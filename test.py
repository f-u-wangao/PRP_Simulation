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

# %%
for i in range(0):
    print(i)

# %%
import numpy as np

a = np.array([1, 2], dtype=int)
b = {}
b[1] = a
c = b[1]
c = np.array([3, 4], dtype=int)
print(b)

a = np.random.random()
print(a)

# %%
a = [1, 2, 3]


def add(x):
    x.append(4)


add(a)
print(a)

# %%
a = [{1: 'a', 2: 'b'}, {3: 'c', 4: 'd'}]
a = [{}, {}]
print(a)
