# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 12:32:45 2017

@author: Chandler
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ### empty
        if s is None:
            return
        ### single
        n = len(s)
        if n == 1:
            return s
        left_index, right_index, current_halflen, largest_len = 0,0,0,0
        ### main part
        for i in range(0,n):
            ### odd
            for j in range(1,min(i+1,n-i)): # This place, when it is odd, we need to at least (-1/+1), when it comes to even, it is (0,+1), no need to start with one, so we start with zero
                if (s[i-j]==s[i+j]):
                    current_halflen +=1
                else:
                    break
            if current_halflen>=largest_len: # odd has higher pirority than even, bc given same current_length, odd is larger than even
                # print('Odd')
                # print(i)
                # print(j)
                largest_len = current_halflen
                left_index = i-current_halflen
                right_index = i+current_halflen
            current_halflen = 0
            ### Even
            for j in range(0,min(i+1,n-i-1)):
                if (s[i-j]==s[i+j+1]):
                    current_halflen +=1
                else:
                    break
            if current_halflen>largest_len:
                # print('Even')
                largest_len = current_halflen
                left_index = i-current_halflen+1
                right_index = i+current_halflen
                # print(i)
                # print(current_halflen)
                # print(left_index)
                # print(right_index)
            current_halflen = 0
        # return largest_len, left_index, right_index  
        return s[left_index:right_index+1]
                