class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num]+=1
        freqs = [[] for _ in range(len(nums) + 1)]
        for val,freq in counts.items():
            freqs[freq].append(val)
        
        res = []
        for i in range(len(freqs) - 1, 0, -1):
            for num in freqs[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        
            
