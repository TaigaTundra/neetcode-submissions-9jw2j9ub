class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r

        while l <= r:
            k = (l + r) // 2
            
            # Calculate total hours for this speed k
            total_hours = 0
            for p in piles:
                total_hours += math.ceil(p / k)
            
            # Check if this speed is a valid solution
            if total_hours <= h:
                ans = k
                r = k - 1  # Try a smaller speed
            else:
                l = k + 1  # Need a faster speed
        
        return ans
        