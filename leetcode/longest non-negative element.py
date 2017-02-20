# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 12:17:04 2016

@author: Chandler
"""

def solution(S):
    max_sum = 0
    current_sum = 0
    positive = False
    n = len(S)
    
    for i in xrange(n):
        item = S[i]
        print item
        if item <0:
            if (max_sum<current_sum):
                max_sum = current_sum
                current_sum = 0
                print max_sum
        else:
            positive = True
            current_sum += item
                
    if (current_sum > max_sum):
        max_sum = current_sum
    if (positive):
        return max_sum
    return -1
        


ls = [-1,-2,-3,-4,0,-1,5,-6]