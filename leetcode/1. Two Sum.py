# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 09:04:00 2016

@author: Chandler
"""

'''
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i] + nums[j] == target:
                break
    return (nums[i],nums[j])
'''


class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        sortedNum = sorted(num)
        count = 0
        for i in sortedNum:
            rest = target - i
            low = 0
            high = len(num) -1
 
            while (low <= high):
                count +=1
                mid = int((low + high) / 2)
                if rest < sortedNum[mid]:
                    high = mid - 1
                    continue
                if rest > sortedNum[mid]:
                    low = mid + 1
                    continue
                if rest == sortedNum[mid]:
                    index1 = num.index(i)
                    num[num.index(i)] = "obtained"
                    index2 = num.index(rest)
                    if index1 > index2:
                        index1, index2 = index2, index1
                    return index1+1, index2+1         
        
        
    
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map={}
        for index, value in enumerate(nums):
            hash_map[value] = index # you should put value into dictionary's keys, so that you can easily find the keys using 'in' command
        for index, value in enumerate(nums):
            if target - value in hash_map:
                index2 = hash_map[target-value]
                if index != index2:
                    return [index+1, index2+1]
