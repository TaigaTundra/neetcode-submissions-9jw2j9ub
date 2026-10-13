class Solution:
    def rob(self, nums: List[int]) -> int:
        m = len(nums)
        if m == 1:
            return nums[0]
        if m == 2:
            return max(nums[0],nums[1])

        def rob_one(nums):
            n = len(nums)
            prev,curr = nums[0], max(nums[0],nums[1])
            for i in range(2,n):
                prev_curr = curr
                curr = max(curr, prev+nums[i])
                prev = prev_curr 
            return curr
        
        return max(rob_one(nums[1:]),rob_one(nums[:-1]))


