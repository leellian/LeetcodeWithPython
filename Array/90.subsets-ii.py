#
# @lc app=leetcode id=90 lang=python
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (41.66%)
# Total Accepted:    192.3K
# Total Submissions: 461.3K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
# 
#
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        result = [[]]
        nums.sort()
        for i in range(1,len(nums)+1):
            self.backtracking(nums,i,0,[],result)
        return result

    def backtracking(self,nums,length,index,temp,result):
        if len(temp)==length:
            if temp+[] not in result:
                result.append(temp+[])
            return
        for i in range(index,len(nums)):
            if len(temp)<length:
                self.backtracking(nums,length,i+1,temp+[nums[i]],result)

