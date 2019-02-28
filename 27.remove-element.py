#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#
# https://leetcode.com/problems/remove-element/description/
#
# algorithms
# Easy (43.52%)
# Total Accepted:    371.6K
# Total Submissions: 853.4K
# Testcase Example:  '[3,2,2,3]\n3'
#
# Given an array nums and a value val, remove all instances of that value
# in-place and return the new length.
# 
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
# 
# The order of elements can be changed. It doesn't matter what you leave beyond
# the new length.
# 
# Example 1:
# 
# 
# Given nums = [3,2,2,3], val = 3,
# 
# Your function should return length = 2, with the first two elements of nums
# being 2.
# 
# It doesn't matter what you leave beyond the returned length.
# 
# 
# Example 2:
# 
# 
# Given nums = [0,1,2,2,3,0,4,2], val = 2,
# 
# Your function should return length = 5, with the first five elements of nums
# containing 0, 1, 3, 0, and 4.
# 
# Note that the order of those five elements can be arbitrary.
# 
# It doesn't matter what values are set beyond the returned length.
# 
# Clarification:
# 
# Confused why the returned value is an integer but your answer is an array?
# 
# Note that the input array is passed in by reference, which means modification
# to the input array will be known to the caller as well.
# 
# Internally you can think of this:
# 
# 
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeElement(nums, val);
# 
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len
# elements.
# for (int i = 0; i < len; i++) {
# print(nums[i]);
# }
# 
#
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #1. 两头往中间移动
        # l = len(nums)
        # if not l:
        #     return 0
        # if l == 1:
        #     return 1 if nums[0] != val else 0
        # start = 0
        # end = l - 1
        # while(start <= end):
        #     s_val = nums[start]
        #     e_val = nums[end]
        #     if s_val != val and e_val == val:
        #         start += 1
        #         end -= 1
        #     elif s_val == val and e_val != val:
        #         nums[start] = e_val
        #         start += 1
        #         end -= 1
        #     elif s_val == val and e_val == val:
        #         end -= 1
        #     else:
        #         start += 1
        # return start

        ##对于空间复杂度有要求的数组，注意双指针的使用：从头往后移动；头尾往中央移动等

        #2. 从头往后移动
        l = len(nums)
        if not l:
            return 0
        slow = 0
        for fast in range(l):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow

