"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

#first commit
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return []
        nums_len = len(nums)
        for idx_i in xrange(nums_len):
            for idx_j in xrange(idx_i+1, nums_len):
                if nums[idx_i] + nums[idx_j] == target:
                    return [idx_i, idx_j]
        return []

#second commit with hash table
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return False
        tmp_dict = {}
        for idx, value in enumerate(nums):
            if value in tmp_dict:
                return [tmp_dict[value],idx]
            else:
                tmp_dict[target-value] = idx
        return False
