class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i,num in enumerate(nums):
            count[num] = count.get(num,0)+1
        majority = len(nums) // 2

        for key,val in count.items():
            if val >majority:
                return key

        