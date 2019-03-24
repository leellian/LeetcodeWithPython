# 
# @lc app=leetcode id=119 lang=python
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (42.41%)
# Total Accepted:    189.9K
# Total Submissions: 447.6K
# Testcase Example:  '3'
#
# Given a non-negative index k where k ≤ 33, return the k^th index row of the
# Pascal's triangle.
# 
# Note that the row index starts from 0.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 3
# Output: [1,3,3,1]
# 
# 
# Follow up:
# 
# Could you optimize your algorithm to use only O(k) extra space?
# 
#
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        #1. 递归，但是空间复杂度高
        # result = []
        # if rowIndex==0:
        #     return [1]
        # else:
        #     for i in range(rowIndex+1):
        #         if i==0 or i==rowIndex:
        #             result.append(1)
        #         else:
        #             sum = self.getRow(rowIndex-1)[i-1]+self.getRow(rowIndex-1)[i]
        #             result.append(sum)
        # return result

        #2. 只需要O(k)的空间，注意：在迭代的时候，如果从前往后计算，则result[j]的值会被改变，计算j+1的值的时候，j的值就不是上一行的值了。
        result = [0 for i in range(rowIndex+1)]
        if rowIndex==0:
            return [1]
        else:
            for i in range(rowIndex+1):
                for j in range(i,-1,-1):
                    if j==0 or j==i:
                        result[j] = 1
                    else:
                        result[j] = result[j]+result[j-1]
        return result
