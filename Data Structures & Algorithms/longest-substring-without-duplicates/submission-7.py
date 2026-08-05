class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0 
        sett = set()
        w_size_max = 0
        w_curr_size = 0

        while r < len(s):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            sett.add(s[r])
            w_size_max = max(w_size_max, r-l+1)
            r+=1

        return w_size_max
            

                

