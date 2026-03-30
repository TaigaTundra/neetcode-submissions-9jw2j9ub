class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 0 

        for num in nums:
            curr_longest = 0
            if num - 1 not in sett:
                while num in sett:
                    num+=1
                    curr_longest +=1
                    longest = max(curr_longest, longest)
        return longest


        