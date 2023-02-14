#!/usr/bin/env python3

from cards import *
import sys
'''Для запуску скрипту необхідно ввести: python fortune.py та кількість карт від 1 до 36'''
a = random.choices(d, k = int(sys.argv[1]))
print(a)





