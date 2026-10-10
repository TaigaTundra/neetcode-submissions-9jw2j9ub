class Solution:
    def trap(self, heights: list[int]) -> int:
        n = len(heights)
        l_max = [0] * n 
        r_max = [0] *n 
        res = 0

        l_max[0] = heights[0]
        for i in range(1,n):
            l_max[i] = max(l_max[i-1],heights[i])
        
        r_max[-1] = heights[-1]
        for i in range(n-2,-1,-1):
            r_max[i] = max(r_max[i+1], heights[i])
        
        for i in range(n):
            res += min(l_max[i],r_max[i]) -heights[i]
        
        return res

        