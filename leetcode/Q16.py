# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 16:41:13 2017

@author: Chandler
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        i = 0; solution=0; diff_flag = float('inf')
        while i<len(nums)-2:
            left = i+1
            right = len(nums)-1

            while left < right:
                diff = abs(nums[i]+nums[left]+nums[right]-target)
                if diff == 0:
                    return nums[i]+nums[left]+nums[right]
                if diff<diff_flag:
                    solution = nums[i]+nums[left]+nums[right]
                    diff_flag = diff
                if nums[i]+nums[left]+nums[right]-target <0:
                    left += 1
                elif nums[i]+nums[left]+nums[right]-target >0:
                    right -= 1 # stupid mistake : right -= right
                    # print('go to right')
                    # print([nums[left],nums[i],nums[right]])
            i += 1
            # print('run one times')
        return solution
            