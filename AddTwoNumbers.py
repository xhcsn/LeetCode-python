# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        headNode = ListNode(0)
        point = headNode
        Sum = 0
        l1_mul = 1
        l2_mul = 1
        while (l1 != None)or(l2 != None):
            while (l1 !=None):
                Sum = Sum + l1.val*l1_mul
                l1 = l1.next
                l1_mul = l1_mul*10
            while (l2 !=None):
                Sum = Sum + l2.val*l2_mul
                l2 = l2.next
                l2_mul = l2_mul*10
        return Sum