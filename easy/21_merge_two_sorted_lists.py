from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 or not list2:
            return list1 or list2

        # make sure list1 is the base
        if list2.val < list1.val:
            list1, list2 = list2, list1

        prev1 = ListNode(0, None)
        p1 = list1
        p2 = list2

        while p1 and p2:
            if p2.val < p1.val:  # insert value from p2 right before p1
                n = ListNode(p2.val, p1)
                prev1.next = n
                prev1 = n
                p1 = n.next
                p2 = p2.next
            else:  # move list1 pointer forward
                prev1 = p1
                p1 = p1.next

        # put the rest of the remaining list on the end
        prev1.next = p1 or p2

        return list1
