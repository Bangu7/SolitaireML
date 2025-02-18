import itertools as it

suits = {'Hearts': 'Red', 'Diamonds': 'Red', 'Spades': 'Black', 'Clubs': 'Black'}
# names = {1: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven',
#          8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King'}
names = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

class Card():
    def __init__(self, pos, suit):
        self._pos = pos % 13
        self._suit = suit

    def __str__(self):
        return names[self._pos] + ' of ' + self._suit
        

class Deck():
    def __init__(self):
        self._deck = []
        for s in suits.keys():
            for pos in range(13):
                self._deck.append(Card(pos, s))

d = Deck()
for i in d._deck:
    print(i) 