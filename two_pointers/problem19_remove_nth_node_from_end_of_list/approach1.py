class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode|None, n: int) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head

        first = dummy
        second = dummy

        for i in range(n + 1):
            first = first.next
        
        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next