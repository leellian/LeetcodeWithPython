#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (32.63%)
# Total Accepted:    369.6K
# Total Submissions: 1.1M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# 
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# Example 1:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# 
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        if not l:
            return -1
        if l == 1:
            return 0 if nums[0]==target else -1
        start = 0
        end = l-1
        mid = (l-1)/2
        while(start<end):
            s_val = nums[start]
            e_val = nums[end]
            m_val = nums[mid]
            if m_val > s_val:
                start = mid
                mid = (start+end)/2
            elif m_val < e_val:
                end = mid
                mid = (start+end)/2
            else:
                start = mid
                end = mid+1
                break
        if target>nums[start] or target<nums[end]:
            return -1
        elif target>=nums[end] and target<=nums[-1]:
            s = end
            e = l-1
            m = (s+e)/2
            while(s<e):
                if nums[m]>target:
                    e = m
                    m = (s+e)/2
                elif nums[m] < target:
                    s = m
                    m = (s+e)/2
                else:
                    return m
            return -1
        elif target<=nums[start] and target>=nums[0]:
            s = 0
            e = start
            m = (s+e)/2
            while(s<e):
                if nums[m]>target:
                    e = m
                    m = (s+e)/2
                elif nums[m]<target:
                    s = m
                    m = (s+e)/2
                else:
                    return m
            return -1
        else:
            return -1

