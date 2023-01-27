from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2  # Our place in the input lists
        carry = 0  # Carry digit
        sentinel = ListNode()  # Placeholder at beginning of list
        ret_ptr = sentinel  # Our place in the return list

        while p1 and p2:
            # add a new digit to the return list
            new = ListNode()
            ret_ptr.next = new
            ret_ptr = new
            # add the next 2 input digits, plus carry
            s = p1.val + p2.val + carry
            # carry a 1 when sum >= 10
            carry = int(s >= 10)
            new.val = s % 10
            match (p1.next, p2.next, carry):
                case (ListNode(), None, _):
                    # extend shorter p2 with 0
                    p2.next = ListNode()
                case (None, ListNode(), _):
                    # extend shorter p1 with 0
                    p1.next = ListNode()
                case (None, None, 1):
                    # carry for final digit, extend both
                    p1.next, p2.next = ListNode(), ListNode()
                case _:
                    pass
            # advance the input list pointers
            p1, p2 = p1.next, p2.next

        return sentinel.next

