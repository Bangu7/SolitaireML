import itertools as it
import numpy as np

suits = {'Hearts': 'Red', 'Diamonds': 'Red', 'Spades': 'Black', 'Clubs': 'Black'}
# names = {1: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven',
#          8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King'}
names = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

class Card():
    def __init__(self, pos, suit, reveal = False):
        self._pos = pos % 13
        self._suit = suit
        self._revealed = reveal

    def __str__(self):
        return names[self._pos] + ' of ' + self._suit
    
    def show(self):
        self._revealed = True

    def hide(self):
        self._revealed = False

class Deck():
    def __init__(self, fill = True):
        self._deck = []
        for s in suits.keys():
            for pos in range(13):
                self._deck.append(Card(pos, s))

    def get_deck(self):
        return self._deck
    
    def is_empty(self):
        return True if len(self._deck) == 0 else False

    def remove_random(self) -> Card | None:
        if not self.is_empty():
            return self._deck.pop(np.random.randint(0, len(self._deck)))
    
    def remove_card(self, card: Card):
        self._deck.remove(card)

    def add_card(self, card: Card):
        self._deck.append(card)

    def add_deck(self, cards: list[Card]):
        for card in cards:
            self.add_card(card)

class Hand():
    def __init__(self, deck: Deck, draw: int, show = False):
        self._hand = [deck.remove_random().show() for i in range(draw)] if show else [deck.remove_random() for i in range(draw)]

    def show(self, pos):
        if pos >= len(self._hand):
            return
        self._hand[pos].show()

    def show_all(self):
        for i in range(len(self._hand)):
            self.show(i)
        
    def hide(self, pos):
        if pos >= len(self._hand):
            return
        self._hand[pos].hide()

    def hide_all(self):
        for i in range(len(self._hand)):
            self.hide(i)

    def get_hand(self):
        return self._hand

# d = Deck()
# for i in d._deck:
#     print(i) 