#
# @lc app=leetcode id=75 lang=python
#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (41.50%)
# Total Accepted:    297.9K
# Total Submissions: 717.7K
# Testcase Example:  '[2,0,2,1,1,0]'
#
# Given an array with n objects colored red, white or blue, sort them in-place
# so that objects of the same color are adjacent, with the colors in the order
# red, white and blue.
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white,
# and blue respectively.
# 
# Note: You are not suppose to use the library's sort function for this
# problem.
# 
# Example:
# 
# 
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# 
# Follow up:
# 
# 
# A rather straight forward solution is a two-pass algorithm using counting
# sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
# array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?
# 
# 
#
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #1. two pointers, loop two times
        # if not nums:
        #     return
        # N = len(nums)
        # if N<=3:
        #     nums.sort()
        #     return
        # fast,slow = 0,0
        # while fast<N:
        #     if nums[fast]==0:
        #         nums[fast],nums[slow] = nums[slow],nums[fast]
        #         slow+=1
        #     fast+=1
        # fast = slow
        # while fast<N:
        #     if nums[fast]==1:
        #         nums[fast],nums[slow] = nums[slow],nums[fast]
        #         slow+=1
        #     fast+=1

        #2. brute force
        # if not nums:
        #     return
        # N = len(nums)
        # if N<=3:
        #     nums.sort()
        #     return
        # t_dict = {0:0,1:0,2:0}
        # for i in range(N):
        #     if nums[i] in t_dict.keys():
        #         t_dict[nums[i]] += 1
        # #可以优化下面代码
        # t_0,t_1= t_dict[0],t_dict[1]
        # for i in range(N):
        #     if i<t_0:
        #         nums[i] = 0
        #     elif t_0<=i<(t_1+t_0):
        #         nums[i] = 1
        #     else:
        #         nums[i] = 2

        #3. two pointers, loop 1 time
        if not nums:
            return
        N = len(nums)
        if N<=3:
            nums.sort()
            return
        fast,slow,flag = 0,0,0
        while slow<N and flag<2:
            if fast==N:
                fast=slow
                flag+=1
            if nums[fast]==flag:
                nums[fast],nums[slow]=nums[slow],nums[fast]
                slow+=1
            fast+=1

        

