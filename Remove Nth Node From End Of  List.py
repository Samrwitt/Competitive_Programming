# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next=head
        first=dummy
        second=dummy

        for _ in range(n+1):
            second=second.next
        
        while second is not None:
            second=second.next
            first=first.next

        first.next=first.next.next
       
        return dummy.next 