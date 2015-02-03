#!/usr/bin/python
# coding=utf-8
# File Name: two_sum.py
# Developer: Vincent Fei
# Data: Mon Feb  2 22:12:01 2015
'''
Question:

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the 
target, where index1 must be less than index2. Please note that your returned answers 
(both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''
class solution(object):
    #@return tuple(index1, index2)
    def twosum(self, numbers, target):
        dic = {}
        for i, value in enumerate(sorted(numbers)):
            if value in dic: # if found the remain value in dic key
                return (dic[value]+1, i+1)
            else:
                dic[target-value] = i

if __name__ == '__main__':

    #test
    num1 = [1,3,5,7,9,10]
    target1 = 12
    num2 = [0,2,3,5,22]
    target2 = 5

    get_it = solution()
    result1 = get_it.twosum(num1, target1)
    result2 = get_it.twosum(num2, target2)

    print "Test 1 :"
    print "The Input : %s" % num1 
    print "Target : %d" % target1
    print "The Output: Index1: %d, Index2: %d" %(result1[0], result1[1])
    print
    print "Test 2 :"
    print "The Input : %s Target : %d" %(num2,target2)
    print "The Output: Index1: %d, Index2: %d" %(result2[0], result2[1])

