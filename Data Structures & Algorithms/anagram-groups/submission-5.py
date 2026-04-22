class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for w in strs: 
            temp = [0] *26
            for c in w:
                temp[ord(c) - ord('a')] +=1 
            key = tuple(temp)
            ans[key].append(w)

        return list(ans.values())  
