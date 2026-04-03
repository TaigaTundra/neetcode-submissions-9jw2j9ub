class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [0]* (2*len(nums))

        for i in range(2*len(nums)):
            if i < len(nums):
                res[i] = nums[i]
            else:
                res[i] = res[i-len(nums)]
        
        return res

        