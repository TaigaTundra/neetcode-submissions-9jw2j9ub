class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = {}

        for i,num in enumerate(nums):
            lookup[num] = lookup.get(num,0)+1

        max_freq = 0
        max_num = None
        res = []
        count = 0
        while count != k:
            max_freq = 0
            max_num = None
            for num,freq in lookup.items():
                if freq > max_freq:
                    max_freq = freq
                    max_num = num
            res.append(max_num)
            del lookup[max_num]
            count +=1 
        
        return res



