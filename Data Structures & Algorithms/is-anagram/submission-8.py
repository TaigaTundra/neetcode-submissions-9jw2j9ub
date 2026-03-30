class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        if m!=n:
            return False
        hash_s = defaultdict(int)
        hash_t = defaultdict(int)

        for i in range(m):
            hash_s[s[i]] +=1 
            hash_t[t[i]] +=1 
        
        return hash_s == hash_t