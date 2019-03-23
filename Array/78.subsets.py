#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (51.45%)
# Total Accepted:    339.7K
# Total Submissions: 660.1K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        result = [[]]
        N = len(nums)+1
        for i in range(1,N):
            self.backtracking(nums,i,0,[],result)
        return result

    def backtracking(self,nums,length,index,temp,result):
        if len(temp)==length:
            result.append(temp+[])
            return
        for i in range(index,len(nums)):
            if len(temp)<length:
                self.backtracking(nums,length,i+1,temp+[nums[i]],result)

        

