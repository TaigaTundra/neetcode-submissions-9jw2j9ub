class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 
        shortest = float('inf')
        count = 0

        for r in range(len(nums)):
            count +=nums[r]
            while count >=target:
                shortest = min(shortest, r-l+1)
                count-=nums[l]
                l+=1
        
        return shortest if shortest != float('inf') else 0


            
        