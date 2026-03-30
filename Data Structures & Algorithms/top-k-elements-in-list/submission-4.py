class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = {}
        freq = [[] for i in range(len(nums)+1)]
        res = []

        for num in nums:
            lookup[num] = lookup.get(num,0)+1
        
        for num,val in lookup.items():
            freq[val].append(num)
        
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        

        

