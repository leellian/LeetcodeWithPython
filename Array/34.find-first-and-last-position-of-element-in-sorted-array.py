#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (32.95%)
# Total Accepted:    267.6K
# Total Submissions: 812K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# Example 1:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# 
# Example 2:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# 
#
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #1. O(N)
        # N = len(nums)
        # l,r = 0,N-1
        # l_pos,r_pos = -1,-1
        # while l<=r:
        #     mid = (l+r)//2
        #     if nums[mid]==target:
        #         l_pos = r_pos = mid
        #         mv_l = mv_r = mid
        #         #print 'midddddd',mid,l,r
        #         while 0<=l<=mv_l:
        #             #print 'mv_llllll',mv_l
        #             if nums[mv_l]==target:
        #                 l_pos = mv_l
        #                 mv_l -= 1
        #             else:
        #                 break
        #         while mv_r<=r<=N-1:
        #             #print 'mv_rrrrrr',mv_r
        #             if nums[mv_r]==target:
        #                 r_pos = mv_r
        #                 mv_r += 1
        #             else:
        #                 break
        #         return [l_pos,r_pos]
        #     elif nums[mid]<target<=nums[r]:
        #         l = mid+1
        #     else:
        #         r = mid-1
        # return [l_pos,r_pos]

        #2. log(N)
        N = len(nums)
        lo,hi = 0,N-1
        left,right = N,-1
        while lo<=hi:
            mid = (lo+hi)//2
            if nums[mid]==target:
                left = min(left,mid)
                hi = mid-1
            elif nums[mid]>target:
                hi = mid-1
            else:
                lo = mid+1
        
        lo,hi = 0,N-1
        while lo<=hi:
            mid = (lo+hi)//2
            if nums[mid]==target:
                right = max(right,mid)
                lo = mid+1
            elif nums[mid]>target:
                hi = mid-1
            else:
                lo = mid+1

        left = left if left!=N else -1
        right = right if right!=-1 else -1
        return [left,right]
