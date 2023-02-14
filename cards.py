#!/usr/bin/env python3

import itertools
import random

ranks = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
# or  ranks = list(range(6, 10 + 1)) + list('JQKA')
suits = {'spades': '\u2660',
        'hearts': '\u2665',
        'diamonds': '\u2666',
        'clubs': '\u2663'
}
class Card:
    __slots__ = 'rank', 'suit'  # consume less memory

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

p = itertools.product(ranks, suits)
d = []
for el in p:
    d.append(el)

if __name__ == '__main__':
    ...
