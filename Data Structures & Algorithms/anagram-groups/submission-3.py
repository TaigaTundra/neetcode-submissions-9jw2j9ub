class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        lookup = defaultdict(list)

        for word in strs:
            count = [0]*26
            for char in word:
                count[ord('a')-ord(char)]+=1
            key = tuple(count)
            lookup[key].append(word)
        return list(lookup.values())
            



            
    

            

