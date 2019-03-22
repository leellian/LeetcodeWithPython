#
# @lc app=leetcode id=74 lang=python
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (34.69%)
# Total Accepted:    210.9K
# Total Submissions: 607.7K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# 
# 
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
# 
# 
# Example 1:
# 
# 
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 13
# Output: false
# 
#
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #1. binary search, two times
        # N = len(matrix)
        # if not N:
        #     return False
        # M = len(matrix[0])
        # if not M:
        #     return False
        # start,end = 0,N-1
        # while start<=end:
        #     mid = (start+end)//2
        #     mid_val = matrix[mid]
        #     if target<mid_val[0]:
        #         end = mid-1
        #     elif target>mid_val[M-1]:
        #         start = mid+1
        #     else:
        #         low,high = 0,M-1
        #         while low<=high:
        #             m_mid = (low+high)//2
        #             if target==mid_val[m_mid]:
        #                 return True
        #             if target<mid_val[m_mid]:
        #                 high = m_mid-1
        #             else:
        #                 low = m_mid+1
        #         return False
        # return False

        #2. binary search, reduce search counts, still two times
        # N = len(matrix)
        # if not N:
        #     return False
        # M = len(matrix[0])
        # if not M:
        #     return False
        # start,end = 0,N-1
        # while start<=end:
        #     mid = (start+end)//2
        #     mid_val = matrix[mid]
        #     if target<mid_val[0]:
        #         if mid-1>=0 and target > matrix[mid-1][M-1]:
        #             return False
        #         else:
        #             end = mid-1
        #     elif target>mid_val[M-1]:
        #         if mid+1<=N-1 and target<matrix[mid+1][0]:
        #             return False
        #         else:
        #             start = mid+1
        #     else:
        #         low,high = 0,M-1
        #         while low<=high:
        #             m_mid = (low+high)//2
        #             if target==mid_val[m_mid]:
        #                 return True
        #             if target<mid_val[m_mid]:
        #                 high = m_mid-1
        #             else:
        #                 low = m_mid+1
        #         return False
        # return False

        #3. binary search, one time!
        if not matrix or not matrix[0]:
            return False
        N,M = len(matrix),len(matrix[0])
        low,high = 0,N*M-1
        while low<=high:
            mid = (low+high)//2
            if target==matrix[mid/M][mid%M]:
                return True
            elif target<matrix[mid/M][mid%M]:
                high=mid-1
            else:
                low=mid+1
        return False

