class Solution:
    def hasDuplicate(self, nums: List[int]):
        sett = set(nums)
        return len(sett) != len(nums)