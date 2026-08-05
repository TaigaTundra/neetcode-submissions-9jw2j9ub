class Solution:
    def findMin(self, nums: List[int]) -> int:
        temp = nums[0]
        for num in nums:
            if num <temp:
                temp = num
        return temp
