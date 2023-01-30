from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2

        if list2 is None:
            return list1

        p1 = list1
        prev1 = None
        p2 = list2

        base = list1

        while True:
            if prev1 and not p1:
                prev1.next = p2
                break
            if not p2:
                break

            if p2.val < p1.val:  # insert before p1
                n = ListNode(p2.val, p1)
                if prev1:
                    prev1.next = n
                else:
                    base = n

                prev1 = n
                p1 = n.next
                p2 = p2.next
            else:
                prev1 = p1
                p1 = p1.next

        return base
