class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m,n = len(s), len(t)

        if m !=n :
            return False 
        
        hash_s = {}
        hash_t = {}
        
        for i in range(m):
            hash_s[s[i]] = hash_s.get(s[i],0) +1 
            hash_t[t[i]] = hash_t.get(t[i],0) +1 
        
        return hash_s == hash_t 
