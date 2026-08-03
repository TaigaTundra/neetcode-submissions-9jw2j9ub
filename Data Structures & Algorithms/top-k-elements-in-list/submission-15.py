class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(list)
        res = [[]for _ in range (len(nums)+1)]
        ans = []

        for i,num in enumerate(nums):
            counts[num] = counts.get(num,0)+1
        
        for key,val in counts.items():
            res[val].append(key)
        
        for i in range(len(res)-1,0,-1):
            for num in res[i]:
                ans.append(num)
                if k == len(ans):
                    return ans






        