#!/usr/bin/python
# coding=utf-8
# File Name: 5.SingleNum/single_num.py
# Developer: VVgege
# Data: Tue Feb  3 22:30:56 2015
'''
Question
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''
class solution(object):
    def __init__(self, list_a=[]):
        self.list_a = list_a

    def single_num(self):
        result = 0
        for i in self.list_a:
            result ^= i
        return result

if __name__ == '__main__':

    #test
    my_list = [1,2,3,1,4,3,4,5,7,5,7]
    my_solution = solution(my_list)
    output = my_solution.single_num()
    print 'The Input is :%s' % my_list
    print 'The Output is : %d' % output
