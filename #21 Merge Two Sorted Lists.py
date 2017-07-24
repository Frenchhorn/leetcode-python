'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sentinel = ListNode(None)
        r = sentinel

        while l1 and l2:
            if l1.val > l2.val:
                r.next = l2
                l2 = l2.next
            else:
                r.next = l1
                l1 = l1.next
            r = r.next

        if not l1 and l2:
            r.next = l2
        elif not l2 and l1:
            r.next = l1

        return sentinel.next