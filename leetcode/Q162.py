# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 23:42:47 2017

@author: Chandler
"""



def findPeakElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left = 0
    right = len(nums)-1
    if left == right:
        return 0
    while left<right:
        mid = (left+right)//2
        # print(mid)

        if nums[mid]<nums[mid+1]:
            left = mid + 1
        elif nums[mid]<nums[mid-1]:
            right = mid            
        else: # This part is important, bc we need to make sure that every time either left or righi need to move, finally they will converge to mid
        # However, if we set if and elif, no else, then it will never end
            return mid
    return left 

'''    
class Solution(object):
def findPeakElement(self, nums):
"""
:type nums: List[int]
:rtype: int
"""
left, right = 0, len(nums) - 1
while left < right:
mid = (right + left) // 2
if nums[mid] < nums[mid + 1]:
left = mid + 1
else:
right = mid
return left
'''