import random

from components.card import Card


class Board:

    def __init__(self):
        self.cards = []
        self.shuffle()

    def shuffle(self):

        tab_to_shuffle = []
        for g in range(20):
            tab_to_shuffle.append(g + 1)
            tab_to_shuffle.append(g + 1)

        random.shuffle(tab_to_shuffle)

        for i in range(4):
            for j in range(10):
                self.cards.append(Card(tab_to_shuffle[i * 10 + j], j * 126 + 4*(j+1) + 102, i * 178 + 4*(i+1) + 30))

    def get_card(self, n):
        return self.cards[n]
