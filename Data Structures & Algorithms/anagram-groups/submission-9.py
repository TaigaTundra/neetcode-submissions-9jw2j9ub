class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            counts = [0] *26 
            for char in word:
                counts[ord(char) -ord('a')] +=1
            key = tuple(counts)
            groups[key].append(word)
        
        return list(groups.values())