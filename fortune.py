#!/usr/bin/env python3

from cards import CardDeck
import sys
import random
# Для запуску скрипту необхідно ввести:
# python fortune.py та кількість карт від 1 до 36
deck = CardDeck
a = random.choices(deck.create_deck(), k=int(sys.argv[1]))
print(a)
