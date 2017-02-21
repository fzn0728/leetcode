# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 20:46:37 2017

@author: Chandler
"""

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x<0:
        flag = -1
        x = abs(x)
    else:
        flag = 1
    reverse_list = []
    list_x = list(str(x))
    for i in range(len(list_x)):
        reverse_list.append(list_x[-i-1])
        result = flag*int(''.join(reverse_list))
    if result > 2147483647:
        return 0
    return result