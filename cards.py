#!/usr/bin/env python3

import itertools


class CardDeck:
    rank = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    suit = {'spades' '\u2660', 'hearts' '\u2665',
            'diamonds' '\u2666', 'clubs' '\u2663'}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @classmethod
    def create_deck(cls):
        p = itertools.product(cls.rank, cls.suit)
        d = []
        for el in p:
            d.append(el)
        return d


if __name__ == '__main__':
    ...
