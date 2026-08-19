class Solution:
    def hasDuplicate(self, nums: List[int]):
        return len(nums) > len(set(nums))