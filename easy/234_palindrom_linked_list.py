"""This solution is O(n) time and O(1) space.

1. Find the midpoint of the input list
2. Reverse the second half of the list in place, storing
   a pointer to the start of the second half
3. Compare the first half of the list with the reversed
   second half. If they are the same, the list is a
   palindrome.

"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def leq(l1, l2):
    """Lists are equal"""
    c1, c2 = l1, l2
    while (c1 and c2):
        if c1.val != c2.val:
            return False
        c1 = c1.next
        c2 = c2.next
    if c1 or c2:
        return False
    return True


def reverse_list(head):
    prev = None
    while (head):
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = head
        length = 0
        while n:
            length += 1
            n = n.next

        midpoint = length // 2

        if midpoint == 0:
            return True

        n = head
        for i in range(midpoint - 1):
            n = n.next

        if length % 2 == 0:
            start = n.next
        else:
            start = n.next.next

        n.next = None
        l = reverse_list(start)

        return leq(l, head)
