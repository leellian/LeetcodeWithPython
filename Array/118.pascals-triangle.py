#
# @lc app=leetcode id=118 lang=python
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (44.90%)
# Total Accepted:    234.6K
# Total Submissions: 522.2K
# Testcase Example:  '5'
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 5
# Output:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
# 
#
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pas_triangle = [[] for i in range(numRows)]
        for i in range(numRows):
            if i==0:
                pas_triangle[i].append(1)
            else:
                for j in range(i+1):
                    if j==0 or j==i:
                        pas_triangle[i].append(1)
                    else:
                        sum = pas_triangle[i-1][j-1]+pas_triangle[i-1][j]
                        pas_triangle[i].append(sum)
        return pas_triangle

