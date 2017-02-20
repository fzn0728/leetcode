# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 10:19:11 2016

@author: Chandler
"""

class Solution(object):
    
    def addTwoNumbers(self,l1,l2):
        output = [] # this defination didn't give the length of [], so indexing would be out of range. I have to use append command
        if (l1 ==[]) | (l2 ==[]):
            if l2 ==[]:
                output = l1
                return output
            elif l1 ==[]:
                output = l2
                return output
        else:   
            for i in range(len(l1)):
                output.append(l1[i] + l2[i])
            for j in range(len(output)):
                if output[j]>=10:
                    output[j] = output[j] - 10
                    if j+1 <= len(output) - 1:
                        output[j+1] = output[j+1] + 1
                    else:
                        output.append(1)
            return output

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        cur = result;
        while l1 or l2:
            cur.val += self.addTwoNodes(l1,l2)
            if cur.val>=10:
                cur.val -=10
                cur.next = ListNode(1) # one digit for next node
            else:
                # Check if there is need to make the next node
                if l1 and l1.next or l2 and l2.next:
                    cur.next = ListNode(0)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return result
                
            
    def addTwoNodes(self, n1, n2):
        if not n1 and not n2:
            None
        if not n1:
            return n2.val
        if not n2:
            return n1.val
        return n1.val+n2.val