class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head.next 

        while f and f.next:
            s = s.next
            f = f.next.next

        second = s.next
        prev = s.next = None

        while second:
            temp = second.next
            second.next = prev 
            prev = second 
            second = temp 
        
        second = prev 
        first = head 

        while second :
            temp1, temp2 = first.next, second.next
            first.next = second 
            second.next = temp1 
            first,second = temp1, temp2 






