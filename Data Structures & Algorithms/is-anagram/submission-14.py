class Solution:
    def isAnagram(self, s: str, t: str):
        counts_s = [0] *26 
        counts_t = [0] *26 

        if len(s)!= len(t):
            return False 
        
        for i in range(len(s)):
            counts_s[ord(s[i]) - ord('a')] +=1
            counts_t[ord(t[i]) - ord('a')] +=1
        
        return counts_t == counts_s
            