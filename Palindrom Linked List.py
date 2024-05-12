# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: [ListNode]) -> bool:
        def reverseLinkedList(node):
            prev = None
            current = node
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half_reversed = reverseLinkedList(slow)
        
        while second_half_reversed:
            if head.val != second_half_reversed.val:
                return False
            head = head.next
            second_half_reversed = second_half_reversed.next
        
        return True