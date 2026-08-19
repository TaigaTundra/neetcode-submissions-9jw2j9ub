class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count +=1 
            else:
                prod *=num
        if zero_count >1:
            return [0] * len(nums)

        elif zero_count ==1: 
            for i  in range(len(nums)):
                if nums[i] ==0:
                    nums[i] = prod
                else:
                    nums[i] = 0 
        else: 
            for i  in range(len(nums)):
                nums[i] = int(prod / nums[i])

        return nums





 