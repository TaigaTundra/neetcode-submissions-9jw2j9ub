class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Initialize L and R arrays of size n+1 with 1s.
        # This simplifies boundary conditions (L[0]=1 and R[n]=1).
        L = [1] * (n + 1)
        R = [1] * (n + 1)

        # 1. Calculate Prefix Products (L): L[i] = nums[0] * ... * nums[i-1]
        # Iterate from i=1 up to n (L[1] through L[n])
        for i in range(1, n + 1):
            L[i] = L[i-1] * nums[i-1]

        # 2. Calculate Suffix Products (R): R[i] = nums[i] * ... * nums[n-1]
        # Iterate from i=n-1 down to 0 (R[n-1] through R[0])
        for i in range(n - 1, -1, -1):
            R[i] = R[i+1] * nums[i]

        # R is now: [24, 12, 4, 1, 1] for [1, 2, 3, 4]

        # 3. Calculate Final Result (answer[i] = L[i] * R[i+1])
        answer = [0] * n
        for i in range(n):
            # L[i] is the product to the LEFT of nums[i]
            # R[i+1] is the product to the RIGHT of nums[i]
            answer[i] = L[i] * R[i+1]
            
        return answer

