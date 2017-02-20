# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 17:36:42 2016

@author: Chandler
"""
'''
def threeSum(nums):
    dict = {}
    list = []
    newlist = []
    for l in xrange(len(nums)):
        dict[nums[l]] = l
    return dict  
    
    
    for i in xrange(len(nums)):
        for j in xrange(i,len(nums)):
            if 0-nums[i]-nums[j] in dict.keys()[j:]:
                list = [nums[i],nums[j],dict[-nums[i]-nums[j]]]
                newlist.append(list)
    return newlist.sort()
    
    
num    
    

dict = {}
nums = [-1,0,1,2,-1,-4]
for l in xrange(len(nums)):
    dict[nums[l]] = l
    
'''
#hash may not work since there is duplicated number

def threeSum(nums):
    nums.sort()
    solution = []
    for i in xrange(len(nums)-1):
        if i>0 and nums[i] == nums[i-1]:
            continue# consider duplicated number
        left = i+1
        right = len(nums) - 1 # Pay attention since len of nums is one larger than the max index
        while left<right:
            val = nums[i]+nums[left]+nums[right]
            if val == 0 and [nums[i],nums[left],nums[right]] not in solution:
                solution.append([nums[i],nums[left],nums[right]])
                left = left + 1
                right = right - 1
            elif val<0:
                left = left + 1
            else:
                right = right - 1
    return solution
        