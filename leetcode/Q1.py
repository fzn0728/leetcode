# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 16:08:46 2016

@author: Chandler
"""


'''
def twoSum(num, target):
    index = []
    numtosort = num[:]; numtosort.sort()
    i = 0; j = len(numtosort) - 1
    while i < j:
        if numtosort[i] + numtosort[j] == target:
            for k in range(0,len(num)):
                if num[k] == numtosort[i]:
                    index.append(k)
                    break
            for k in range(len(num)-1,-1,-1):
                if num[k] == numtosort[j]:
                    index.append(k)
                    break
            index.sort()
            break
        elif numtosort[i] + numtosort[j] < target:
            i = i + 1
        elif numtosort[i] + numtosort[j] > target:
            j = j - 1
    return index
'''


def twoSum(num,target):
    dict = {}
    for i in xrange(len(num)):
        x = num[i]

        if target - x in dict:
            return [dict[target - x],i]
        dict[x] = i
        
            
            
        