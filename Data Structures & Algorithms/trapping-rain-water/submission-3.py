class Solution:
    def trap(self, heights: list[int]) -> int:
        n = len(heights)
        l_max = [0] * n 
        res = 0

        l_max[0] = heights[0]
        for i in range(1,n):
            l_max[i] = max(l_max[i-1],heights[i])
        
        r_max = 0
        for i in range(n-1,-1,-1):
            r_max = max(r_max,heights[i])
            res += min(l_max[i],r_max) -heights[i]
        
        return res

        