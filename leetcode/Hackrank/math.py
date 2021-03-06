# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 22:33:52 2016

@author: Chandler
"""

def zigzag(n):
    def move(i, j):
        if j < (n - 1):
            return max(0, i-1), j+1
        else:
            return i+1, j
    a = [[0] * n for _ in range(n)]
    x, y = 0, 0
    for v in range(n * n):
        print('v is %d' %v)
        a[y][x] = v
        if (x + y) & 1:
            x, y = move(x, y)
        else:
            y, x = move(y, x)
    return a



a = zigzag(5)
from pprint import pprint
pprint(zigzag(5))