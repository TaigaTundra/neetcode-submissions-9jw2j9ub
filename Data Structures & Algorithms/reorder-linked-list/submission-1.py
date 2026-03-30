class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find the middle of the list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half
        second_half = slow.next
        slow.next = None  # Detach the first half
        
        prev = None
        curr = second_half
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        second_half_reversed = prev

        # 3. Merge the two halves
        first_half = head
        while second_half_reversed:
            temp1 = first_half.next
            temp2 = second_half_reversed.next
            
            first_half.next = second_half_reversed
            second_half_reversed.next = temp1
            
            first_half = temp1
            second_half_reversed = temp2


        

        

