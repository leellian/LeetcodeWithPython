#
# @lc app=leetcode id=16 lang=python
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (39.89%)
# Total Accepted:    283.9K
# Total Submissions: 702.4K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
#
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #1. 写的不够简洁
        # l = len(nums)
        # if l<3:
        #     return 0
        # nums.sort()
        # result = nums[0]+nums[1]+nums[2]
        # cmp = abs(result - target)
        # for i in range(l-2):
        #     j = i+1
        #     k = l-1
        #     while(j<k):
        #         if nums[i]+nums[j]+nums[k] == target:
        #             return target
        #         elif nums[i]+nums[j]+nums[k]-target>0:
        #             tmp = nums[i]+nums[j]+nums[k]-target
        #             result = result if cmp<tmp else nums[i]+nums[j]+nums[k]
        #             cmp = min(cmp, tmp)
        #             k -= 1
        #         else:
        #             tmp = abs(nums[i]+nums[j]+nums[k]-target)
        #             result = result if cmp<tmp else nums[i]+nums[j]+nums[k]
        #             cmp = min(cmp, tmp)
        #             j += 1
        # return result

        #2. 改进更简洁一些
        l = len(nums)
        pre_target = None
        if l < 3:
            return 0
        nums.sort()
        for i in range(l-2):
            j = i+1
            k = l-1
            while(j<k):
                s = nums[i]+nums[j]+nums[k]
                if pre_target is None:
                    pre_target = s
                if abs(s-target) < abs(pre_target-target):
                    pre_target = s
                if s-target == 0:
                    return s
                elif s-target>0:
                    k -= 1
                else:
                    j += 1
        return pre_target

        

