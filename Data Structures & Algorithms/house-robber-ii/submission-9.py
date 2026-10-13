class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(nums[0],self.rob_one(nums[1:]),self.rob_one(nums[:-1]))

    def rob_one(self,nums):
            n = len(nums)
            if n == 1:
                return nums[0]
            prev,curr = nums[0], max(nums[0],nums[1])
            for i in range(2,n):
                prev_curr = curr
                curr = max(curr, prev+nums[i])
                prev = prev_curr 
            return curr
        
        


