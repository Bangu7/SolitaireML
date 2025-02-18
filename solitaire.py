import numpy as np
import itertools
import cards

class Solitaire():
    def __init__(self):
        self._deck = cards.Deck()
        self._cols = [cards.Hand(self._deck, i) for i in range(1, 8)]
        self._foundations = [cards.Hand(self._deck, 0) for i in range(4)]
        self._current = [cards.Hand(self._deck, 0)]

        for col in self._cols:
            col.show(0)

    def move_cols(self, cur = (0, 0), next = (0, 0)):
        cur_card = self._cols[cur[0]][cur[1]]
        next_card = self._cols[cur[0]][cur[1]]

        # if cur_card[]

        # if suits.get(cur_card[0]) == suits.get(next_card[0]):
        #     return
        
        # if cur_card[1] != (next_card[1] - 1):
        #     return

    
    def move_to_found():
        pass
        # same_suit = cur_card[0] == next_card[0]

            
np.random.seed(10)
sol = Solitaire()
for i in sol._cols:
    for j in i._hand:
        if j._revealed:
            print(j, end=' ')
    print()