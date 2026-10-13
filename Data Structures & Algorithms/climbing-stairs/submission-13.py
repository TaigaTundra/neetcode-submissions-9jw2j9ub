class Solution:
    def climbStairs(self, n: int) -> int:
        curr =1
        prev=1


        for i in range(n-1):
            old_step = curr
            curr = curr+ prev 
            prev =  old_step 
        
        return curr 