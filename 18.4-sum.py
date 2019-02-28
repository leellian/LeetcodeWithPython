#
# @lc app=leetcode id=18 lang=python
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (29.65%)
# Total Accepted:    211.7K
# Total Submissions: 713.6K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
# 
# Note:
# 
# The solution set must not contain duplicate quadruplets.
# 
# Example:
# 
# 
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #1. O(n³)
        l = len(nums)
        if l < 4:
            return []
        nums.sort()
        result = []
        for i in range(l-3):
            for j in range(i+1,l-2):
                start = j+1
                end = l-1
                while(start<end):
                    sum = nums[i]+nums[j]+nums[start]+nums[end]
                    if sum == target:
                        tmp = [nums[i],nums[j],nums[start],nums[end]]
                        tmp.sort()
                        if tmp not in result:
                            result.append(tmp)
                        start += 1
                        end -= 1
                    elif sum < target:
                        start += 1
                    else:
                        end -= 1
        return result

        #2. 上面的方法竟然一次ac了，后续discuss看看其他人的解法，有没有复杂度更低的
        

