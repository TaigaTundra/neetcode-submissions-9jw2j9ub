class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26 
        max_win = 0
        l,r = 0,0 

        while r <len(s):
            counts[ord(s[r])-ord('A')] +=1
            while (r-l+1)-max(counts) > k:
                counts[ord(s[l])-ord('A')]-=1
                l+=1
            max_win = max(max_win,r-l+1)
            r+=1
        
        return max_win

        