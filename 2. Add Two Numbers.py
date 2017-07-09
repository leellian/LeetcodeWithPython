"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
#可以看做是两个数相加，需要考虑等长、不等长、进位等情况。
"""

#first commit; cost time:119ms
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = node = ListNode(0)
        carry = 0
        while True:
            if l1 and l2:
                value = (l1.val + l2.val + carry)%10
                tmp = ListNode(value)
                carry = (l1.val + l2.val + carry)/10
                node.next = tmp
                node = node.next
                l1 = l1.next
                l2 = l2.next
            elif not l1 and l2:
                value = (l2.val + carry)%10
                tmp = ListNode(value)
                carry = (l2.val + carry)/10
                node.next = tmp
                node = node.next
                l2 = l2.next
            elif l1 and not l2:
                value = (l1.val + carry)%10
                tmp = ListNode(value)
                carry = (l1.val + carry)/10
                node.next = tmp
                node = node.next
                l1 = l1.next
            elif not l1 and not l2 and carry != 0:
                value = carry%10
                carry = carry/10
                tmp = ListNode(value)
                node.next = tmp
            else:
                return result.next

#second commit; cost time:132ms
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = node = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry = l1.val + carry
                l1 = l1.next
            if l2:
                carry = l2.val + carry
                l2 = l2.next
            value = carry%10
            node.next = ListNode(value)
            node = node.next
            carry = carry/10
        return result.next
