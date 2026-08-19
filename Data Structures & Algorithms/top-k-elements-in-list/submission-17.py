class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[]for _ in range(len(nums)+1)]
        res = []

        for num in nums:
            counts[num] = counts.get(num,0)+1
        
        for i,num in counts.items():
            freq[num].append(i)
        
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if k == len(res):
                    return res 

        
            

