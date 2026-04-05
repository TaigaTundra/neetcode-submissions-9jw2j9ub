class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0,x 

        while l<=r:
            mid = (l+r) //2 
            target = mid*mid 

            if target<x:
                l = mid+1 
            elif target > x:
                r = mid -1 
            else:
                return mid 
        return r 
        