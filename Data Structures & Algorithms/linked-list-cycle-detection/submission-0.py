# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sl,fa = head , head
        while fa and fa.next:
            sl = sl.next
            fa = fa.next.next
            if fa ==sl:
                return True
        return False


        