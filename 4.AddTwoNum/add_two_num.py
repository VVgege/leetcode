#!/usr/bin/python
# coding=utf-8
# File Name: 4.AddTwoNum/add_two_num.py
# Developer: VVgege
# Data: Tue Feb  3 22:30:17 2015
'''
Question
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
class ListNode:
    def __init__(self, data, next):
        self.val = data
        self.next = None

class solution(object):
    def __init__(self, l1_head=None, l2_head=None):
        self.l1 = l1_head
        self.l2 = l2_head

    #@return a list
    def add_two_num(self):
        l1=self.l1
        l2=self.l2
        carry = 0
        head = ListNode(0,None)
        ptr = head
        while l1 or l2 or carry:
            node = ListNode(carry,None)
            if l1:
                node.val += l1.val
                l1 = l1.next
            if l2:
                node.val += l2.val
                l2 = l2.next
            carry = node.val/10
            node.val = node.val % 10
            ptr.next = node
            ptr = node
        return head.next

if __name__ == '__main__':
    node1_3 = ListNode(3,None)
    node1_2 = ListNode(4,None)
    node1_1 = ListNode(2,None)
    node1_1.next = node1_2
    node1_2.next = node1_3
    print 'list1 is :'
    ll1 = node1_1
    while ll1:
        print ll1.val
        ll1 = ll1.next

    node2_3 = ListNode(4,None)
    node2_2 = ListNode(6,None)
    node2_1 = ListNode(5,None)
    node2_1.next = node2_2
    node2_2.next = node2_3
    print 'list2 is :'
    ll2 = node2_1
    while ll2:
        print ll2.val
        ll2 = ll2.next


    print "The Output is"
    result = solution(node1_1, node2_1)
    l3 = result.add_two_num()
    while l3:
        print l3.val
        l3 = l3.next



