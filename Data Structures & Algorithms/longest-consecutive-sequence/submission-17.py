class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        max_count = 0

        for num in nums:
            if num -1 in sett:
                continue
            count = 1
            temp = num
            while temp +1 in sett:
                count+=1
                temp+=1
            max_count = max(count,max_count)

        return max_count 
