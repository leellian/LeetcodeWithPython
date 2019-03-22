#
# @lc app=leetcode id=73 lang=python
#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (39.13%)
# Total Accepted:    194.8K
# Total Submissions: 497.6K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in-place.
# 
# Example 1:
# 
# 
# Input: 
# [
# [1,1,1],
# [1,0,1],
# [1,1,1]
# ]
# Output: 
# [
# [1,0,1],
# [0,0,0],
# [1,0,1]
# ]
# 
# 
# Example 2:
# 
# 
# Input: 
# [
# [0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]
# ]
# Output: 
# [
# [0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]
# ]
# 
# 
# Follow up:
# 
# 
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
# 
# 
#
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #1. brute force O(m+n)
        if not matrix or not matrix[0]:
			return
        rows,cols = set([]),set([])
        N,M = len(matrix),len(matrix[0])
        S = N*M
        for i in range(S):
            if matrix[i/M][i%M]==0:
                rows.add(i/M)
                cols.add(i%M)
        for i in range(S):
            if i/M in rows or i%M in cols:
                matrix[i/M][i%M]=0

        #2. improve method
