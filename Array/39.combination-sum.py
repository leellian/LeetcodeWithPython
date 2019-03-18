#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (46.96%)
# Total Accepted:    311.2K
# Total Submissions: 662.6K
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where the
# candidate numbers sums to target.
# 
# The same repeated number may be chosen from candidates unlimited number of
# times.
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
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
# 
#
class Solution(object):
    def combinationSum(self, candidates, target):
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
                    self.backtracking(target-candidates[i],candidates,result,i,temp)
                    temp.pop()
                    #print "2:",temp,i,target,result

