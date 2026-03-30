class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l,r = 0,len(heights)-1

        while l<=r:
            if heights[l]<=heights[r]:
                curr_area = heights[l]*(r-l)
                l+=1
            elif heights[l]>heights[r]:
                curr_area = heights[r]*(r-l)
                r-=1
            res = max(res,curr_area)

        return res        