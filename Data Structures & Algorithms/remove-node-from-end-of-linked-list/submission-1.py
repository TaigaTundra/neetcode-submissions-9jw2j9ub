# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        rev_head = self.reverse(head)

        if n == 1:
            ans = self.reverse(rev_head.next)
            return ans

        curr = rev_head
        for i in range(n - 2):
            if not curr.next: 
                return self.reverse(rev_head)
            curr = curr.next
        curr.next = curr.next.next
        ans = self.reverse(rev_head)
        return ans  
         
    def reverse(self, head):
        prev = None 
        curr = head
        while curr:
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp 
        return prev 
