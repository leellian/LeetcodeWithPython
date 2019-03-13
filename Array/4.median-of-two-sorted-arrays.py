#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (25.46%)
# Total Accepted:    381.3K
# Total Submissions: 1.5M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# 
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# 
# Example 2:
# 
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# 
#
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        tmp_list = []
        while(l1 > 0 and l2 > 0):
            if nums1[l1-1] > nums2[l2-1]:
                tmp_list.append(nums1[l1-1])
                l1 -= 1
            else:
                tmp_list.append(nums2[l2-1])
                l2 -= 1
        if l1 > 0:
            for i in range(l1, 0, -1):
                tmp_list.append(nums1[i-1])
        if l2 > 0:
            for i in range(l2, 0, -1):
                tmp_list.append(nums2[i-1])
        l3 = len(tmp_list)
        if l3%2==0:
            return float(tmp_list[l3/2]+tmp_list[l3/2-1])/2
        else:
            s = (l3-1) / 2
            return tmp_list[s]
        # result = (tmp_list[l3/2]+tmp_list[l3/2-1])/2 if l3%2==0 else tmp_list[(l3-1)/2)]


        
