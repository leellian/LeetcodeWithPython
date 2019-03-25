#
# @lc app=leetcode id=120 lang=python
#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (38.57%)
# Total Accepted:    172.5K
# Total Submissions: 447.1K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you
# may move to adjacent numbers on the row below.
# 
# For example, given the following triangle
# 
# 
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
# 
# 
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# 
# Note:
# 
# Bonus point if you are able to do this using only O(n) extra space, where n
# is the total number of rows in the triangle.
# 
#
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
    #     #1. brute force 把所有排列都找出来，min一下，往下可延伸的条件是[j-1,j,j+1]的范围，注意边界
    #     if not triangle:
    #         return None
    #     if len(triangle)==1:
    #         return triangle[0][0]
    #     if len(triangle)==2:
    #         sum1 = triangle[0][0] + triangle[1][0]
    #         sum2 = triangle[0][0] + triangle[1][1]
    #         return min(sum1,sum2)
    #     result = []
    #     self.backtracking(triangle,0,0,[],result)
    #     def sum(plist):
    #         all = 0
    #         for i in plist:
    #             all+=i
    #         return all
    #     p = map(lambda i:sum(i),result)
    #     p.sort()
    #     return p[0]
    
    # def backtracking(self,triangle,height,index,temp,result):
    #     if height>len(triangle)-1:
    #         return
    #     if height==len(triangle)-1:
    #         #print '3333,height:%d,index:%d,temp:%r,result:%r'%(height,index,temp,result)
    #         if index==0:
    #             for i in range(0,2):
    #                 t = temp+[triangle[height][i]]
    #                 result.append(t)
    #         else:
    #             #print '4444,height:%d,index:%d,temp:%r,result:%r'%(height,index,temp,result)
    #             for i in range(index-1,index+2):
    #                 t = temp + [triangle[height][i]]
    #                 result.append(t)
    #         return
    #     if index==0:
    #         for i in range(0,min(len(triangle[height]),2)):
    #             #print '11111,height:%d,i:%d,index:%d,temp:%r,result:%r'%(height,i,index,temp,result)
    #             self.backtracking(triangle,height+1,i,temp+[triangle[height][i]],result)
    #     else:
    #         for i in range(index-1,index+2):
    #             #print '22222,height:%d,i:%d,index:%d,temp:%r,result:%r'%(height,i,index,temp,result)
    #             self.backtracking(triangle,height+1,i,temp+[triangle[height][i]],result)
        
        #2. dp bottom-up 从上到下范围弄错了，第ij个节点，其上一行的邻接点只有i-1,j-1和i-1,j
        if not triangle:
            return None
        if len(triangle)==1:
            return triangle[0][0]
        N = len(triangle)
        for i in range(1,N):
            M = len(triangle[i])
            for j in range(M):
                t = triangle[i][j]
                s = [t+triangle[i-1][k] for k in range(max(j-1,0),min(j+1,M-1))]
                triangle[i][j] = min(s)
        return min(triangle[N-1])



