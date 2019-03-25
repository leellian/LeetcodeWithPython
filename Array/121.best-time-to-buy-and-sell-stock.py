#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (46.48%)
# Total Accepted:    455K
# Total Submissions: 978K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
# 
# If you were only permitted to complete at most one transaction (i.e., buy one
# and sell one share of the stock), design an algorithm to find the maximum
# profit.
# 
# Note that you cannot sell a stock before you buy one.
# 
# Example 1:
# 
# 
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.
# 
# 
# Example 2:
# 
# 
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
# 
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #1. brute force:time limit exceeded
        # if not prices or len(prices)==1:
        #     return 0
        # N = len(prices)
        # for i in range(N-1,-1,-1):
        #     temp = 0
        #     for j in range(i-1,-1,-1):
        #         if prices[j]>=prices[i]:
        #             continue
        #         else:
        #             temp = max(temp,prices[i]-prices[j])
        #     prices[i] = temp
        # return max(prices[1::])
        
        #2. O(n)
        N = len(prices)
        if N<2:
            return 0
        min_val = prices[0]
        max_val = 0
        for i in range(N):
            min_val = min(min_val,prices[i])
            max_val = max(max_val,prices[i]-min_val)
        return max_val

