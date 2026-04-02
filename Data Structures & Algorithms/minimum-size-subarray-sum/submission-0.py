class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 
        longest = float('inf')
        count = 0

        for r in range(len(nums)):
            count +=nums[r]
            while count >=target:
                longest = min(longest, r-l+1)
                count-=nums[l]
                l+=1
        
        return longest if longest != float('inf') else 0


            
        