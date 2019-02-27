#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (42.52%)
# Total Accepted:    318.2K
# Total Submissions: 748.5K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container and n is at least 2.
# 
# 
# 
# 
# 
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In
# this case, the max area of water (blue section) the container can contain is
# 49. 
# 
# 
# 
# Example:
# 
# 
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# 
#
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ############ Time Limit Exceeded ############
        # l = len(height)
        # cal = []
        # for i in xrange(l):
        #     for j in xrange(i+1, l):
        #         tmp = min(height[i],height[j]) * (j-i)
        #         cal.append(tmp)
        # cal.sort()
        # return cal[-1]

        ############ Time Limit Exceeded ############
        # l = len(height)
        # cal = 0
        # for i in xrange(l):
        #     for j in xrange(i+1,l):
        #         tmp = min(height[i],height[j]) * (j-i)
        #         cal = max(cal, tmp)
        # return cal

        ####有人说是dp算法，暂时还没弄明白，后续再看####
        cal = 0
        l = 0
        r = len(height) - 1
        while(l < r):
            cal = max(cal, min(height[l], height[r])*(r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return cal

