import numpy as np
import itertools

suits = {'H': 'R', 'D': 'R', 'S': 'B', 'C': 'B'}
numbers = [i for i in range(1, 14)]
deck = list(itertools.product(suits.keys(), numbers))

class Solitaire():
    def __init__(self):
        self._deck = deck
        self._cols = [[self._deck.pop(np.random.randint(0, len(self._deck))) for i in range(0, j)] for j in range(1, 8)]
        self._foundations = [[] * 4]
        self._current = []

    def move(self, cur = 0, next = 0, cur_found = False, next_found = False, cur_current = False, next_current = False):
        if cur_current:
            cur_card = self._current[0]
        else:
            cur_card = self._foundations[cur[0]][cur]

        # same = suits.get(cur_card[0]) == suits.get(next_card[0])

        if next_found:
            pass

sol = Solitaire()
for i in sol._cols:
    print(i[0], ' Card ' * (len(i) - 1))
