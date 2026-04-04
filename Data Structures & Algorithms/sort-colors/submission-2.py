class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0]*3 
        m = 0

        for num in nums:
            if num == 0:
                count[0]+=1
            elif num == 1:
                count[1] +=1
            else:
                count[2] +=1

        for i in range(3):
            while count[i]!= 0:
                nums[m] = i
                m+=1
                count[i] -= 1
        return nums 

