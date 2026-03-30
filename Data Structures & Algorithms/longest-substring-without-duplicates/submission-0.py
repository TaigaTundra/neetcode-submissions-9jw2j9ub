class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = set()
        l=0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1                
            seen.add(s[r])
            curr_longest =r-l+1
            longest = max(longest,curr_longest)
        
        return longest