# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        root, prev = None, None
        reminder = 0

        while l1 or l2:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            s = val1 + val2 + reminder

            reminder = s // 10
            s = s % 10

            current = ListNode(s)
            if prev:
                prev.next = current
            else:
                root = current

            prev = current

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if reminder != 0:
            current.next = ListNode(reminder)

        return root





