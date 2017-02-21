# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 12:07:54 2017

@author: Chandler
"""

class Solution(object): # I have no better solution than the answer
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows<=1:
            return s
        index = 0
        result = ""
        n = len(s)
        for i in range(0,numRows):
            if i==0 or i==numRows-1: #first line and last line
                while index<n:
                    result += s[index]
                    index += 2*numRows-2
                index = i+1 # Index is used to go through the string and find the letter every numRows
            else:
                while index<n:
                    result += s[index]
                    index += 2*numRows-2*i-2
                    if index >=n:
                        break
                    result += s[index] # it seems that no matter how large the numRows is, there are only two pattern need to be consider, 2*n-2i-2 and 2*i
                    index += 2*i
                index = i + 1
ef        return result