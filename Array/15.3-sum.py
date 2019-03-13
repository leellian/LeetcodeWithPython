#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (23.36%)
# Total Accepted:    483.5K
# Total Submissions: 2.1M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ####1. brute force####肯定会超时了...时间复杂度O(n³)
        # l = len(nums)
        # if l < 3:
        #     return []
        # result = []
        # for i in range(l):
        #     for j in range(i+1,l):
        #         for k in range(j+1,l):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 tmp = [nums[i], nums[j], nums[k]]
        #                 tmp.sort(reverse = False)
        #                 if tmp not in result:
        #                     result.append(tmp)
        #                 break
        # return result

        #2. 优化后版本 O(n²)
        # l = len(nums)
        # if l < 3:
        #     return []
        # nums.sort()
        # result = []
        # for i in range(l-2):
        #     j = i+1
        #     k = l-1
        #     while(j<k):
        #         if nums[i]+nums[j]+nums[k] == 0:
        #             tmp = [nums[i], nums[j], nums[k]]
        #             tmp.sort(reverse=False)
        #             if tmp not in result:
        #                 result.append(tmp)
        #             j += 1
        #             k -= 1
        #         elif nums[i]+nums[j]+nums[k] < 0:
        #             j += 1
        #         else:
        #             k -= 1
        # return result

        #3. 继续优化，减少重复
        # l = len(nums)
        # if l<3:
        #     return []
        # nums.sort()
        # preI = None
        # result = []
        # for i in range(l-2):
        #     j = i+1
        #     k = l-1
        #     if preI == nums[i]:
        #         continue
        #     preI = nums[i]                
        #     preJK = None
        #     while(j<k):
        #         if preJK == (nums[j],nums[k]):
        #             j += 1 
        #             #TODO 有点没想明白，到底是j++，还是k--，还是j++&&k--？
        #             #[-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]测试用例说明这里逻辑不对，不能直接用j++
        #             continue
        #         preJK = (nums[j],nums[k])
        #         if nums[i]+nums[j]+nums[k] == 0:
        #             result.append([nums[i],nums[j],nums[k]])
        #             j += 1
        #             k -= 1
        #         elif nums[i]+nums[j]+nums[k] < 0:
        #             j += 1
        #         else:
        #             k -= 1
        # return result

        #3  继续优化，减少重复 #逻辑正确版本，相比上一个提交
        l = len(nums)
        if l<3:
            return []
        nums.sort()
        preI = None
        result = []
        for i in range(l-2):
            j = i+1
            k = l-1
            if preI == nums[i]:
                continue
            preI = nums[i]                
            preJK = None
            while(j<k):
                if preJK == (nums[j],nums[k]):
                    j += 1
                    k -= 1 
                    #将preJK的赋值放在==0的情况，这样就能确定j k的变化了
                    continue
                if nums[i]+nums[j]+nums[k] == 0:
                    result.append([nums[i],nums[j],nums[k]])
                    preJK = (nums[j],nums[k])
                    j += 1
                    k -= 1
                elif nums[i]+nums[j]+nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return result

        #4 还有更牛逼的解法，参见wikipedia，后续继续研究 TODO
        #https://en.wikipedia.org/wiki/3SUM#Quadratic_algorithm
        

