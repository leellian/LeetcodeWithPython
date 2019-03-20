#
# @lc app=leetcode id=40 lang=python
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (40.37%)
# Total Accepted:    204.9K
# Total Submissions: 506.8K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sums to target.
# 
# Each number in candidates may only be used once in the combination.
# 
# Note:
# 
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
# [1,2,2],
# [5]
# ]
# 
# 
#
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.backtracking(target,candidates,result,0,[])
        return result

    def backtracking(self,target,candidates,result,index,temp):
            if target==0:
                result.append(temp+[])
                #print "3:",temp,target,result
                return
            for i in range(index,len(candidates)):
                if target>=candidates[i]:
                    temp.append(candidates[i])
                    #print "1:",temp,i,target,result
                    self.backtracking(target-candidates[i],candidates,result,i+1,temp)
                    temp.pop()
                    #print "2:",temp,i,target,result
        

