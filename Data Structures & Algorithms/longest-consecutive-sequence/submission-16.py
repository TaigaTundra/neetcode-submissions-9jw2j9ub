class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        max_streak = 0

        for num in sett:
            if num - 1 not in sett:
                current_lenght = 1 
        
                while num + current_lenght in sett:
                    current_lenght+=1
                max_streak = max(max_streak,current_lenght)
        return max_streak
                

            
