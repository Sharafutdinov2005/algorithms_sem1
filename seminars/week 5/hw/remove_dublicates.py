from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        helper = ListNode(0)
        helper.next = head
        prev = helper
        current = head

        while current:
            if current.next and current.val == current.next.val:
                value = current.val
                while current and current.val == value:
                    current = current.next
                prev.next = current
            else:
                prev = current
                current = current.next

        return helper.next
