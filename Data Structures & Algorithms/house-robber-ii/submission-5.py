class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            n = len(arr)
            if n == 1:
                return arr[0]
            dp1 = [0]* n

            dp1[0], dp1[1] = arr[0], max(arr[0],arr[1])
            for i in range(2,n):
                dp1[i] = max(dp1[i-1], dp1[i-2]+arr[i])
            return dp1[n-1]
        return max(helper(nums[:-1]), helper(nums[1:]))